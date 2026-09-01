from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Enterprise CI/CD Demo"}


@app.get("/health")
def health():
    return {"status": "healthy"}