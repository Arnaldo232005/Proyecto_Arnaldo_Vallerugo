#Se importan los módulos requeridos
import json
from usuario import *
from albums import *
from songs import *
import webbrowser
import uuid
#Se crean las listas a usar y se importa el txt
artists=[]
listen=[]
NewUsers=[]
loadUsers=[]
x=open("NewUsers.txt","r")
contenido=x.read()
contenido_modificado=contenido.replace("'", "\"")
x.close()
y=open("NewUsers.txt","w")
y.write(contenido_modificado)
y.close()
final_y=open("NewUsers.txt","r")
NewUser2=json.load(final_y)
final_y.close()
for i in NewUser2:
    loadUsers.append(i)
#Se descarga los usuarios en los txt
def downloadNewUser(archivo):
    for i in archivo:
        if i["type"]=="listener":
            user = Oyente(i["id"], i["name"], i["email"], i["username"], i["type"],i["streams"], i["liked_songs"], i["liked_albums"],i["liked_artists"],i["liked_playlist"],i["song_played"])
            listen.append(user)
            NewUsers.append(user)
        elif i["type"]=="musician":
            user = Artista(i["id"], i["name"], i["email"], i["username"], i["type"],i["streams"], i["albums"], i["likes"])
            artists.append(user)
            NewUsers.append(user)
#Se descargan los usuarios en los json
def downloadUser(base_de_datos):
    for i in base_de_datos:
        if i["type"]=="listener":
            user = Oyente(i["id"], i["name"], i["email"], i["username"], i["type"],0, [], [],[],[],[])
            listen.append(user)
        elif i["type"]=="musician":
            user = Artista(i["id"], i["name"], i["email"], i["username"], i["type"], 0, [], 0)
            artists.append(user)
#Se define el buscador de usuarios
def SearchUser(artistas, escuchas,Usuario):
    #Se actualiza la lista loudUsers
    loadUsers = []
    x = open("NewUsers.txt", "r")
    contenido = x.read()
    contenido_modificado = contenido.replace("'", "\"")
    x.close()
    y = open("NewUsers.txt", "w")
    y.write(contenido_modificado)
    y.close()
    final_y = open("NewUsers.txt", "r")
    NewUser2 = json.load(final_y)
    final_y.close()
    for i in NewUser2:
        loadUsers.append(i)
    #Se escribe un nombre y se busca en loudUsers
    print('---Escribe el nombre de usuario a buscar---')
    x=input("---->")
    for i in loadUsers:
        if x ==i["username"]:
            if i["type"]=="musician":
                user=Artista(i["id"],i["name"],i["email"],i["username"],i["type"],i["streams"],i["albums"],i["likes"])
                print(user.show())
                if Usuario.type=="listener":
                    #En caso de que Usuario sea "listener" y el buscado es "musician"
                    #Se pueden ver y escuhar el album del artista buscado
                    print("--¿Que Album deseas escuchar?---")
                    album_escogido = input("---->")
                    for i in user.Albums:
                        i=Album(i["id"],i["name"],i["description"],i["cover"],i["published"],i["genre"],i["artists"],i["tracklist"],i["likes"],i["streams"])
                        if i.Name == album_escogido:
                            print(i.show())
                            print('''[1]---->Dar like
[2]---->Quitar like
[3]---->Salir''')
                            desicion = int(input("---->"))
                            if desicion == 1:
                                f_liked_albums = []
                                f_liked_albums.append(i.Name)
                                for x in Usuario.liked_albums:
                                    if x not in f_liked_albums:
                                        f_liked_albums.append(x)
                                Usuario.liked_albums = f_liked_albums
                                i.like()
                            elif desicion == 2:
                                f_liked_albums = []
                                for x in Usuario.liked_albums:
                                    if x not in f_liked_albums:
                                        f_liked_albums.append(x)
                                f_liked_albums.remove(i.Name)
                                Usuario.liked_albums = f_liked_albums
                                i.quitar_like()
                            elif desicion == 3:
                                pass
                            print('---Seleccione el nombre de la canción a escuchar en este album---')
                            for j in i.Tracklist:
                                print(j["name"])
                            cancion_escuchar = input("---->")
                            for j in i.Tracklist:
                                if j["name"] == cancion_escuchar:
                                    cancion_escogida = Song(j["id"], j["name"], j["duration"], j["link"], 0,j["streams"])
                                    print("Estas escuchando:")
                                    print(cancion_escogida.show())
                                    print('''[1]---->Dar like
[2]---->Quitar like
[3]---->Salir''')

                                    desicion = int(input("---->"))
                                    if desicion == 1:
                                        f_liked_songs = []
                                        f_liked_songs.append(cancion_escogida.Name)
                                        for x in Usuario.liked_songs:
                                            if x not in Usuario.liked_songs:
                                                f_liked_songs.append(x)
                                        Usuario.liked_songs = f_liked_songs
                                        cancion_escogida.like()
                                        loadUsers.append(Usuario.load())
                                        Guardado = open("NewUsers.txt", "w")
                                        Guardado.write(str(loadUsers))
                                        Guardado.close()
                                    elif desicion == 2:
                                        f_liked_songs = []
                                        for x in Usuario.liked_songs:
                                            if x not in Usuario.liked_songs:
                                                f_liked_songs.append(x)
                                        f_liked_songs.remove(cancion_escogida.Name)
                                        Usuario.liked_songs = f_liked_songs
                                        cancion_escogida.quitar_like()
                                        loadUsers.append(Usuario.load())
                                        Guardado = open("NewUsers.txt", "w")
                                        Guardado.write(str(loadUsers))
                                        Guardado.close()
                                    elif desicion == 3:
                                        webbrowser.open(cancion_escogida.Link)
                                        Usuario.cancion_escuchada(cancion_escogida.Name)
                                        Usuario.streams_aniadir()
                                        user.streams_aniadir()
                                        i.streams_aniadir()
                                        cancion_escogida.streams_aniadir()
                                        loadUsers.append(Usuario.load())
                                        Guardado = open("NewUsers.txt", "w")
                                        Guardado.write(str(loadUsers))
                                        Guardado.close()
                                    elif desicion==4:
                                        pass
            #Si el buscado es "listener" solo se imprimiran sus datos
            if i["type"]=="listener":
                user = Oyente(i["id"], i["name"], i["email"], i["username"], i["type"],i["streams"], i["liked_songs"], i["liked_albums"],i["liked_artists"],i["liked_playlist"],i["song_played"])
                print(user.show())
#Se define CreateUser para crear usuarios nuevos
def CreateUser():
    #Se selecciona el tipo de Usuario
    print('''¿Que tipo de usuario quieres crear?
[1]---->Musico
[2]---->Oyente''')
    y=int(input("---->"))
    if y==1:
        User=Artista(str(uuid.uuid4()),input("Name:"),input("Email:"),input("Username:"),"musician",0,[],[])
        loadUsers.append(User.load())
        Guardado = open("NewUsers.txt", "w")
        #El Usuario es guardado en el txt
        Guardado.write(str(loadUsers))
        Guardado.close()
        return User
    elif y==2:
        User1= Oyente(str(uuid.uuid4()), input("Name:"), input("Email:"), input("Username:"), "listener", 0, [],[],[],[],[])
        loadUsers.append(User1.load())
        # El Usuario es guardado en el txt
        Guardado = open("NewUsers.txt", "w")
        Guardado.write(str(loadUsers))
        Guardado.close()
        return User1






