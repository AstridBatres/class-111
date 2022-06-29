from flask import Flask

app = Flask(__name__)



@app.get("/")
def index():
    return "<h1>Hello, world!</h1>"


@app.get("/about")
def get_about():
    me={
        "first_name": "Astrid",
        "last_name": "Guerrero",
        "hobbies": "hiking, working out",
        "active": True
    }

    return me