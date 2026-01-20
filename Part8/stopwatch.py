# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds+=1
            return
        
        if self.minutes < 59:
            self.minutes+=1
            self.seconds=0
            return
        
        self.minutes=0
        self.seconds=0

    def __str__(self):
        
        if self.minutes<10:
            smin="0"+str(self.minutes)
        else:
            smin=str(self.minutes)
        if self.seconds<10:
            ssec="0"+str(self.seconds)
        else:
            ssec=str(self.seconds)
        return f"{smin}:{ssec}"


if __name__ == '__main__':
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()