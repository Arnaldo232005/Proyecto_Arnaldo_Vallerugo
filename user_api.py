import requests
import json
def api():
    u=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    if u.status_code==200:
        with open("users.json","w") as file:
            json.dump(u.json(),file,indent=4)
    u=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    if u.status_code==200:

        with open("albums.json","w") as file:
            json.dump(u.json(),file,indent=4)
    u=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
    if u.status_code==200:
        with open("playlists.json","w") as file:
            json.dump(u.json(),file,indent=4)


