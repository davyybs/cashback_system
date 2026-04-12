from fastapi import FastAPI

app = FastAPI()

from routes import router

app.include_router(router)

#para rodar o código, escrever no terminal: uvicorn main:app --reload