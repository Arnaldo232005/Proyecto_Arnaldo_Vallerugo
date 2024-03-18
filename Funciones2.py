#Se importan los módulos requeridos
from Funciones import *
from playlist import *
#Se crean las listas a usar
albums=[]
loadUsers=[]
playlist=[]
listen=[]
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
#Se descargan los Albums de los Usuarios creados
def downloadNewAlbums(archivo):
    for i in archivo:
        if i["type"]=="musician":
            user = Artista(i["id"], i["name"], i["email"], i["username"], i["type"],i["streams"], i["albums"], i["likes"])
            for x in user.Albums:
                album=Album(x["id"],x["name"],x["description"],x["cover"],x["published"],x["genre"],x["artists"],x["tracklist"],x["likes"],x["streams"])
                albums.append(album)
#Se descargan los Albums de los json
def downloadAlbums(base_de_datos):
    for i in base_de_datos:
        album=Album(i["id"],i["name"],i["description"],i["cover"],i["published"],i["genre"],i["artist"],i["tracklist"],0,0)
        albums.append(album)
#Se descargan los playlist
def downloadPlaylist(base_de_datos):
    for i in base_de_datos:
        play=Playlist(i["id"],i["name"],i["description"],i["creator"],i["tracks"],0,0)
        playlist.append(play)
#Se define createAlbums
def createAlbums (Usuario):
    #Se actualiza loadUsers
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
    #Se remueve el usuario para actualizarlo
    loadUsers.remove(Usuario.load())
    #Se crea el Album
    print('''---Crea tu album---''')
    Albums = Album(str(uuid.uuid4()),input("Name:"),input("Description:"),input("Cover:"),input("Published:"),input("Genre:"),Usuario.Name,[],0,0)
    print('''---Crea tu primera canción---''')
    Tracklists=Song(str(uuid.uuid4()),input("Name:"),input("Duration"),input("Link:"),0,0)
    (Albums.Tracklist).append(Tracklists.load())
    #Se añade el Album creado al creador y se vuelve añadir a loadUsers
    Usuario.Albums=[Albums.load()]
    loadUsers.append(Usuario.load())
    Guardado = open("NewUsers.txt", "w")
    Guardado.write(str(loadUsers))
    Guardado.close()
#Se define añadir cancion
def aniadir_cancion(Usuario):
    #Se actualiza loudUsers
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
    #Se remueve el usuario para actualizarlo
    loadUsers.remove((Usuario.load()))
    #Se selecciona el Album para añadir canción
    print("Escoge el Album para añadir canción")
    album_escogido=input("---->")
    for x in Usuario.Albums:
        if album_escogido==x["name"]:
            Albums = Album(x["id"], x["name"], x["description"], x["cover"],x["published"], x["genre"], x["artists"], x["tracklist"], x["likes"],x["streams"])
            #Se crea tu canción
            print('''---Crea tu canción---''')
            ej = Song(str(uuid.uuid4()), input("Name:"), input("Duration"), input("Link:"), 0,0)
            (Albums.Tracklist).append(ej.load())
            #Se añde el album al creador
            Usuario.Albums = [Albums.load()]
            loadUsers.append(Usuario.load())
            #Se guarda el Usuario
            Guardado = open("NewUsers.txt", "w")
            Guardado.write(str(loadUsers))
            Guardado.close()
#Se define escuchar música
def escuchar_musica(Usuario):
    #Se actualiza loudUser
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
    # Se remueve el usuario para actualizarlo
    loadUsers.remove(Usuario.load())
    #Se selecciona Album a buscar
    print("--¿Que Album deseas buscar?---")
    album_escogido=input("---->")
    for i in albums:
        if i.Name==album_escogido:
            print(i.show())
            #Una vez escogido le puedes dar like o quitarselo, si le das like puedes escuchar sus canciones
            print('''[1]---->Dar like
[2]---->Quitar like
[3]---->Salir''')
            desicion=int(input("---->"))
            if desicion==1:
                f_liked_albums=[]
                f_liked_albums.append(i.Name)
                for x in Usuario.liked_albums:
                    if x not in f_liked_albums:
                        f_liked_albums.append(x)
                Usuario.liked_albums=f_liked_albums
                i.like()
            elif desicion==2:
                f_liked_albums = []
                for x in Usuario.liked_albums:
                    if x not in f_liked_albums:
                        f_liked_albums.append(x)
                f_liked_albums.remove(i.Name)
                Usuario.liked_albums = f_liked_albums
                i.quitar_like()
            elif desicion==3:
                pass
            #Se selecciona canción del Album
            print('---Seleccione el nombre de la canción a escuchar en este album---')
            for j in i.Tracklist:
                print(j["name"])
            cancion_escuchar=input("---->")
            for j in i.Tracklist:
                if j["name"]==cancion_escuchar:
                    cancion_escogida=Song(j["id"],j["name"],j["duration"],j["link"],0,0)
                    print("Estas escuchando:")
                    print(cancion_escogida.show())
                    #Se despliagan las opciones, dentro de esas escuchar canción
                    print('''[1]---->Dar like
[2]---->Quitar like
[3]---->Escuchar
[4]---->Salir''')
                    desicion = int(input("---->"))
                    if desicion == 1:
                        #Se aplica el like
                        f_liked_songs = []
                        f_liked_songs.append(cancion_escogida.Name)
                        for x in Usuario.liked_songs:
                            if x not in f_liked_songs:
                                f_liked_songs.append(x)
                        Usuario.liked_songs = f_liked_songs
                        cancion_escogida.like()
                        loadUsers.append(Usuario.load())
                        Guardado = open("NewUsers.txt", "w")
                        Guardado.write(str(loadUsers))
                        Guardado.close()
                    elif desicion == 2:
                        #Se aplica el dislike
                        f_liked_songs = []
                        for x in Usuario.liked_songs:
                            if x not in f_liked_songs:
                                f_liked_songs.append(x)
                        f_liked_songs.remove(cancion_escogida.Name)
                        Usuario.liked_songs = f_liked_songs
                        cancion_escogida.quitar_like()
                        loadUsers.append(Usuario.load())
                        Guardado = open("NewUsers.txt", "w")
                        Guardado.write(str(loadUsers))
                        Guardado.close()
                    elif desicion==3:
                        #Se reproduce canción
                        webbrowser.open(cancion_escogida.Link)
                        Usuario.cancion_escuchada(cancion_escogida.Name)
                        Usuario.streams_aniadir()
                        i.streams_aniadir()
                        cancion_escogida.streams_aniadir()
                        loadUsers.append(Usuario.load())
                        Guardado = open("NewUsers.txt", "w")
                        Guardado.write(str(loadUsers))
                        Guardado.close()
                    elif desicion==4:
                        pass
#Se define escuchar_playlist, tiene un programa parecido al anterior
def escuchar_playlist(Usuario):
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
    loadUsers.remove(Usuario.load())
    print("--¿Que Playlist deseas buscar?---")
    playlist_escogido = input("---->")
    for elec in playlist:
        if elec.Name == playlist_escogido:
            print(elec.show())
            print('''[1]---->Dar like
[2]---->Quitar like
[3]---->Salir''')
            desicion = int(input("---->"))
            if desicion == 1:
                f_liked_playlist = []
                f_liked_playlist.append(elec.Name)
                for x in Usuario.liked_playlist:
                    if x not in f_liked_playlist:
                        f_liked_playlist.append(x)
                Usuario.liked_playlist = f_liked_playlist
                elec.like()
            elif desicion == 2:
                f_liked_playlist = []
                for x in Usuario.liked_playlist:
                    if x not in f_liked_playlist:
                        f_liked_playlist.append(x)
                f_liked_playlist.remove(elec.Name)
                Usuario.liked_albums = f_liked_playlist
                elec.quitar_like()
            elif desicion == 3:
                pass
            for id in elec.Tracks:
                for al in albums:
                    for song in al.Tracklist:
                        song_1=Song(song["id"],song["name"],song["duration"],song["link"],0,0)
                        if song_1.Id==id:
                            print (song_1.Name)
            print('---Seleccione la canción a escuchar en este playlist---')
            ele=input("---->")
            for id in elec.Tracks:
                for al in albums:
                    for song in al.Tracklist:
                        song_1=Song(song["id"],song["name"],song["duration"],song["link"],0,0)
                        if song_1.Id==id:
                            if song_1.Name==ele:
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
                                    elec.streams_aniadir()
                                    song_1.streams_aniadir()
                                    loadUsers.append(Usuario.load())
                                    Guardado = open("NewUsers.txt", "w")
                                    Guardado.write(str(loadUsers))
                                    Guardado.close()
                                elif desicion ==4:
                                    pass
#Se define crear_playlist
def crear_playlist(Usuario):
    #Se actualiza playlist
    playlist = []
    x = open("NewPlaylist.txt", "r")
    contenido = x.read()
    contenido_modificado = contenido.replace("'", "\"")
    x.close()
    y = open("NewPlaylist.txt", "w")
    y.write(contenido_modificado)
    y.close()
    final_y = open("NewPlaylist.txt", "r")
    NewUser2 = json.load(final_y)
    final_y.close()
    for i in NewUser2:
        loadUsers.append(i)
    #Se crea playlist y se garda en txt
    print('''---Crea tu playlist---''')
    Play = Playlist(str(uuid.uuid4()), input("Name:"), input("Description:"), Usuario.Name, [],0,0)
    playlist.append(Play.load())
    Guardado = open("NewPlaylist.txt", "w")
    Guardado.write(str(playlist))
    Guardado.close()
#Se define aniadir_canción_playlist
def aniadir_cancion_playlist(Usuario):
    #Se actualiza playlist
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
    #Se busca el playlist del Usuario
    for x in playlist:
        if x["creator"]==Usuario.Name:
            Play = Playlist(x["id"], x["name"],x["description"], Usuario.Name, x["trask"],x["likes"],x["streams"])
            playlist.remove(Play.load())
            # Se selecciona la canción a añadir al playlist
            print('---Seleccione la canción a añadir en este playlist o esribe "salir"---')
            es = input("---->")
            if es=="salir":
                break
                pass
            else:
                for i in albums:
                    for j in i.Tracklist:
                        if j["name"] == es:
                            a = Song(j["id"], j["name"], j["duration"], j["link"], 0,0)
                            (Play.Tracks).append(a.Id)
                            playlist.append(Play.load())
                            #Se guarda el playlist en el txt
                            Guardado = open("NewPlaylist.txt", "w")
                            Guardado.write(str(playlist))
                            Guardado.close()









