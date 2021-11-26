from pydantic import BaseModel
import WebServer


'''
Uses data from socket to create a new user

I understand this is supposed to be a data model 
and is typically used differently but I made a mistake
*This portion of the comment will be removed later on*
'''
class User(BaseModel):
#    username = WebServer.get_username()
#    balance = WebServer.DEFAULT_BALANCE
#    room_id = WebServer.assign_user_to_room
#    user_id = WebServer.player_count
    username: str
    balance: float
    room_id: int
    user_id: int


'''
Creates a playable location for 6 players to carry out 
their game of Poker. 
'''
class Room(BaseModel):
    room_player_count: int
    room_user_ids = {}
    pass
