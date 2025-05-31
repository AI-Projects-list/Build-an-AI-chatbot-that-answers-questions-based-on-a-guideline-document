# 🧠 AI Chatbot from Guideline Document

This project builds a chatbot that reads a guideline document, indexes its content using embeddings, and answers user queries using OpenAI or other LLMs. The chatbot is accessible through:

- ✅ Python backend API (Flask)
- ✅ WinForms Desktop App (C#)
- ✅ Web interface (Flask)

---

## 🚀 Features

- 📄 Guideline document processing (PDF/DOCX)
- 🔍 Embedding-based search (RAG)
- 🤖 Chatbot powered by OpenAI / LLM
- 🪟 Desktop UI via C# WinForms
- 🌐 Web UI via Flask

---

## 📁 Project Structure

```
ai_chatbot_project/
├── backend/                  # Python backend
│   ├── app.py                # Flask API
│   ├── chatbot.py            # RAG + LLM logic
│   ├── embeddings.py         # FAISS / embedding logic
│   ├── requirements.txt      # Dependencies
│
├── frontend_winform/         # C# WinForms Chatbot UI
│   ├── Program.cs
│   ├── Form1.cs
│   └── Form1.Designer.cs
│
├── frontend_web/             # Web UI using Flask
│   ├── app.py
│   ├── templates/index.html
│
└── README.md
```

---

## 🧠 Backend Setup (Python)

### Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Run Flask API
```bash
python app.py
```

---

## 🪟 WinForms Setup (C#)

1. Open `frontend_winform` in Visual Studio
2. Add new Windows Forms App (.NET Framework) project
3. Replace default files with provided:
   - `Form1.cs`
   - `Form1.Designer.cs`
   - `Program.cs`
4. Add `Newtonsoft.Json` via NuGet Package Manager
5. Run the project and test chatbot API call

---

## 🌐 Web Interface (Flask)

```bash
cd frontend_web
python app.py
```

Access at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠 Future Work

- Add document uploader
- Integrate advanced LLM like Claude or Gemini
- Support for offline LLMs like LLaMA2
- Host on Render / Azure / GCP

---

## 📬 API Endpoint

```
POST /chat
{
  "message": "your question here"
}
```

Response:
```json
{
  "reply": "answer from the document"
}
```

---

