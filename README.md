# 🗣️ Angel: A Voice-Controlled Virtual Assistant (V.A.)

**Angel** is an ambitious Python project designed to function as a basic virtual assistant, combining voice recognition with API integrations and advanced language processing capabilities powered by the Gemini API.

This project showcases fundamental Python skills in I/O (input/output), API handling, and system-level integrations.

## ✨ Core Features & Technical Stack

| Feature                     | Python Module/API Used      | Description                                                                                         |
| :-------------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------- |
| **Voice Recognition**       | `speech_recognition`        | Listens for the wake word "Angel" and converts spoken commands into text.                           |
| **Text-to-Speech (TTS)**    | `pyttsx3`                   | Synthesizes responses for audible feedback to the user.                                             |
| **Advanced Query Handling** | `google-genai` (Gemini API) | Uses the power of a Large Language Model to answer complex questions and general knowledge queries. |
| **Web Browser Control**     | `webbrowser`                | Opens common sites like Google, YouTube, and LinkedIn directly via voice command.                   |
| **News Retrieval**          | `requests` (News API)       | Fetches and reads the top 3 current news headlines.                                                 |

## 🚀 How to Set Up and Run Angel

### Prerequisites (Keys Required)

You need **Python 3** installed and your own personal API keys to run the assistant:

1.  **Google AI Studio API Key:** Get your key from Google AI Studio. This key replaces `"YOUR_GEMINI_API_KEY_HERE"` in the Python file.
2.  **News API Key:** Obtain a key from NewsAPI.org. This key replaces `"YOUR_NEWS_API_KEY_HERE"` in the Python file.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [your_repo_link]
    ```
2.  **Install Dependencies:**
    ```bash
    pip install speechrecognition pyttsx3 requests google-genai
    ```
3.  **Update API Keys:** Open `virtual_assistant.py` and manually replace the placeholder strings with your actual API keys.

### Execution

Run the script directly from your terminal:

```bash
python virtual_assistant.py
```

## 🎙️ How to Use

1.  The console will print `"Listening..."`.
2.  Say the wake word: **"Angel"**
3.  Angel will respond: `"Yes, how can I help you?"`
4.  Give your command, such as:
    - "Open YouTube"
    - "Tell me the news"
    - "What is the capital of France?" (This will trigger the Gemini API)

## 💡 Future Enhancements (Phase II)

This project is planned for continued development. Future features will include:

- **Robust Error Handling:** Better handling of audio timeouts and failed API calls.
- **Weather Integration:** Adding a function to fetch real-time weather data.
- **Calendar/Reminder Setting:** Integrating with system-level calendar APIs.
- **Code Refactoring:** Implementing a class structure for cleaner, object-oriented code.
- **Application Launching:** Adding command to open specific application.
