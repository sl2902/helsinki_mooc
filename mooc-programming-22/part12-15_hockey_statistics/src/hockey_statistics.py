# Write your solution here
import json
class Player:
    def __init__(self, name: str, assists: int, 
                goals: int, penalties: int, games: int,
                team: str, country: str):
        self._name = name
        self._assists = assists
        self._goals = goals
        self._penalties = penalties
        self._games = games
        self._team = team
        self._country = country
        self._points = goals + assists
    
    def __str__(self):
        return f"{self._name:21}{self._team:5}{self._goals:>2} +{self._assists:>3} ={self._points:>4}"

class Team(Player):
    def __init__(self):
        self._team = {}
    
    def add_player(self, name: str, assists: int, 
                goals: int, penalties: int, games: int, 
                team: str, country: str):
        if name not in self._team:
            self._team[name] = Player(name, assists, goals, penalties, 
                                        games, team, country)
    
    def all_teams(self):
        return self._team
    
    def list_teams(self):
        return sorted(set(self._team[player]._team for player in self.all_teams()))
    
    def list_countries(self):
        return sorted(set(self._team[player]._country for player in self.all_teams()))
    
    def by_team(self, team: str):
        players = [self._team[player] for player in self.all_teams() if self._team[player]._team == team]
        return sorted(players, key=lambda x: (x._assists + x._goals), reverse=True)
    
    def by_country(self, country: str):
        players = [self._team[player] for player in self.all_teams() if self._team[player]._country == country]
        return sorted(players, key=lambda x: (x._assists + x._goals), reverse=True)
    
    def by_most_points(self, top: int):
        players = [self._team[player] for player in self.all_teams()]
        return sorted(players, key=lambda x: (x._assists + x._goals, x._goals), reverse=True)[:top]
    
    def by_most_goals(self, top: int):
        players = [self._team[player] for player in self.all_teams()]
        return sorted(players, key=lambda x: (-x._goals, x._games))[:top]
    
class HockeyApp:
    def __init__(self):
        self._hockey_stats = Team()
        # self._data = player_data
        # self.add_player()
    
    def read_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for player in data:
                yield player
    
    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    def add_player(self, filename: str):
        for player in self.read_file(filename):
            self._hockey_stats.add_player(player['name'], player['assists'],
                                player['goals'], player['penalties'], player['games'], 
                                player['team'], player['nationality'])
    
    def get_player(self, name: str):
        return self._hockey_stats._team.get(name, None)
    
    def all_teams(self):
        return self._hockey_stats.all_teams()
    
    def search_player(self):
        try:
            player = input("name: ")
            print()
            print(self.get_player(player))
        except:
            print("player doesn't exist")
    
    def list_teams(self):
        for team in self._hockey_stats.list_teams():
            print(team)
    
    def list_countries(self):
        for country in self._hockey_stats.list_countries():
            print(country)
    
    def by_team(self):
        try:
            team = input("team: ")
            print()
            for player in self._hockey_stats.by_team(team):
                print(player)
        except:
            print("team doesn't exist")
    
    def by_country(self):
        try:
            country = input("country: ")
            print()
            for player in self._hockey_stats.by_country(country):
                print(player)
        except:
            print("country doesn't exist")
    
    def by_most_points(self):
        try:
            n = int(input("how many: "))
            print()
            for player in self._hockey_stats.by_most_points(n):
                print(player)
        except:
            print("invalid input")
    
    def by_most_goals(self):
        try:
            n = int(input("how many: "))
            print()
            for player in self._hockey_stats.by_most_goals(n):
                print(player)
        except:
            print("invalid input")

    
    def execute(self):
        filename = input("filename: ")
        # try:
        self.add_player(filename)
        # except:
        #     raise ValueError("invalid file")
        print(f'read the data of {len(self.all_teams())} players')
        print()
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_player()
            elif command == "2":
                self.list_teams()
            elif command == "3":
                self.list_countries()
            elif command == "4":
                self.by_team()
            elif command == "5":
                self.by_country()
            elif command == "6":
                self.by_most_points()
            elif command == "7":
                self.by_most_goals()
            else:
                self.help()


class FileHandler:
    def __init__(self, filename: str):
        self._filename = filename
    
    def read_file(self):
        with open(self._filename, 'r') as f:
            data = json.load(f)
            for player in data:
                yield player

# filename = 'partial.json'
# player_data = FileHandler(filename)
app = HockeyApp()
app.execute()
# app._hockey_stats.test()
# for player in app.all_teams():
#     print(app.all_teams()[player])