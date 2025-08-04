from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(
    os.path.join(BASE_DIR, ".env"),
    override=True,
)

app = FastAPI(
    title="Cave API",
    description="API para gerenciamento de lances e relatórios",
    version="1.0.0",
)

# TODO alterar as origens permitidas para as URLs do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 7000))
    print(port)
    uvicorn.run(app, host="127.0.0.1", port=port)