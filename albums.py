class Album:
    def __init__(self,Id,Name,Description,Cover,Published,Genre,Artists,Tracklist,Likes,streams):
        self.Id=Id
        self.Name=Name
        self.Description=Description
        self.Cover=Cover
        self.Published=Published
        self.Genre=Genre
        self.Artists=Artists
        self.Tracklist=Tracklist
        self.Likes=Likes
        self.streams=streams
    def show(self):
        return print(f'''Id:{self.Id}
Name:{self.Name}
Description:{self.Description}
Cover:{self.Cover}
Published:{self.Published}
Genre:{self.Genre}
Artists:{self.Artists}
Tracklist:{self.Tracklist}
Likes:{self.Likes}
''')
    def load(self):
        a={"id":self.Id,"name":self.Name,"description":self.Description,"cover":self.Cover,"published":self.Published,"genre":self.Genre,"artists":self.Artists, "tracklist":self.Tracklist, "likes":self.Likes,"streams":self.streams}
        return(a)
    def like(self):
        self.Likes=self.Likes+1
    def quitar_like(self):
        if self.Likes>0:
            self.Likes=self.Likes-1
    def streams_aniadir(self):
        self.streams=self.streams+1
