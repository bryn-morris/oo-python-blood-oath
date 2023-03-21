from .bloodoath import BloodOath

# Cults >-----Blood Oaths -------< Followers #

class Cult:

    all = []

    def __init__(self, name, city, founding_year, slogan):
        self.name = name
        self.city = city
        self.fy = founding_year
        self.slogan = slogan
        Cult.all.append(self)
    
    @property
    def oaths(self):
        return [o for o in BloodOath.all if o.cult == self]

    @property
    def followers(self):
        return [o.follower for o in self.oaths]
    
    def recruit_follower(date, self, follower):
        
        BloodOath(date,self, follower)

    @property
    def cult_population(self):
        return len(self.followers)
    
    @classmethod
    def find_by_name(cls, name_string):
        for c in cls.all:
            if c.name == name_string:
                return c
            else:
                return "Cult Not Found!"

        # return [c for c in cls.all if c.name == name_string][0]

    @classmethod
    def find_by_location(cls, location_string):
        
        return [c for c in cls.all if c.city == location_string]
    
    @classmethod
    def find_by_founding_year(cls, founding_year_int):

        return [c for c in cls.all if c.fy == founding_year_int]