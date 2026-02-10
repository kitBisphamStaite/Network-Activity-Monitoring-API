from fastapi import FastAPI

app = FastAPI()

# Run:
# uvicorn main:app --reload

@app.get("/")
def root():
    return {"status": "running"}
