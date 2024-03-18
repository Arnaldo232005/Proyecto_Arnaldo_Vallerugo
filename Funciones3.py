#Se importan los módulos requeridos
from Funciones import *
from usuario import *
from playlist import*
from Funciones2 import *
#Se define introducción
def introduccion():
    #Se despliega el menu de la introducción
        print('''---Bienvenido  Metrofy---
    [1]---->Registrarte
    [2]---->Ingresar con cuenta ya creada''')
        x=int(input("---->"))
        if x ==1:
            #Se retorna la función CreateUser
            return CreateUser()
        if x==2:
            #Se descarga el Usuario de los txt
            print("Ingrese el usuario de tu cuenta")
            cuenta=input("---->")
            for i in NewUser2:
                if i["username"]==cuenta:
                    if i["type"]=="listener":
                        user=Oyente(i["id"],i["name"],i["email"],i["username"],i["type"],i["streams"],i["liked_songs"],i["liked_albums"],i["liked_artists"],i["liked_playlist"],i["song_played"],)
                        return user
                    if i["type"]=="musician":
                        user=Artista(i["id"],i["name"],i["email"],i["username"],i["type"],i["streams"],i["albums"],i["likes"])
                        return user
#Se define editarUsuario
def editarUsuario(Usuario):
    #Se remueve Usuria para actualizarlo
    loadUsers.remove(Usuario.load())
    print('''---Opciones--
    [1]---->Cambiar Datos
    [2]---->Salir''')
    e = int(input("---->"))
    if Usuario.type=="musician":
        if e == 1:
            #Se despliega menu para actualizar "musician"
            print('''---Dato a Cambiar---
    [1]---->Name
    [2]---->Correo
    [3]---->User
    [4]---->Type
''')
            j = int(input("---->"))
            if j == 1:
                NewData = input("---->")
                Usuario.Name = NewData
            elif j == 2:
                NewData = input("---->")
                Usuario.Correo = NewData
            elif j == 3:
                NewData = input("---->")
                Usuario.UserName= NewData
            elif j == 4:
                Usuario.type="listener"
            loadUsers.append(Usuario.load())
            Guardado = open("NewUsers.txt", "w")
            Guardado.write(str(loadUsers))
            Guardado.close()
        elif e == 2:
                pass
    elif Usuario.type=="listener":
        if e == 1:
            # Se despliega menu para actualizar "listener"
            print('''---Dato a Cambiar---
    [1]---->Name
    [2]---->Correo
    [3]---->User
    [4]---->Type
''')
            j = int(input("---->"))
            if j == 1:
                NewData = input("---->")
                Usuario.Name = NewData
            elif j == 2:
                NewData = input("---->")
                Usuario.Correo= NewData
            elif j == 3:
                NewData = input("---->")
                Usuario.UserName = NewData
            elif j == 4:
                Usuario.type="musician"
            Guardado = open("NewUsers.txt", "w")
            Guardado.write(str(loadUsers))
            Guardado.close()
        elif e == 2:
                pass
def mostrar_tu_playlist(Usuario):
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
    playlist = []
    x = open("NewPlaylist.txt", "r")
    contenido = x.read()
    contenido_modificado = contenido.replace("'", "\"")
    x.close()
    y = open("NewPlaylist.txt", "w")
    y.write(contenido_modificado)
    y.close()
    final_y = open("NewPlaylist.txt", "r")
    NewUser3 = json.load(final_y)
    final_y.close()
    for i in NewUser3:
        playlist.append(i)
    loadUsers.remove(Usuario.load())
    for x in playlist:
        if x["creator"]==Usuario.Name:
            Play = Playlist(x["id"], x["name"],x["description"], Usuario.Name, x["trask"],x["likes"],x["streams"])
            playlist.remove(Play.load())
            for id in Play.Tracks:
                for al in albums:
                    for song in al.Tracklist:
                        song_1 = Song(song["id"], song["name"], song["duration"], song["link"], 0, 0)
                        if song_1.Id == id:
                            print(song_1.Name)
            print('---Seleccione la canción a escuchar en este playlist---')
            ele = input("---->")
            for id in Play.Tracks:
                for al in albums:
                    for song in al.Tracklist:
                        song_1 = Song(song["id"], song["name"], song["duration"], song["link"], 0, 0)
                        if song_1.Id == id:
                            if song_1.Name == ele:
                                print(song_1.Name)
                                print("Estas escuchando:")
                                print(song_1.show())
                                print('''[1]---->Dar like
[2]---->Quitar like
[3]---->Escuchar
[4]---->Salir''')
                                desicion = int(input("---->"))
                                if desicion == 1:
                                    f_liked_songs = []
                                    f_liked_songs.append(song_1.Name)
                                    for x in Usuario.liked_songs:
                                        if x not in f_liked_songs:
                                            f_liked_songs.append(x)
                                    Usuario.liked_songs = f_liked_songs
                                    song_1.like()
                                    loadUsers.append(Usuario.load())
                                    Guardado = open("NewUsers.txt", "w")
                                    Guardado.write(str(loadUsers))
                                    Guardado.close()
                                elif desicion == 2:
                                    f_liked_songs = []
                                    for x in Usuario.liked_songs:
                                        if x not in f_liked_songs:
                                            f_liked_songs.append(x)
                                    f_liked_songs.remove(song_1.Name)
                                    Usuario.liked_songs = f_liked_songs
                                    song_1.quitar_like()
                                    loadUsers.append(Usuario.load())
                                    Guardado = open("NewUsers.txt", "w")
                                    Guardado.write(str(loadUsers))
                                    Guardado.close()
                                elif desicion == 3:
                                    webbrowser.open(song_1.Link)
                                    Usuario.cancion_escuchada(song_1.Name)
                                    Usuario.streams_aniadir()
                                    Play.streams_aniadir()
                                    song_1.streams_aniadir()
                                    loadUsers.append(Usuario.load())
                                    playlist.append(Play.load())
                                    Guardado = open("NewPlaylist.txt", "w")
                                    Guardado.write(str(playlist))
                                    Guardado.close()
                                    Guardado = open("NewUsers.txt", "w")
                                    Guardado.write(str(loadUsers))
                                    Guardado.close()
                                elif desicion == 4:
                                    pass