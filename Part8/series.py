# Write your solution here:

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.genres = []
        self.ratings = []
        self.title = title
        self.seasons = seasons
        self.genres = genres

    def rate(self,rating: int):
        self.ratings.append(rating)

    def __str__(self):
        res=""
        res = f"{self.title} ({self.seasons} seasons)\n"
        genre_string=", ".join(self.genres)
        res += f"genres: {genre_string}\n"
        if len(self.ratings)==0:
            res += f"no ratings"
        else:
            l=len(self.ratings)
            s=sum(self.ratings)
            res += f"{l} ratings, average {s/l:.1f} points"
        return res

def minimum_grade(grade: float, series: list):
    res=[]
    for serie in series:
        if len(serie.ratings)>0:
            ar = sum(serie.ratings)/len(serie.ratings)
            if ar>grade:
                res.append(serie)
    return res
    
def includes_genre(genre: str, series: list):
    res=[]
    for serie in series:
        if genre in serie.genres:
            res.append(serie)
    return res



if __name__ == '__main__':
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)