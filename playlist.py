class Playlist:
    def __init__(self,Id,Name,Description,Creator,Tracks,Likes,streams):
        self.Id=Id
        self.Name=Name
        self.Description=Description
        self.Creator=Creator
        self.Tracks=Tracks
        self.Likes=Likes
        self.streams=streams
    def show(self):
        return (f'''Id:{self.Id}
Name:{self.Name}
Description:{self.Description}
Creator:{self.Creator}
Tracks:{self.Tracks}
''')
    def load(self):
        a = {"id": self.Id, "name": self.Name, "description": self.Description, "creator": self.Creator, "trask": self.Tracks,"likes":self.Likes,"streams":self.streams}
        return (a)
    def like(self):
        self.Likes=self.Likes+1
    def quitar_like(self):
        if self.Likes>0:
            self.Likes=self.Likes-1
    def streams_aniadir(self):
        self.streams=self.streams+1
