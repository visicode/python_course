# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self,wn :int, nums: list):
        self._wn=wn
        self._nums=nums

    def number_of_hits(self, ils: list)->int:
        return len([num for num in ils if num in self._nums])

    def hits_in_place(self, ils: list)->list:
        return [ils[i] if ils[i] in self._nums else -1 for i in range(7)]

