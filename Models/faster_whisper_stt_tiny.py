import numpy as np
import soundfile as sf
import asyncio
from faster_whisper import WhisperModel
import time
import os
import streamlit as st
from io import BytesIO
import wave
import base64

# VAD Parameters
VAD_THRESHOLD = 0.01  # Adjust based on your environment

def create_audio_recorder():
    """Create an HTML/JavaScript audio recorder component"""
    return st.markdown(
        f"""
        <div>
            <audio id="recorder" style="display: none;"></audio>
            <script>
                const startRecording = async () => {{
                    const stream = await navigator.mediaDevices.getUserMedia({{ audio: true }});
                    const mediaRecorder = new MediaRecorder(stream);
                    const audioChunks = [];
                    
                    mediaRecorder.addEventListener("dataavailable", event => {{
                        audioChunks.push(event.data);
                    }});
                    
                    mediaRecorder.addEventListener("stop", () => {{
                        const audioBlob = new Blob(audioChunks, {{ type: 'audio/wav' }});
                        const reader = new FileReader();
                        reader.readAsDataURL(audioBlob);
                        reader.onloadend = () => {{
                            const base64Audio = reader.result.split(',')[1];
                            window.parent.postMessage({{
                                type: 'audio_data',
                                data: base64Audio
                            }}, '*');
                        }};
                    }});
                    
                    mediaRecorder.start();
                    return mediaRecorder;
                }};
                window.startRecording = startRecording;
            </script>
        </div>
        """,
        unsafe_allow_html=True
    )

async def process_audio_data(audio_data, output_dir="Testing/audio files"):
    """Process the received audio data with VAD"""
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Decode base64 audio data
        audio_bytes = base64.b64decode(audio_data)
        
        # Convert to numpy array
        with wave.open(BytesIO(audio_bytes), 'rb') as wav_file:
            audio = np.frombuffer(wav_file.readframes(wav_file.getnframes()), dtype=np.int16)
            audio = audio.astype(np.float32) / 32768.0  # Normalize to [-1, 1]
            sample_rate = wav_file.getframerate()
        
        # Apply VAD filtering
        if vad_filter(audio, threshold=VAD_THRESHOLD):
            # Save the audio file
            filename = os.path.join(output_dir, "stt_transcribe.flac")
            sf.write(filename, audio, sample_rate, format='FLAC')
            return filename
        else:
            print("No significant audio detected.\n")
            return None
            
    except Exception as e:
        print(f"Error processing audio: {e}")
        return None

def vad_filter(audio, threshold=VAD_THRESHOLD):
    """Voice Activity Detection filtering"""
    return np.max(np.abs(audio)) > threshold

async def transcribe_audio(filename, language="en"):
    """Transcribe audio using Faster-Whisper"""
    if not filename:
        return None
        
    try:
        model = WhisperModel("tiny", device="cpu", compute_type="int8")
        segments, info = model.transcribe(filename, language=language)
        
        transcribed_text = ""
        for segment in segments:
            transcribed_text += segment.text + " "
            
        return transcribed_text.strip()
        
    except Exception as e:
        print(f"Error in transcription: {e}")
        return None

async def capture_and_process_browser_audio(audio_data):
    """Main function to process browser-captured audio"""
    try:
        # Process the audio data
        audio_file = await process_audio_data(audio_data)
        
        if audio_file:
            # Transcribe the audio
            start = time.time()
            transcribed_text = await transcribe_audio(audio_file)
            end = time.time()
            print("Time taken: ", end-start)
            return transcribed_text
        
        return None
        
    except Exception as e:
        print(f"Error in audio processing: {e}")
        return None