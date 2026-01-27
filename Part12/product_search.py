# Write your solution here
def search(products: list, criterion: callable)->list:
    ols=[]
    for elem in products:
        if (criterion(elem)):
            ols.append(elem)
    return ols

