import json

f1=open("data/dog_bites_updated.csv", "r")
lines = f1.readlines()

year_list = []
year_list = lines[0].split(",")[1:]

dictionary = {}

bronx = lines[1].split(",")[1:]
brooklyn = lines[2].split(",")[1:]
manhattan = lines[3].split(",")[1:]
queens = lines[4].split(",")[1:]
staten_island = lines[5].split(",")[1:]

bronx_dict = {}
brooklyn_dict = {}
manhattan_dict = {}
queens_dict = {}
staten_island_dict = {}

for num in range(0,9):
    bronx_dict[2015+num] = bronx[num]
    brooklyn_dict[2015+num] = brooklyn[num]
    manhattan_dict[2015+num] = manhattan[num]
    queens_dict[2015+num] = queens[num]
    staten_island_dict[2015+num] = staten_island[num]

dictionary = {
    "Bronx": bronx_dict,
    "Brooklyn" : brooklyn_dict,
    "Manhattan" : manhattan_dict,
    "Queens" : queens_dict,
    "Staten Island" : staten_island_dict
}

f1.close()

f2 = open("data_bite.json", "w")
json.dump(dictionary,f2, indent = 4)

f2.close()