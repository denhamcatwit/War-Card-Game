from pydantic import BaseModel
from typing import List

from starlette.websockets import WebSocket

'''
Uses data from socket to create a new user.
'''
class User():
    username: str #  = WebServer.get_username()
    room_id: int #   = WebServer.assign_user_to_room
    user_id: int # = WebServer.player_count

    def __init__(self, username, r_id, u_id):
        self.username = username
        self.room_id = r_id
        self.user_id = u_id



'''
Creates a playable location for 6 players to carry out 
their game of Poker. 
'''
class Table():
    users: List[User] = []
    pot: int = 0
    isActive: bool = False
    websocket: WebSocket

    def set_socket(self, ws: WebSocket):
        self.websocket = ws

class AddUserReq(BaseModel):
    userName: str

