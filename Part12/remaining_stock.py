# Write your solution here:
def sort_by_remaining_stock(pr: list)->list:
    def ors(t: tuple)->int:
        return t[2]
    
    return sorted(pr, key=ors,reverse=False)
    
