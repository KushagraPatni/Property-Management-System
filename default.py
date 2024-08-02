from models import Property
from models import User

u1 = User('Aryan', '1234') 
u2 = User('Kushagra', '2222')
u3  = User('Divyank', '1111')

p1 = Property("Valmiki Bhavan", 30)
p2 = Property("Shankar Bhavan", 50)
p3 = Property("Vyas Bhavan", 55)

u1.register_property(p1)
u2.register_property(p2)
u3.register_property(p3)

users = [u1 , u2 , u3]
properties = [p1, p2, p3]
