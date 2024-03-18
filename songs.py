class Song:
    def __init__(self,Id,Name,Duration,Link,Likes,streams):
        self.Id=Id
        self.Name=Name
        self.Duration=Duration
        self.Link=Link
        self.Likes=Likes
        self.streams=streams
    def show(self):
        return (f'''Id:{self.Id}
Name:{self.Name}
Duration:{self.Duration}
Link:{self.Link}
Likes:{self.Likes}''')
    def load(self):
        a={"id":self.Id,"name":self.Name,"duration":self.Duration,"link":self.Link,"likes":self.Likes,"streams":self.streams}
        return (a)
    def like(self):
        self.Likes=self.Likes+1
    def quitar_like(self):
        if self.Likes>0:
            self.Likes=self.Likes-1
    def streams_aniadir(self):
        self.streams=self.streams+1
