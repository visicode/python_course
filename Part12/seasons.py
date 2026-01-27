# Write your solution here:
def sort_by_seasons(ils: list)->list:
    def ors(elem: dict)->int:
        return elem["seasons"]
    return sorted(ils, key=ors, reverse=False)

