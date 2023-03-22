from .bloodoath import BloodOath

# Cults >-----Blood Oaths -------< Followers #

class Cult:

    all = []
    cult_num={}

    def __init__(self, name, city, founding_year, slogan):
        self.name = name
        self.city = city
        self.fy = founding_year
        self.slogan = slogan
        Cult.all.append(self)

        if city in Cult.cult_num.keys():
            Cult.cult_num[city] += 1
                        
        else:
            Cult.cult_num[city] = 1
            
            
    
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
    
    @property
    def average_age(self):

        follower_age_list = [f.age for f in self.followers]
        
        return(float(sum(follower_age_list)/self.cult_population))
    
    @property
    def my_followers_mottos(self):

        for f in self.followers:
            print(f.life_motto)

    @classmethod
    def least_popular(cls):
        
        # list_of_dict = [{c:c.cult_population} for c in cls.all]

        # sorted(list_of_dict, lambda x: x.c)

        # for dict in list_of_dict:
        #     if ___ == list_of_dict[][0]

        for c in cls.all:
            if c.cult_population == min([c.cult_population for c in cls.all]):
                return c.name
    
    @classmethod
    def most_common_location(cls):

        return cls.cult_num
       