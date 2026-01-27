class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here

def most_goals(ils: list)->str:
    return max(ils,key= lambda item : item.goals).name

def most_points(ils: list)->tuple:
    def points (ibp: BallPlayer)->int:
        return ibp.goals+ibp.passes
    sls = max (ils, key=points)
    return (sls.name, sls.number)

def least_minutes(ils: list)->BallPlayer:
    return min(ils,key= lambda item: item.minutes)

