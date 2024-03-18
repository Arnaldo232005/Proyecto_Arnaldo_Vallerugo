class Usuario:
    def __init__(self,Id,Name,Correo,UserName,type,streams):
        self.Id=Id
        self.Name=Name
        self.Correo=Correo
        self.UserName=UserName
        self.type=type
        self.streams=streams
    def streams_aniadir(self):
        self.streams=self.streams+1
class Artista(Usuario):
    def __init__(self, Id, Name, Correo, UserName,type,streams,Albums,likes):
        super().__init__(Id,Name,Correo,UserName,type,streams)
        self.Albums=Albums
        self.likes=likes
    def borrar_datos(self):
        self.likes=[]
    def like(self):
        self.likes=self.likes+1
    def quitar_like(self):
        if self.likes>0:
            self.likes=self.likes-1
    def show(self):
        return(f'''
id:{self.Id}
name:{self.Name}
email:{self.Correo}
username:{self.UserName}
type:{self.type}
albums:{self.Albums}
likes:{self.likes}
''')
    def load(self):
        a={"id":self.Id,"name":self.Name,"email":self.Correo,"username":self.UserName,"type":self.type,"albums":self.Albums,"likes":self.likes,"streams":self.streams}
        return (a)
class Oyente(Usuario):
    def __init__(self, Id, Name, Correo, UserName,type,streams,liked_songs,liked_albums,liked_artists,liked_playlist,song_played):
        super().__init__(Id,Name,Correo,UserName,type,streams)
        self.liked_songs=liked_songs
        self.liked_albums=liked_albums
        self.liked_artists=liked_artists
        self.song_played=song_played
        self.liked_playlist=liked_playlist
    def borrar_datos(self):
        self.liked_songs=[]
        self.liked_albums=[]
        self.liked_artists=[]
        self.song_played=[]
    def show(self):
        return (f'''
id:{self.Id}
name:{self.Name}
correo:{self.Correo}
username:{self.UserName}
type:{self.type}
liked_songs:{self.liked_songs}
liked_albums:{self.liked_albums}
liked_artists:{self.liked_artists}
liked_playlist:{self.liked_playlist}
song_played:{self.song_played}
''')
    def load(self):
        a= {"id":self.Id,"name":self.Name,"email":self.Correo,"username":self.UserName,"type":"listener","liked_songs":self.liked_songs,"liked_albums":self.liked_albums,"liked_artists":self.liked_artists,"liked_playlist":self.liked_playlist,"song_played":self.song_played,"streams":self.streams}
        return (a)
    def cancion_escuchada(self,cancion):
        (self.song_played).append(cancion)





