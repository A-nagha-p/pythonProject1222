class Time:
    def __init__(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def __add__(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=Time(3,10,5)
o2=Time(4,6,10)
print(o1+o2)