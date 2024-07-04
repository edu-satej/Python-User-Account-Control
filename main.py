import sqlite3 as sql

class database:
    def __init__(self, file):
        self.conn = sql.connect(file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")

    def query(self, cmd, params=None):
        if params: self.cur.execute(cmd, params)
        else: self.cur.execute(cmd); self.conn.commit()
        return self.cur.fetchone()

    def silentquery(self, cmd, params=None):
        if params: self.cur.execute(cmd, params)
        else: self.cur.execute(cmd)
        self.conn.commit()

    def __del__(self): self.conn.close()

def login(db, usr, pwd):
    if db.query("SELECT * FROM users WHERE username = ? AND password = ?", (usr, pwd)): response = "SUCCESSFULLY LOGGED IN"
    else: response = "ERR: INVALID CREDENTIALS"
    return response

def signup(db, usr, pwd):
    try: db.silentquery("INSERT INTO users (username, password) VALUES (?, ?)", (usr, pwd)); response = "SUCCESSFULLY CREATED"
    except sql.IntegrityError: response = "ERR: USERNAME ALREADY EXISTS"
    return response

# APPLIED CODE STARTS HERE
db = database("users.db")

while True:
    userinput = input("> ")
    words = userinput.split()
    if words[0] == "LOGIN" or words[0] == "SIGNUP":
        if words[1] == "AS":
            if words[3] == "WITH":
                if words[4] == "PASSWORD":
                    if words[0] == "LOGIN": print(login(db, words[2], words[5]))
                    elif words [0] == "SIGNUP": print(signup(db, words[2], words[5]))
                else: print("ERR: MISSING PASSWORD KEYWORD")
            else: print("ERR: MISSING WITH KEYWORD")
        else: print("ERR: MISSING AS KEYWORD")
    elif words[0] == "QUIT": db = None; break
    else: print("ERR: INVALID COMMAND ISSUED")
print("DATABASE CONNECTION CLOSED")
input("PRESS [ENTER] TO EXIT")
