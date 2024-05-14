from fastapi import FastAPI
import uvicorn

from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "Welcome to FastAPI!"
    }

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)