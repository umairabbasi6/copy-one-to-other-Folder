from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def secure_root():
    return {"message": "You're on HTTPS (offline mode)!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=9000,  # or another port like 8443
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem"
    )
