from fastapi import APIRouter, WebSocket
import websocket
from fastapi.exceptions import FastAPIError
from starlette.requests import Request
from starlette.responses import Response

from game import Game
from schemas import AddUserReq

class Router:
    router = APIRouter()
    # game =  Game()
    @router.get('/')
    async def getHome(self):
        return "hello world"

    @router.post('/user/create')
    async def createUser(req: AddUserReq):
        Game()._instance.create_new_user(req.userName)

    @router.websocket('/ws')
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        while True:
                data = await websocket.receive_text()
                await websocket.send_text("Data Received")

    @router.websocket('/ws/{tableId}')
    async def getTable(websocket: WebSocket, tableId: int):
        Game()._instance.connect_to_table(tableId)

        while True:
            await websocket.send(Game()._instance.get_table(tableId))
