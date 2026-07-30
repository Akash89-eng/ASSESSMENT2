players = {
    "Virat": [600, 400, 2],
    "Rohit": [500, 350, 1],
    "Bumrah": [50, 40, 25],
    "Surya": [300, 180, 0]
}

# Calculate Strike Rate
print("Strike Rate:")
for p, v in players.items():
    sr = (v[0] / v[1]) * 100
    print(p, "=", round(sr, 2))

# Orange Cap Winner
orange = max(players, key=lambda x: players[x][0])
print("\nOrange Cap Winner:", orange)

# Purple Cap Winner
purple = max(players, key=lambda x: players[x][2])
print("Purple Cap Winner:", purple)

# Players with Strike Rate above 150
print("\nPlayers with Strike Rate above 150:")
found = False
for p, v in players.items():
    sr = (v[0] / v[1]) * 100
    if sr > 150:
        print(p, "=", round(sr, 2))
        found = True

if not found:
    print("No player found")

# 
print("\nRanking by Runs:")
rank = sorted(players.items(), key=lambda x: x[1][0], reverse=True)

for i, (p, v) in enumerate(rank, 1):
    print(i, p, "-", v[0], "runs")
