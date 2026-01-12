# Write your solution here
def find_movies (db: list,s: str)->list:
    result=[]
    for ls in db:
        if ls["name"].lower().find(s.lower())!=-1:
            result.append(ls)
    return result

if __name__ == '__main__':
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)