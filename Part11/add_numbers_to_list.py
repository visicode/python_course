# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(ils : list):
    if len(ils)%5!=0:
        ils.append(ils[-1]+1)
        add_numbers_to_list(ils)

