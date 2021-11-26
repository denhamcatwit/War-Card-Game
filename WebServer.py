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


@fastapi.get("/joining-room")
def send_user_to_room(user: schemas.User.user_id, room: schemas.User.room_id):
    # Not sure how to create multiple Rooms as I'm not sure what
    # the Room will contain
    pass

'''
@fastapi.put("/player-balance")
def update_player_balance(username):
    try:
        # While writing this i remembered that player balances are supposed to be client side i think
        pass
    except Exception as e:
        # did not update balance
        pass

'''
##########################################################
####### Everything past this point is notes I took #######
####### while figuring this out watching TechW/Tim #######
####### So please ignore they are not amazing &    #######
#######      will be deleted in later updates      #######
##########################################################


'''
GET: returning information
POST: sending information to the post endpoint or the endpoint method 'post' 
ex: posting new user login or new user signup
PUT: update something that is already existing in the database, modifying existing information
DELETE: deletes information

API stands for Application Programming Interface
API is some web service that provides an interface to applications to implement and retrieve information
ex: amazon would have an api for inventory service, like stock, quantity, price, etc
separate from frontend system, api returns information to frontend 

THIS MEANS I DO NOT CREATE A SITE I SIMPLY CREATE AND PROVIDE INFORMATION TO THE FRONT END, 
MEANING I AM NOT MAKING ANY GUI OR SHOWING CARDS, I AM JUST "GET"TING USER IDS AND ROOM IDS BASED ON USER COUNTS

JSON is JavaScript Object Notation
FASTAPI JSONifies the information and sends it that way
We can work with strictly python types in our api
any returned data is auto converted to JSON

Path parameters/query parameters
ex: (inventory management system like amazon)
ivnentory = {
    1: {
        "name": "Milk"
        "price": 3.99
        "brand": "Regular"
    }
}

@app.get("/get_item/{item_id}") # Can take multiple params ex: @app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int): # The : int is a type id telling python it should be an integer
    return inventory[item_id]


Path function can be used importing Path
ex: 
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description = "The ID of the item you'd like to view. ")): 
    return inventory[item_id]

Path allows us to add more details or more restraints to our path parameters
always need to give a default value for the path parameter (can use None if there is always a value because it'll never be passed)

can add constraints
ex: greater than 0
def get_item(item_id: int = Path(None, description = "The ID of the item you'd like to view.", gt = 0, lt = 2 )): 
    return inventory[item_id]

Query parameters (comes after question mark in url)
ex: "facebook.com/home?redirect=/tim&msg=fail"
    redirect is a variable name, = means =, and after it is the value
    msg = fail

@app.get(/get-by-name)
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id] 
        return {"Data": "Not Found"}

'''