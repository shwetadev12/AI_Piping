from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router_GET import router as router_GET

app = FastAPI()

app.include_router(router_GET)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
