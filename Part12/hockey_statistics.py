# Write your solution here
import json

class Player:
    def __init__(self ,name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name=name
        self.nationality=nationality
        self.assists=assists
        self.goals=goals
        self.penalties=penalties
        self.team=team
        self.games=games
    def __str__(self):
        return f"{self.name:<21}{self.team}{self.goals:>4} + {self.assists:>2} = {self.goals+self.assists:>3}"

def print_help():
    print(""" commands:
    0 quit
    1 search for player
    2 teams
    3 countries
    4 players in team
    5 players from country
    6 most points
    7 most goals""")

def find_player(pn: str)->Player:
    if pn=="":
        raise ValueError("Empty string search error")
    for pl in players:
        if pl.name == pn:
            return pl
    return None

def all_teams()->list:
    res=[]
    for pl in players:
        if pl.team not in res:
            res.append(pl.team)
    return sorted(res)

def all_country()->list:
    res=[]
    for pl in players:
        if pl.nationality not in res:
            res.append(pl.nationality)
    return sorted(res)

def player_point(pl: Player)->int:
    return pl.assists+pl.goals

def player_p_g(pl: Player)->tuple:
    return (pl.assists+pl.goals,pl.goals)

def player_g_gml(pl: Player)->tuple:
    return (pl.goals,-pl.games)

def find_team_player(tm: str)->list:
    res=[]
    for pl in players:
        if pl.team == tm:
            res.append(pl)
    return sorted(res,key=player_point, reverse=True)

def find_country_player(co: str)->list:
    res=[]
    for pl in players:
        if pl.nationality == co:
            res.append(pl)
    return sorted(res,key=player_point, reverse=True)

def most_points_players()->list:
    res=[]
    for pl in players:
        res.append(pl)
    return sorted(res,key=player_p_g, reverse=True)

def most_goals_players()->list:
    res=[]
    for pl in players:
        res.append(pl)
    return sorted(res,key=player_g_gml, reverse=True)

players=[]

#fn ="partial.json"
fn = input("file name: ")

with open(fn) as my_file:
    data = my_file.read()
loaded_data = json.loads(data)

for pl in loaded_data:
    players.append(Player(pl["name"],pl["nationality"],pl["assists"],pl["goals"],pl["penalties"],pl["team"],pl["games"]))

print (f"read the data of {len(players)} players")
print()
print_help()

while True:
    command = input("command: ")
    if command == "0":
        break
    elif command == "1":
        name = input("name: ")
        player = find_player(name)
        print (player)
    elif command == "2": #team names in alphabetical order
        teams = all_teams()
        for team in teams:
            print(team)
    elif command == "3": #countries in alphabetical order
        cs = all_country()
        for co in cs:
            print(co)
    elif command == "4": #list players in a specific team in the order of points scored, from highest to lowest. Points equals goals + assists
        team = input("team: ")
        pls = find_team_player(team)
        for pl in pls:
            print(pl)
    elif command == "5":
        country = input("country: ")
        pls = find_country_player(country)
        for pl in pls:
            print(pl)
    elif command == "6": #list of n players who've scored the most points. if two players have the same score, whoever has scored the higher number of goals comes first
        num = int(input("how many: "))
        pls = most_points_players()
        for i in range(num):
            print(pls[i])
    elif command == "7": #list of n players who've scored the most goals. if two players have the same number of goals, whoever has played the lower number of games comes first
        num = int(input("how many: "))
        pls = most_goals_players()
        for i in range(num):
            print(pls[i])
    else:
        print ("unknown command")
        print_help()
    print()


#{'name': 'Travis Zajac', 
# 'nationality': 'CAN', 
# 'assists': 16, 
# 'goals': 9, 
# 'penalties': 28, 
# 'team': 'NJD', 
# 'games': 69}
#Travis Zajac         NJD   9 + 16 =  25
#123456789012345678901234567890123456789
