from .bloodoath import BloodOath

class Follower:

    all = []
    
    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)


    @property
    def oaths(self):
        # return [o for o in BloodOath.all if o.follower == self]
    
        oath_list = []

        for oath in BloodOath.all:
            if oath.follower == self:
                oath_list.append(oath)

        return oath_list
                

    @property
    def cults(self):
        # [o for o in BloodOath.all if o.follower == self]
        return [o.cult for o in self.oaths]
    
    def join_cult(self, cult_instance):
        
        BloodOath("1984-01-20", cult_instance, self)

    @classmethod
    def of_a_certain_age(cls, age_int):
        
        return [f for f in cls.all if f.age >= age_int]