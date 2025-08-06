from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routes.routers import router
from config import load_environment

load_environment()

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

app.include_router(
    router
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# if __name__ == "__main__":
#     import uvicorn
#     port = int(os.getenv("PORT", 8000))
#     server_host = os.getenv("SERVER_HOST", "127.0.0.1")
#     uvicorn.run(app, host=server_host, port=port)