from fastapi import FastAPI, WebSocket
import schemas
import math

fastapi = FastAPI()
players = {}
player_count = 0
username: str
user_id: int
room_id: int

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
def create_new_user(username, player_count, user: schemas.User):
    user_id = player_count
    room_id = get_room_id()
    players[player_count] = {username: user.username,
                             room_id: user.room_id,
                             user_id: user.user_id}

    player_count += 1
    send_user_to_room(user_id, room_id)


'''
Finds and returns the user id, assists in assigning user to room
'''
def get_user_id():
    return user_id

'''
Finds and returns the username. 
'''
def get_username():
    return username

'''
Finds and returns room_id value calculated by dividing the user id (which is the total number of players) by 6 (total 
number of players allowed at one table, or room)
'''
def get_room_id():
    assigned_room = math.ceil(user_id / 6)
    return assigned_room

'''
Will check user_id and see what range it falls in
Based on that range it will assign to a Room correlating to that range
(user_id 17 -> (int) math.ceiling(user_id/6) = 3, so user assigned to room 3)
'''
@fastapi.post(f"/assign-room/{create_new_user.user_id}")
def assign_user_to_room(user_id: int, Room: schemas.Room):
    assigned_room = get_room_id()
    if assigned_room > create_new_user.room_id.players[player_count - 1]:
        pass
    else:
        pass

    return assigned_room

'''
Will return the information necessary to have player join room they were assigned. 
'''
@fastapi.get("/joining-room")
def send_user_to_room(room: schemas.User.room_id):
    user = get_user_id()
    room.add(user)



@fastapi.put("/creating-new-room")
def create_new_room():



    pass


'''
Need to create a room object and call upon that here
room id will be number of room
will create a new room if room id changes
error occurs because
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File ".\WebServer.py", line 96, in <module>
    def send_user_to_room(room: schemas.User.room_id):
AttributeError: type object 'User' has no attribute 'room_id'

'''
