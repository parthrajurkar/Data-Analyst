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
    
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
        
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)

#Point Class Object created        
p1=Point(0,0)
p2=Point(-2,-1)

print(p1.euclidean_distance(p2))

print(p2.distance_from_origin())

#Line class object created

L1=Line(1,2,3)
print(L1)