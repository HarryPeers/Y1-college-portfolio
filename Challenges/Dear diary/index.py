from sys import path as systemPath
from os import getcwd

cwd = getcwd()
systemPath.append(f"{cwd}/dependancies/")


from fastapi import *
from uvicorn import run
from datetime import datetime
from json import load, dump

def get_entries(app):
    with open(f"{app.cwd}/entries.json") as file:
        return load(file)

def write_entries(app, entries):
    with open(f"{app.cwd}/entries.json", "w") as file:
        dump(entries, file, indent=3)

app = FastAPI()
app.cwd = cwd

@app.get("/") 
async def index(request:Request):
    return responses.FileResponse(f"{request.app.cwd}/index.html")

@app.get("/font/{file}")
async def index(request:Request, file):
    return responses.FileResponse(f"{request.app.cwd}/font/{file}")

@app.get("/entries")
async def entries(request:Request):
    return get_entries(request.app)

@app.post("/entries/comment") 
async def comment(request:Request):
    payload = await request.json()
    entries = get_entries(request.app)
    entries[payload["postname"]]["comments"].append({"content": payload["content"], "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    write_entries(request.app, entries)


if __name__ == "__main__":
    run("index:app", host="127.0.0.1", port=80)