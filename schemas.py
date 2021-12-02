from pydantic import BaseModel

'''
Uses data from socket to create a new user.
'''
class User(BaseModel):
    username: str #  = WebServer.get_username()
    room_id: int #   = WebServer.assign_user_to_room
    user_id: int # = WebServer.player_count


'''
Creates a playable location for 6 players to carry out 
their game of Poker. 
'''
class Room(BaseModel):
    room_player_count: int
    room_user_ids: dict

