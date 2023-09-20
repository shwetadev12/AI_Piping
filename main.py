from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router_POST import router as router_POST

app = FastAPI()

app.include_router(router_POST)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)