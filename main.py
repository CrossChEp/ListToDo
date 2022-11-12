import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller.auth_controller import auth_router
from controller.user_controller import user_controller

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:63343",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller)
app.include_router(auth_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
