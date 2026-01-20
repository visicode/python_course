# Write your solution here:
class Clock:
    def __init__(self,hour: int, min: int,sec: int):
        self.hour=hour
        self.min=min
        self.sec=sec

    def set(self, hour: int, min: int):
        self.hour=hour
        self.min=min
        self.sec=0

    def tick(self):
        if self.sec < 59:
            self.sec+=1
            return
        
        if self.min < 59:
            self.min+=1
            self.sec=0
            return
        
        if self.hour<23:
            self.hour+=1
            self.min=0
            self.sec=0
            return
        
        self.hour=0
        self.min=0
        self.sec=0



    def __str__(self):
        
        if self.min<10:
            smin="0"+str(self.min)
        else:
            smin=str(self.min)

        if self.sec<10:
            ssec="0"+str(self.sec)
        else:
            ssec=str(self.sec)

        if self.hour<10:
            shour="0"+str(self.hour)
        else:
            shour=str(self.hour)

        return f"{shour}:{smin}:{ssec}"


if __name__ == '__main__':
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)