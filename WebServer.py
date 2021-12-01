from fastapi import FastAPI, WebSocket
import schemas
import math

fastapi = FastAPI()
DEFAULT_BALANCE = 25000
players = {}
player_count = 0
username = ""

'''
Sends Client to connect to websocket 
'''


@fastapi.get("/")
def home_page():
    return websocket_endpoint


'''
Creates a websocket for the client to connect to
Client sends username
Variable 'username' is used to create a new "user" which assigns 
a user id and room id for the client to connect and play
'''


@fastapi.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("Websocket is now live. Accepting Client connections...")
    await websocket.accept()
    while True:
        try:
            await websocket.send_json("Enter a username: ")
            username = str(await websocket.receive_text())
            create_new_user(username, player_count)
        except Exception as e:
            print("Error Occurred. Connection has been closed.")
            await websocket.close()
            break


'''
Uses the Client-input variable 'username' to create a new user
and add the new user to the players dictionary
'''


@fastapi.post("/create-user")
def create_new_user(username, player_count):
    players[player_count] = {username: schemas.User.username, DEFAULT_BALANCE: schemas.User.balance,
                             assign_user_to_room: schemas.User.room_id, get_user_id(): schemas.User.user_id}
    player_count += 1
    send_user_to_room(get_user_id(), assign_user_to_room())


'''
Finds and returns the user id, assists in assigning user to room
'''


def get_user_id():
    return schemas.User.user_id


'''
Finds and returns the username. 
'''

def get_username():
    return username


'''
Will check user_id and see what range it falls in
Based on that range it will assign to a Room correlating to that range
(user_id 17 -> (int) math.ceiling(user_id/6) = 3, so user assigned to room 3)
'''


@fastapi.post("/assign-room")
def assign_user_to_room():
    user_id = get_user_id()
    room = math.ceil(user_id / 6)
    return room

'''
Will return the information necessary to have player join room they were assigned. 
'''


@fastapi.get("/joining-room")
def send_user_to_room(room: schemas.User.room_id):
    user = get_user_id()
    room.add(user)

