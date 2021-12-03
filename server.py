from fastapi import FastAPI, File, UploadFile, APIRouter, Depends, Form

from router import Router
from starlette.middleware.cors import CORSMiddleware

class Server:
    def __init__(self):
        app = FastAPI()
        router = Router()
        app.include_router(router.router)
        self.app = app
        self.addMiddleware()
        


    def getOrigins(self):
        origins = [
            
            "http://localhost:3000",
        ]
        return origins

    def addMiddleware(self):
        origins = self.getOrigins()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=False,
            allow_methods=["*"],
            allow_headers=["*"],
        )
