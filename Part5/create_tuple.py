# Write your solution here
def create_tuple(x: int, y: int, z: int) -> tuple:
    ls = [x,y,z]
    return((min(ls),max(ls),sum(ls)))

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

