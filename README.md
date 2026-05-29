# ✍️ AI Writing Assistant

Web app untuk membantu menulis, memperbaiki, dan mengubah tone tulisan
menggunakan Large Language Model (LLM) via Groq API dengan fitur streaming real-time.

## ✨ Fitur
- **Tulis dari awal** — generate tulisan berdasarkan instruksi
- **Perbaiki teks** — improve grammar, struktur, dan kejelasan
- **Ubah tone** — formal, profesional, santai, persuasif, akademis, kreatif
- **Streaming real-time** — output muncul kata per kata seperti ChatGPT
- **Copy to clipboard** — salin hasil dengan satu klik

## 🛠️ Tech Stack
- Python 3.x
- FastAPI — backend API dengan streaming support
- Groq API (LLaMA 3.3 70B) — LLM inference
- HTML/CSS/JavaScript — frontend tanpa framework
- Uvicorn — ASGI server

## 🚀 Cara Menjalankan

**1. Clone repo:**
\```bash
git clone https://github.com/VaniaUlimazRivani/topikkhusus-ai-writing-assistant.git
cd topikkhusus-ai-writing-assistant
\```

**2. Install dependencies:**
\```bash
pip install fastapi uvicorn groq python-dotenv
\```

**3. Setup API key:**

Daftar gratis di [console.groq.com](https://console.groq.com) → buat API key

Buat file `.env`:
\```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
\```

**4. Jalankan:**
\```bash
uvicorn main:app --reload
\```

**5. Buka browser:**
\```
http://localhost:8000
\```

## 🏗️ Arsitektur

\```
User Input
    ↓
Frontend (HTML/JS)
    ↓ POST /generate
FastAPI Backend
    ↓ prompt engineering
Groq API (LLaMA 3.3 70B)
    ↓ streaming response
Frontend (real-time output)
\```

## 💡 Prompt Engineering

App ini menggunakan teknik prompt engineering:
- **System prompt** — mendefinisikan persona AI sebagai writing assistant
- **Mode-based prompting** — prompt berbeda untuk setiap mode (write/improve/tone)
- **Tone injection** — tone yang dipilih user diinjeksi langsung ke prompt

## 🗂️ Struktur Project
\```
ai-writing-assistant/
├── main.py          # FastAPI backend + streaming endpoint
├── static/
│   └── index.html   # Frontend (HTML/CSS/JS)
├── .env             # API key (tidak di-push ke GitHub)
└── .gitignore
\```
