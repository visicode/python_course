# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(ils: list)->list:
    def ors(elem: dict)->int:
        return elem["rating"]
    return sorted(ils, key=ors, reverse=True)

