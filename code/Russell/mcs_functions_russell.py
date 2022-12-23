import cmd, textwrap, sys, math, random, pyreadline

#### TO-DO LIST ####
# SEPARATE DISTANCE FROM TRAVEL FUNCTION
# UPDATE PLAYER FUNCTION FROM TRAVEL FUNCTION RETURN VALUE
# DRAW THE REST OF THE FUCKING OWL


# Create Constant Variables #
A1 = 'A1'
A2 = 'A2'
A3 = 'A3'
A4 = 'A4'
B1 = 'B1'
B2 = 'B2'
B3 = 'B3'
B4 = 'B4'
C1 = 'C1'
C2 = 'C2'
C3 = 'C3'
C4 = 'C4'
D1 = 'D1'
D2 = 'D2'
D3 = 'D3'
D4 = 'D4'
name = 'name'
coord = 'coord'
POIs = 'POIs'
explored = 'explored'
desc = 'desc'
looted = 'looted'
items = 'items'
is_weapon = 'is_weapon'
is_food = 'is_food'
is_drink = 'is_drink'
is_ally = 'is_ally'
can_take = 'can_take'
screen_width = 80

# Define Locations, POIs, Items, etc 

world_locations = {
    A1: {
        coord: (1, 1),
        POIs: [],
        explored: 0},
    A2: {
        coord: (1, 2),
        POIs: [],
        explored: 0},
    A3: {
        coord: (1, 3),
        POIs: [],
        explored: 0},
    A4: {
        coord: (1, 4),
        POIs: [],
        explored: 0},
    
    B1: {
        coord: (2, 1),
        POIs: [],
        explored: 0},
    B2: {
        coord: (2, 2),
        POIs: [],
        explored: 0},
    B3: {
        coord: (2, 3),
        POIs: [],
        explored: 0},
    B4: {
        coord: (2, 4),
        POIs: [],
        explored: 0},
    
    C1: {
        coord: (3, 1),
        POIs: [],
        explored: 0},
    C2: {
        coord: (3, 2),
        POIs: [],
        explored: 0},
    C3: {
        coord: (3, 3),
        POIs: [],
        explored: 0},
    C4: {
        coord: (3, 4),
        POIs: [],
        explored: 0},

    D1: {
        coord: (4, 1),
        POIs: [],
        explored: 0},
    D2: {
        coord: (4, 2),
        POIs: [],
        explored: 0},
    D3: {
        coord: (4, 3),
        POIs: [],
        explored: 0},
    D4: {
        coord: (4, 4),
        POIs: [],
        explored: 0}
        
}


location_pois = {
    'Hospital': {
        desc: 'It is a hospital',
        looted: 0,
        items: []},

    'Gas Station': {
        desc: 'It is a gas station',
        looted: 0,
        items: []},

    'School': {
        desc: 'It is a school',
        looted: 0,
        items: []},

    'Police Station': {
        desc: 'It is a police station',
        looted: 0,
        items: []},

    'Church': {
        desc: 'It is a church',
        looted: 0,
        items: []},

    'House': {
        desc: 'It is a house',
        looted: 0,
        items: []},
}


world_items = {
    'Gun': {
        name: 'a gun',
        desc: 'It is a gun',
        can_take: True,
        is_weapon: True,},

    'Taco': {
        name: 'a taco',
        desc: 'It is a taco',
        can_take: True,
        is_food: True},

    'Soda': {
        name: 'a soda',
        desc: 'It is a soda',
        can_take: True,
        is_drink: True},

    'Survivor': {
        name: 'a survivor',
        desc: 'It is a survivor',
        can_take: True,
        is_ally: True}
}

# Set player starting position and set inventory to empty

# player_location = A1
# inventory = []

# Define Functions

# Sets player location to new location
# Quick Maffs for finding distance between current and next location
def travel(current_location, destination):

    if current_location in world_locations and destination in world_locations:
        x1, y1 = world_locations[current_location]['coord']
        x2, y2 = world_locations[destination]['coord']
    
        distance = math.dist([x1, y1], [x2, y2])        
        distance= (round(distance, 2))     ## SHOULD THIS ALSO ACCOUNT FOR TIME OR IS THAT A SEPARATE FUNCTION??
        travel_time = round(distance / 2, 2)

        print(f'You travel {distance} miles to {destination}, which takes {travel_time} hours')

        current_location = destination
        return distance, current_location
    
    else:
        print("Please enter a valid grid location ")

# Once in a grid space, this function allows player to discover POIs for scavenging
def explore(quadrant, level): # 

    for i in range(level):
        discovered = random.choice(list(location_pois.items()))
        world_locations[quadrant][POIs] += discovered  # HOW DO I LIMIT "POIs" TO 3??
        world_locations[quadrant][explored] += 1       # MAYBE WHEN CALLING THE FUNCTION??
        if world_locations[quadrant][explored] > 3:
            world_locations[quadrant][explored] = 3

# Once in a specific POI, allows player to scavenge
# Scavenging can be done all at once (level 3), or a little at a time (one level 2, two level 1, or similar)
def scavenge(location, level): 

    item_count = 0
    items_found = []
    # should randomly select item and incrememt 'looted' level
    for i in range(level):
        item_count += 1
        found = random.choice(list(world_items.items())) # there should be more to this...
        items_found += found                            # maybe skewing the 'randomness' a bit...
        # inventory.append(found)
        location_pois[location][looted] +=1              # not every search should return an item
        if location_pois[location][looted] > 3:
            location_pois[location][looted] = 3
    print(f"You found {item_count} items")
    print(f"Items found: {items_found}")

    # if 0 < location_pois[location][looted] < 3:
    #     print(f"You have looted this POI {looted} times")
    # elif location_pois[location][looted] == 0:
    #     print("You have not yet looted this location")            ## SHOULD THIS BE DONE OUTSIDE OF THE FUNCTION??
    # elif location_pois[location][looted] >= 3:
    #     print("There's nothing left to scavenge")
    
    # if location_pois[location][looted] < 3:
    #     location_pois[location][looted] += 1

def display_location(location):
    # Print the room name.
    statement = 'Your current grid location is '
    
    print(location)
    # print(statement + location)
    # print('#' * len(statement + location))

    # Print the 
    print(f"POIs discovered - {world_locations[location][POIs]}")
    print(f"Explored level: {world_locations[location][explored]}")

def display_poi(poi):
    # Print the room name.
    print(poi)
    print('#' * len(poi))

    # Print the POI's description (using textwrap.wrap())
    print(location_pois[poi], screen_width)

    # Print scavenged level.
    print(f"Scavenged level: {location_pois[poi][looted]}")



player_location = A1
while True:
    
    display_location(player_location)
    response = input("travel where?")
    if response == 'quit':
        break
    if response in [A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4]:
        player_location = travel(player_location, response)
        print(response)
    else:
        print("invalid entry")







# while True:

#     place = input("Pick a quadrant to explore ")
#     level = int(input("How thoroughly would you like to explore? "))
#     explore(world_locations[place], level)
#     print(world_locations[place])
#     x = input("Quit? ")
#     if x == "Y":
#         break

# explore(A1, 2)
# print(world_locations[A1][POIs])
# print(world_locations[A1][explored])
# scavenge('Hospital', 3)
# print(location_pois['Hospital'][looted])
# print(location_pois['Hospital'][items])
# distance, current_location = travel('A1', 'A2')
# print(distance, current_location)
