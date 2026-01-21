# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        if name!='':
            self.__name=name
        else:
            raise ValueError("Name cannot be empty")
        self.__obs=[]

    def add_observation(self, ob: str):
        if ob!='':
            self.__obs.append(ob)
        else:
            raise ValueError("Observation cannot be empty")
        
    def number_of_observations(self) -> int:
        return len(self.__obs)

    def latest_observation(self) -> str:
        l = len(self.__obs)
        if l == 0:
            return ""
        return self.__obs[l-1]
    
    def __str__(self):
        return f"{self.__name}, {len(self.__obs)} observations"


    