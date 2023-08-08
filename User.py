class User():
    def __init__(self , name, id) -> None:
        self.name = name
        self.online = False
        self.id = id

    def __str__(self):
        return self.name + ' ' + self.secname 
    
    def toJSON(self):
        return    {
            "id" : self.id,
            "name" : self.name,
            "online" : self.online
        }
        
