from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class WriteRequest(BaseModel):
    mode: str
    tone: str
    user_text: str
    instruction: str

def build_prompt(req: WriteRequest) -> str:
    if req.mode == "write":
        return f"Tulis {req.tone} berdasarkan instruksi ini:\n\n{req.instruction}"
    elif req.mode == "improve":
        return f"Perbaiki teks berikut agar lebih {req.tone}:\n\n{req.user_text}\n\nInstruksi tambahan: {req.instruction}"
    elif req.mode == "tone":
        return f"Ubah tone teks berikut menjadi {req.tone}:\n\n{req.user_text}"
    return req.instruction

@app.post("/generate")
async def generate(req: WriteRequest):
    def stream():
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Kamu adalah AI Writing Assistant profesional. Bantu pengguna menulis, memperbaiki, dan mengubah tone tulisan dalam Bahasa Indonesia maupun Inggris. Berikan output langsung tanpa basa-basi."
                },
                {
                    "role": "user",
                    "content": build_prompt(req)
                }
            ],
            stream=True,
            max_tokens=1024
        )
        for chunk in completion:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    return StreamingResponse(stream(), media_type="text/plain")

app.mount("/", StaticFiles(directory="static", html=True), name="static")