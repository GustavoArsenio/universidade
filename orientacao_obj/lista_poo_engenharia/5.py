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

class Rectangle():
    def __init__(self,point_1:Point,point_2:Point):
        (self.lower_x,self.upper_x) = sorted( [point_1.x,point_2.x] )
        (self.lower_y,self.upper_y) = sorted( [point_1.y,point_2.y] )

        self.upper_point = Point(self.upper_x,self.upper_y)
        self.lower_point = Point(self.lower_x,self.lower_y)
        self.point_1     = point_1
        self.point_2     = point_2


def point_in_circle(point:Point, circle: Circle):
    return (point.x - circle.center.x)**2 + (point.y - circle.center.y)**2 <= circle.radius**2

def rect_circle_overlap(rectangle:Rectangle, circle:Circle):
    return  point_in_circle(rectangle.upper_point,circle)  or point_in_circle(rectangle.lower_point,circle)



if __name__ == '__main__':
    my_circle = Circle(2,Point(1,1))
    point_inside_circle1  = Point(1.0 , 1.0)
    point_inside_circle2  = Point(1.5 , 1.0)
    point_outside_circle1 = Point(3.0 , 4.0)
    point_outside_circle2 = Point(3.0 , 5.0)


    rectangle_in          = Rectangle( point_inside_circle1  , point_inside_circle2  )
    rectangle_partial_in  = Rectangle( point_inside_circle1  , point_outside_circle1 )
    rectangle_out         = Rectangle( point_outside_circle1 , point_outside_circle2 )

    print(f" rectangle_in          : { rect_circle_overlap( rectangle_in         , my_circle ) }")
    print(f" rectangle_partial_in  : { rect_circle_overlap( rectangle_partial_in , my_circle ) }")
    print(f" rectangle_out         : { rect_circle_overlap( rectangle_out        , my_circle ) }")