import cmd, textwrap, sys, math, random, pyreadline3

#### TO-DO LIST ####
# SEPARATE DISTANCE FROM TRAVEL FUNCTION
# UPDATE PLAYER FUNCTION FROM TRAVEL FUNCTION RETURN VALUE
# DRAW THE REST OF THE FUCKING OWL

opening_statement = '''The world has ended...
\n...
\n...
\n...


In the wake of the COVID-19 pandemic...
\nThe people of the United States had grown tired of living their lives in fear of the invisible...
\n
\n...
\n...
Some other stuff that references... 
\nthe fractured nature of our current reality...
\nand explains the spread of the zombie virus...ZMB-13
\n...
\n...
Some descirption of...
\nyour escape from whatever city you escaped from...
\nand how you made your way to the base in the woods
\n...
\n...
The Old World is dead...
Welcome to the New World, Zed-bait...
'''

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



##########################################



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
        POIs: [{'Gas Station': {
        desc: 'It is a gas station',
        looted: 0,
        items: []}}],
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

player_location = A1
inventory = []



################################################



# Define Basic Functions



def display_inventory():

    if len(inventory) == 0:
        print('You have nothing and you are alone in a hostile world')
        return

    print('Inventory: \n')
    for item in inventory:
        print(item)




def display_location(location):
    # Show grid location
    
    print(f'Your current grid location is {location}')

    # Show grid location info
    print(f"POIs discovered - {world_locations[location][POIs]}")
    print(f"Explored level: {world_locations[location][explored]}")



def display_poi(poi):
    # Show POI name
    print(poi)
    print('#' * len(poi))

    # Print the POI's description
    print(location_pois[poi])

    # Print scavenged level.
    print(f"Scavenged level: {location_pois[poi][looted]}")



def explore(quadrant, level): # 
# Once inside a grid location, this function allows player to discover POIs for scavenging

    for i in range(level):
        discovered = random.choice(list(location_pois.items()))
        world_locations[quadrant][POIs] += discovered  # HOW DO I LIMIT "POIs" TO 3??
        world_locations[quadrant][explored] += 1       # MAYBE WHEN CALLING THE FUNCTION??
        if world_locations[quadrant][explored] > 3:
            world_locations[quadrant][explored] = 3



def scavenge(location, level): 
# Once in a specific POI, allows player to scavenge
# Scavenging can be done all at once (level 3), or a little at a time (one level 2, two level 1, or similar)

    item_count = 0
    items_found = []
    # should randomly select item and incrememt 'looted' level
    
    while item_count < 3:

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
    else:
        print("Nothing left to scavenge, pick a different POI ")



def travel(current_location, destination):
# Sets player location to new location

    if current_location in world_locations and destination in world_locations and destination != current_location:
    
        current_location = destination
        return current_location
    
    elif destination == current_location:
        print("You are already at that grid location ")

    else:
        print("Please enter a valid grid location ")



def travel_time(player_location, destination):
# Quick Maffs for finding distance between current and next location
    x1, y1 = world_locations[player_location]['coord']
    x2, y2 = world_locations[destination]['coord']
  
    distance = math.dist([x1, y1], [x2, y2])        
    distance= (round(distance, 2))     ## SHOULD THIS ALSO ACCOUNT FOR TIME OR IS THAT A SEPARATE FUNCTION??
    travel_time = round(distance / 2, 2)
    
    
    return travel_time



class GamePrompt(cmd.Cmd):


    # DEFAULT FUNCTION

    def default(self, arg):
        # What cmd will default to when given invalid input
        print("That is not a valid input")
        print("Please try something else or type 'help' for a list of commands")



    ### DO_ FUNCTIONS - will run when player types command that follows 'do_' (ex: 'help')
    

    def do_inventory(self, arg):
        display_inventory()



    def do_location(self, arg):
        # Displays current player location
        display_location(player_location)



    def do_quit(self, arg):
        # Quits game
        return True



    def do_scavenge(self, arg):
        # Allows player to set scavenge 'level' for a given POI
        global player_location
        print(f'This grid location has the following POIs: {world_locations[player_location][POIs]}')
        poi_to_scav = input('Which POI would you like to scavenge? ')
        scav_level = int(input('How thoroughly would you like to scavenge? (1-3) '))
        scavenge(poi_to_scav, scav_level)



    def do_travel(self, arg):
        # Moves player to new grid location
        global player_location
        destination = input("Enter desired grid location ")
        tt= travel_time(player_location, destination)
        player_location = travel(player_location, destination)        
        print(f'You travel for {tt} hours to reach grid location {destination} ')
        





    ### HELP_ FUNCTIONS - will run when players types 'help' followed by a valid help command (ex: 'help travel')
    
    def help_combat(self):
        print('Yeah, that is not a thing yet...maybe in the update ')



    def help_map(self):
        print('Draw one, ya lazy ')



    def help_travel(self):
        print('You can travel between any two grid points by typing "travel"')
        print('You will then be prompted to enter your desired destination')
        print('Distance and travel time are automatically calculated')
        print('Eventually they will affect chance of Zed encounter')



    def help_quit(self):
        print('Just type "quit" ')






if __name__ == '__main__':
    print(opening_statement)
    print()
    print('Type "help" for a list of commands ')
    print()
    display_location(player_location)
    GamePrompt().cmdloop()
    print('Hope you enjoyed it, Zed-bait!')


# player_location = A1
# while True:
    
#     display_location(player_location)
#     response = input("travel where?")
#     if response == 'quit':
#         break
#     if response in [A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4]:
#         player_location = travel(player_location, response)
#         print(player_location)
#     else:
#         print("invalid entry")







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
