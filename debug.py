import ipdb
from lib import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
# c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )

# bo1 = BloodOath( '2019-09-16', f1, c1 )


# c1.followers => ???
# f1.cults => ???

c1 = Cult("Little Stinkers", "Adam's Living Room", 2023, "My Code isn't working!!!")
c2 = Cult("Watchtower Society", "New York", 1888, "To fear God is not to")
c3 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c4 = Cult( 'Heavens Gate2: Electric Boogaloo', 'San Diego', 1974, 'Not Like the Other One' )

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( "Bryn", 27, "May I ask a question?")
f3 = Follower( "Kimberly", 31, "Just Do it")

b1 = BloodOath( "1999-10-31",c1,f2 )
b2 = BloodOath( "2004-04-27",c1,f3 )
b3 = BloodOath( "1887-05-30",c2,f1 )
b4 = BloodOath( "1887-05-30",c2,f3 )
b5 = BloodOath( "1890-05-30",c3,f1 )
b6 = BloodOath( "1888-05-30",c4,f1 )
b7 = BloodOath( "1888-05-30",c4,f3 )
b8 = BloodOath( "1888-05-30",c4,f2 )
b9 = BloodOath( "1889-05-30",c3,f3 )


print( "Mwahahaha!" )
ipdb.set_trace()