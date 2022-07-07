from Player import Player
from Pitcher import Pitcher
import random

players = [Player("CWS", 2, "Yasmani Grandal", 0.9), Player("CWS", 3, "Jose Abreu", 3.0),
           Player("CWS", 4, "Nick Madrigal", 0.5), Player("CWS", 5, "Yoan Moncada", 0.6),
           Player("CWS", 6, "Tim Anderson", 2.3), Player("CWS", 7, "Eloy Jimenez", 1.3),
           Player("CWS", 8, "Luis Robert", 1.8), Player("CWS", 9, "Adam Eaton", -0.7),
           Player("CWS", "DH", "Andrew Vaughn", "DNP"), Player("MIN", 2, "Ryan Jeffers", 0.4),
           Player("MIN", 3, "Miguel Sano", 0.0), Player("MIN", 4, "Jorge Polanco", 0.3),
           Player("MIN", 5, "Josh Donaldson", 0.6), Player("MIN", 6, "Andrelton Simmons", 0.4),
           Player("MIN", 7, "Jake Cave", 0.3), Player("MIN", 8, "Byron Buxton", 2.1),
           Player("MIN", 9, "Max Kepler", 1.1), Player("MIN", "DH", "Nelson Cruz", 1.9),
           Player("CLE", 2, "Roberto Perez", 0.2), Player("CLE", 3, "Jake Bauers", -0.2),
           Player("CLE", 4, "Cesar Hernandez", 1.8), Player("CLE", 5, "Jose Ramirez", 2.4),
           Player("CLE", 6, "Andres Gimenez", 1.0), Player("CLE", 7, "Eddie Rosario", 1.2),
           Player("CLE", 8, "Ben Gamel", -0.4), Player("CLE", 9, "Josh Naylor", -0.1),
           Player("CLE", "DH", "Franmil Reyes", 0.4), Player("KCR", 2, "Salvador Perez", 2.1),
           Player("KCR", 3, "Carlos Santana", 1.0), Player("KCR", 4, "Nicky Lopez", 0.3),
           Player("KCR", 5, "Hunter Dozier", 0.4), Player("KCR", 6, "AdalbertoMondesi", 1.3),
           Player("KCR", 7, "Andrew Benintendi", -0.1), Player("KCR", 8, "Michael A Taylor", -0.4),
           Player("KCR", 9, "Whit Merrifield", 0.8), Player("KCR", "DH", "Jorge Soler", 0.3),
           Player("DET", 2, "Wilson Ramos", 0.3), Player("DET", 3, "Renato Nunez", 0.7),
           Player("DET", 4, "Jonathon Schoop", 1.3), Player("DET", 5, "Jeimer Candelario", 2.0),
           Player("DET", 6, "Willi Castro", 0.4), Player("DET", 7, "Robbie Grossman", 1.2),
           Player("DET", 8, "JaCoby Jones", 0.5), Player("DET", 9, "Nomar Mazara", -0.2),
           Player("DET", "DH", "Miguel Cabrera", 0.1)]

pitchers = [Pitcher("CWS", "1", "Lucas Giolito", 0.8), Pitcher("CWS", "2", "Dallas Keuchel", 2.1),
            Pitcher("CWS", "3", "Lance Lynn", 2.5), Pitcher("CWS", "4", "Dylan Cease", 0.1),
            Pitcher("CWS", "5", "Michael Kopech", "DNP"), Pitcher("CWS", "CL", "Liam Hendriks", 1.3),
            Pitcher("MIN", "1", "Kenta Maeda", 1.4), Pitcher("MIN", "2", "José Berríos", 0.5),
            Pitcher("MIN", "3", "Michael Pineda", 0.3), Pitcher("MIN", "4", "JA Happ", 1.2),
            Pitcher("MIN", "5", "Matt Shoemaker", 0.6), Pitcher("MIN", "CL", "Alex Colome", 1.0),
            Pitcher("CLE", "1", "Shane Bieber", 3.2), Pitcher("CLE", "2", "Zach Plesac", 2.0),
            Pitcher("CLE", "3", "Aaron Civale", 0.3), Pitcher("CLE", "4", "Triston McKenzie", 0.6),
            Pitcher("CLE", "5", "Logan Allen", 0.1), Pitcher("CLE", "CL", "James Karinchak", 0.6),
            Pitcher("KCR", "1", "Brad Keller", 1.7), Pitcher("KCR", "2", "Mike Minor", 0.1),
            Pitcher("KCR", "3", "Danny Duffy", 0.3), Pitcher("KCR", "4", "Brady Singer", 1.1),
            Pitcher("KCR", "5", "None", "N/A"), Pitcher("KCR", "CL", "Greg Holland", 0.9),
            Pitcher("DET", "1", "Matthew Boyd", -0.6), Pitcher("DET", "2", "Julio Teheran", -0.9),
            Pitcher("DET", "3", "Tarik Skubal", -0.1), Pitcher("DET", "4", "Jose Urena", 0.2),
            Pitcher("DET", "5", "Casey Mize", -0.5), Pitcher("DET", "CL", "Gregory Soto", 0.2)]


def find_pitcher():
    found_player = False
    team = input("Enter the 3-letter abbreviation of the AL Central team your player is on: ")
    type = input("Enter which pitcher you are looking for; use numbers 1-5 for starters or 'CL' for closer: ")
    for pitcher in pitchers:
        if team.upper() == pitcher.team and type.upper() == pitcher.pitcher_type:
            print("Player name: " + pitcher.name + "\n2020 WAR: " + str(pitcher.war))
            found_player = True
    if not found_player:
        print("Invalid input, try again")
        find_pitcher()


def find_player():
    found_player = False
    team = input("Enter the 3-letter abbreviation of the AL Central team your player is on: ")
    type = input("Enter what position you are looking for; use numbers 2-9 or 'DH' for designated hitter: ")
    for player in players:
        if team.upper() == player.team and type.upper() == str(player.position):
            print("Player name: " + player.name + "\n2020 WAR: " + str(player.war))
            found_player = True
    if not found_player:
        print("Invalid input, try again")
        find_player()

def random_player():
    rando = random.randint(0, 1)
    if rando == 0:
        random_pitcher = pitchers[random.randint(0, len(pitchers) - 1)]
        print(random_pitcher.name)
    elif rando == 1:
        random_positional = players[random.randint(0, len(players) - 1)]
        print(random_positional.name)

random_player()

valid_input = False
while not valid_input:
    pitcher = input("Is the player you are looking for a pitcher? Enter 'yes' or 'no': ")
    if pitcher.lower() == "yes":
        valid_input = True
        find_pitcher()
    elif pitcher.lower() == "no":
        valid_input = True
        find_player()
    else:
        print("Invalid input, try again")
