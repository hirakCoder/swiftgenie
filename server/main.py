from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI
import os

app = FastAPI(title="SwiftGenie API")

class Prompt(BaseModel):
    message: str

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set")
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

@app.post("/generate")
async def generate(prompt: Prompt):
    """Generate Swift code from a user prompt."""
    try:
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt.message}],
        )
        code = response.choices[0].message.content
        return {"code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
