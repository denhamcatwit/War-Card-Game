from starlette.websockets import WebSocket
from schemas import Table, User


class Game:
    _instance = None
    tables: dict = {}
    users: dict = {}

    # def __init__(self):
    #     # return

    def __new__(cls):
        if cls._instance is None:
            # store = document_store.DocumentStore(urls=cls.urls, database=cls.db_name, certificate=cls.cert)
            # store.initialize()
            # cls.store = store

            # with store.open_session() as session:
            #     foo = Foo("PyRavenDB")
            #     session.store(foo)
            #     session.save_changes()

            cls._instance = super(Game, cls).__new__(cls)
            return cls._instance
        else:
            return cls._instance

    # Returns the number of users playing.
    def number_users(self):
        return len(self.users)

    # Return the number of tables active.
    def number_tables(self):
        return len(self.tables)

    # Creates a new user. Will assign a table or create a new table if all tables full.
    def create_new_user(self, name: str):

        numTables = self.number_tables()
        table: Table

        if numTables == 0:
            table = self.create_new_table(numTables)
        else:
            table = self.tables[self.number_tables()-1]
            if (len(table.users) == 2):
                table = self.create_new_table(self.number_tables()+1)


        newUserId = self.number_users()
        user: User = User(name, self.number_tables()-1, newUserId)

        self.users[newUserId] = user
        print(str(self.tables))

        table.users.append(user)
        self.tables[self.number_tables()-1] = table



        # userTable: Table = self.tables[user.room_id]
        # userTable.users.append(user)

# Creates a new table, subsequently creating another tableId and location for more clients to connect to.
    def create_new_table(self, tableId: int):
        newTableId: int = tableId
        table: Table = Table()

        self.tables[newTableId] = table
        print(len(self.tables))
        return table
    
    def connect_to_table(self, websocket: WebSocket, tableId: int):
        table: Table = self.tables[tableId]

        if (table.websocket == None):
            table.set_socket(websocket)

    def get_table(self, tableId: int):
        table: Table = self.tables[tableId]
        return table

# Function used within game logic to update client information every time game gets updated.
    async def broadcast(self, tableId, data):
        while True:
            ws: WebSocket = self.tables[tableId].websocket
            await ws.send_json(data)