#Se importan los módulos requeridos
from Funciones3 import *
from user_api import*
from Funciones2 import *
#Se abren los distintos json usando "encoding="utf-8", para evitar el error cuando aparece un caracter como
#la "ñ" que el programa no lee
x = open("users.json", "r",encoding="utf-8")
base_de_datos =json.load(x)
x.close()
x_albums = open("albums.json", "r",encoding="utf-8")
base_de_datos_albums = json.load(x_albums)
x_albums.close()
x_playlist = open("playlists.json", "r",encoding="utf-8")
base_de_datos_playlist = json.load(x_playlist)
x_playlist.close()
#Se usa el api para descargar los json
api()
#Se descarga los json y los txt
downloadUser(base_de_datos)
downloadNewUser(NewUser2)
downloadAlbums(base_de_datos_albums)
downloadNewAlbums(NewUser2)
downloadPlaylist(base_de_datos_playlist )
#Se define main para hacer el menu
def main():
    #Se abre el ciclo y llamamos la función introduccion
    ciclo=True
    e=introduccion()
    while ciclo==True:
        #Se abre el menu
        print('''Bienvenidos a Metrofy, seleccione una opción
[1]---->Gestión de Perfil
[2]---->Gestión de Música
[3]---->Ranking(Estadísticas)
[4]---->Salir''')
        res = int(input("---->"))
        if res == 1:
            print('''Has entrado a la Gestión de Perfil
[1]---->Buscar usuarios
[2]---->Editar usuario
[3]---->Borrar datos
             ''')
            resp = int(input("---->"))
            # Se llama la funcion de la opción seleccionada
            if resp == 1:
                print(SearchUser(artists,listen,e))
            elif resp==2:
                editarUsuario(e)
            elif resp==3:
                if e.type=="listener":
                    e.borrar_datos()
                elif e.type=="musician":
                    e.borrar_datos()
        elif res==2:
            if e.type=="listener":
                print('''Has entrado a la Gestión de Música
[1]---->Buscar Album
[2]---->Buscar Playlist
[3]---->Crear Playlist
[4]---->Añadir canciones a tu Playlist
[5]---->Escuchar tu playlist 
''')
                ef=int(input("---->"))
                #Se llama la funcion de la opción seleccionada
                if ef==1:
                    escuchar_musica(e)
                elif ef==2:
                    escuchar_playlist(e)
                elif ef==3:
                    crear_playlist(e)
                elif ef==4:
                    aniadir_cancion_playlist(e)
                elif ef==5:
                    mostrar_tu_playlist(e)
            elif e.type=="musician":
                print('''Has entrado a la Gestión de Música
[1]---->Crear Album
[2]---->Añadir canción a Album
                         ''')
                resp=int(input("---->"))
                # Se llama la funcion de la opción seleccionada
                if resp==1:
                    createAlbums(e)
                elif resp==2:
                    aniadir_cancion(e)
        elif res==3:
            #Se crean los respectivos ranking
            #Se recolectan los streams en una listas para ser ordenados y emperejados con sus respectivos objetos
            #para luego ser imprimidos en orden
            def ranking_albums():
                r_albums = []
                top = []
                for i in albums:
                    top.append(i.streams)
                top.sort()
                top.reverse()
                for i in top:
                    for j in albums:
                        if j.streams == i:
                            r_albums.append(j.Name)
                for i in range(0, 5):
                    print({r_albums[i]})

            def ranking_playlist():
                r_playlist = []
                top = []
                for i in playlist:
                    top.append(i.streams)
                top.sort()
                top.reverse()
                for i in top:
                    for j in playlist:
                        if j.streams == i:
                            r_playlist.append(j.Name)
                for i in range(0, 5):
                    print(r_playlist[i])

            def ranking_artistas():
                r_artistas = []
                top = []
                for i in artists:
                    top.append(i.streams)
                top.sort()
                top.reverse()
                for i in top:
                    for j in artists:
                        if j.streams == i:
                            r_artistas.append(j.Name)
                for i in range(0, 5):
                    print(r_artistas[i])

            def ranking_usuario():
                r_usuario = []
                top = []
                for i in listen:
                    top.append(i.streams)
                top.sort()
                top.reverse()
                for i in top:
                    for j in listen:
                        if j.streams == i:
                            r_usuario.append(j.Name)
                for i in range(0, 5):
                    print(r_usuario[i])

            def ranking_song():
                r_song = []
                can=[]
                top = []
                for i in albums:
                    for j in i.Tracklist:
                        song=(Song(j["id"],j["name"],j["duration"],j["link"],0,0))
                        top.append(song.streams)
                        can.append(song)
                top.sort()
                top.reverse()
                for i in top:
                    for j in can:
                        if j.streams == i:
                              r_song.append(j.Name)
                for i in range(0, 5):
                    print(r_song[i])
            print('''---Has entrado a Ranking---
[1]---->Ranking Playlist
[2]---->Ranking Oyente
[3]---->Ranking Artistas
[4]---->Ranking Albums
[5]---->Ranking Canciones''')
            resp=int(input("---->"))
            if resp==1:
                print(ranking_playlist())
            if resp==2:
                print(ranking_usuario())
            if resp==3:
                print(ranking_artistas())
            if resp==4:
                print(ranking_albums())
            if resp==5:
                print(ranking_song())
        elif res==4:
            #Se cierra el ciclo
            ciclo=False
main()
