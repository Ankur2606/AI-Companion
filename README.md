# **AI-Companion**  
Your AI companion to support you during your lows and highs, providing intelligent, real-time assistance.

---

## **Overview**  
The AI Companion is a cutting-edge, low-latency voice assistant that:
- Converts voice input to text using OpenAI's Whisper.  
- Processes text using Hugging Face's Large Language Model (LLM).  
- Converts responses back to speech with Edge-TTS.  
- Features a web interface and real-time performance optimization for seamless interaction.  

---

## **Features**
- **Voice Activity Detection (VAD):** Detects speech activity and ignores silence.  
- **Speech-to-Text (STT):** High-accuracy transcription using the `faster-whisper` model.  
- **Text-to-Speech (TTS):** Converts text to natural speech with tunable pitch, speed, and voice type.  
- **LLM Integration:** Generates intelligent responses with Hugging Face models.  
- **Streamlit Interface:** Offers a user-friendly web-based interaction mode.  

---

## **Installation**

### **Install Daytona**

1. Run the following command to install Daytona:
   ```bash
   curl -sf -L https://download.daytona.io/daytona/install.sh | sudo bash
   ```

2. Start the Daytona server:
   ```bash
   daytona server -y && daytona
   ```

3. If the server daemon stops at any point, restart it using:
   ```bash
   daytona serve
   ```

4. Create a workspace for the AI Companion:
   ```bash
   daytona create https://github.com/Ankur2606/AI-Companion.git --devcontainer-path=.devcontainer/devcontainer.json
   ```

---

### **Manual Setup**

#### **Prerequisites**
- Python 3.8+  
- Git  
- Hugging Face API Token  

#### **Steps**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ankur2606/AI-Companion.git
   cd AI-Companion
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure Hugging Face Token:**
   - Create an account at [Hugging Face](https://huggingface.co/join) and generate an API token.
   - Set the token as an environment variable:
     ```bash
     export HUGGINGFACE_API_TOKEN=your_token  # On Windows: set HUGGINGFACE_API_TOKEN=your_token
     ```

---

## **Usage**

### **Daytona Mode**
Run the project through Daytona for optimized performance:
1. Start Daytona if not already running:
   ```bash
   daytona serve
   ```

2. Launch the AI Companion:
   ```bash
   daytona run
   ```

---

### **Manual Mode**


1. **Web Interface:**
   Launch the Streamlit web app:
   ```bash
   streamlit run main.py
   ```

---

## **Troubleshooting**

- **Daytona Server Issues:**  
  If the server stops, restart it with:
  ```bash
  daytona serve
  ```

- **Initial Model Downloads:**  
  The `faster-whisper` model may take time to download (~2GB). Ensure a stable internet connection.

- **Environment Variable Issues:**  
  Verify the Hugging Face API token is correctly set in your environment.

---

## **Contributing**
We welcome contributions! Please feel free to:
- Open issues for bugs or suggestions.
- Submit pull requests for improvements.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

