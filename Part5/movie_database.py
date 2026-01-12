# Write your solution here
def add_movie(db :list,name: str, dir: str, year: int, l: int)->None:
    d={}
    d["name"]=name
    d["director"]=dir
    d["year"]=year
    d["runtime"]=l
    db.append(d)

if __name__ == '__main__':
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)