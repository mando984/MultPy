"""
table.py update, write and read csv file
"""

import csv
from pathlib import Path

file_path = Path(__file__).parent / "rankList.csv"


def main():


    players = read_rank_list()
    print(players)
    sorted_players = sort_player(players)
    write_rank_list(sorted_players)


def read_rank_list():
    players = []
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            player = {"Name": row["Name"], "Score": int(row["Score"]), "Time": int(row['Time'])}
            players.append(player)
    return players


def sort_player(players):
    # Sort by Score (descending), then by Time (ascending), and Name (descending).
    sorted_students = sorted(players, key=lambda student: (student["Score"], -student["Time"], student["Name"]), reverse=True)
    return sorted_students


def write_rank_list(players):
    with open(file_path, "w", newline='') as file:  # It is recommended to use 'newline=''
        writer = csv.DictWriter(file, fieldnames=["Name", "Score", "Time"])
        writer.writeheader()
        writer.writerows(players)        


if __name__ == "__main__":
    main()