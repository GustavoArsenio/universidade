class Point():
    """
        Clase Point, recebe um tuple x,y
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f" X: {self.x} | Y: {self.y}"

class Circle():
    """"
        Classe Circle, recebe Center, Radius 
    """
    def __init__(self,radius, center:Point(int,int) =  Point(0,0)):
        super().__init__()
        self.center=center
        self.radius=radius
    
    def __str__(self):
        return  f" Center: {self.center} | Radius {self.radius} "