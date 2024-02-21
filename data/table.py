import csv
from pathlib import Path

file_path = Path(__file__).parent / "rangList.csv"

def main():

    players = read_rang_list()
    print(players)
    sorted_players = sort_player(players)
    write_rang_list(sorted_players)

def read_rang_list():
    players = []
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            player = {"Name": row["Name"], "Score": int(row["Score"]), "Time": int(row['Time'])}
            players.append(player)
    return players

def sort_player(players):
    # Sortiranje po Score-u (opadajuće), zatim po Time-u (rastuće) i Name-u (opadajuće)
    sorted_students = sorted(players, key=lambda student: (student["Score"], -student["Time"], student["Name"]), reverse=True)
    return sorted_students

def write_rang_list(players):
    with open(file_path, "w", newline='') as file:  # Preporučljivo koristiti 'newline='''
        writer = csv.DictWriter(file, fieldnames=["Name", "Score", "Time"])
        writer.writeheader()
        writer.writerows(players)        

if __name__ == "__main__":
    main()