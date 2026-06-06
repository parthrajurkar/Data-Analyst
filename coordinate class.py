class Point:    
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
        
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
        
p1=Point(0,0)
p2=Point(-2,-1)

print(p1.euclidean_distance(p2))

print(p2.distance_from_origin())