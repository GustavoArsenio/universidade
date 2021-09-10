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
    def __init__(self,radius, center:Point =  Point(0,0)):
        super().__init__()
        self.center=center
        self.radius=radius
    
    def __str__(self):
        return  f" Center: {self.center} | Radius {self.radius} "

def point_in_circle(point:Point, circle: Circle):
    return (point.x - circle.center.x)**2 + (point.y - circle.center.y)**2 <= circle.radius**2

if __name__ == '__main__':
    my_circle = Circle(2,Point(1,1))
    point_inside_circle  = Point(1,1)
    point_outside_circle = Point(3,1)
    print(f"point_in_circle:  {point_in_circle(point_inside_circle,my_circle)}")
    print(f"point_out_circle: {point_in_circle(point_outside_circle,my_circle)}")

