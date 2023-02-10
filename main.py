from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def func():
    return {"message":"hello"}

if __name__ == "__main__":
    uvicorn.run(app, port = 9000, host="0.0.0.0")
