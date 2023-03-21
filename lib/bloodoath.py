# Cults >-----Blood Oaths -------< Followers #

class BloodOath:

    all = []
    
    def __init__(self, initiation_date, cult, follower_instance):
        self.initiation_date = initiation_date
        self.cult = cult
        self.follower = follower_instance
        BloodOath.all.append(self)

