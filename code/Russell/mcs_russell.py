import cmd, math, random

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
scavenged = 'scavenged'
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
        scavenged: 0},
    A2: {
        coord: (1, 2),
        scavenged: 0},
    A3: {
        coord: (1, 3),
        scavenged: 0},
    A4: {
        coord: (1, 4),
        scavenged: 0},
    
    B1: {
        coord: (2, 1),
        scavenged: 0},
    B2: {
        coord: (2, 2),
        scavenged: 0},
    B3: {
        coord: (2, 3),
        POIs: [],
        scavenged: 0},
    B4: {
        coord: (2, 4),
        scavenged: 0},
    
    C1: {
        coord: (3, 1),
        scavenged: 0},
    C2: {
        coord: (3, 2),
        POIs: [],
        scavenged: 0},
    C3: {
        coord: (3, 3),
        scavenged: 0},
    C4: {
        coord: (3, 4),
        POIs: [],
        scavenged: 0},

    D1: {
        coord: (4, 1),
        scavenged: 0},
    D2: {
        coord: (4, 2),
        scavenged: 0},
    D3: {
        coord: (4, 3),
        scavenged: 0},
    D4: {
        coord: (4, 4),
        scavenged: 0}
        
}


world_items = ['Gun', 'Taco', 'Soda', 'Survivor']



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
    print(f"scavenged level: {world_locations[player_location][scavenged]}")



def scavenge(location): 
# Once in a specific POI, allows player to scavenge
# Scavenging can be done all at once (level 3), or a little at a time (one level 2, two level 1, or similar)

    # should randomly select item and incrememt 'looted' level

    if world_locations[location][scavenged] < 3:

        found = random.choice(world_items) # there should be more to this...
        inventory.append(found)
        world_locations[location][scavenged] +=1   # not every search should return an item
        if world_locations[location][scavenged] > 3:
            world_locations[location][scavenged] = 3
        print(f'You found {found}')

    elif world_locations[location][scavenged] == 3:
        print('You already found everything here')
    



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
    if player_location in world_locations and destination in world_locations and destination != player_location:
        x1, y1 = world_locations[player_location]['coord']
        x2, y2 = world_locations[destination]['coord']
    
        distance = math.dist([x1, y1], [x2, y2])        
        distance= (round(distance, 2))     ## SHOULD THIS ALSO ACCOUNT FOR TIME OR IS THAT A SEPARATE FUNCTION??
        travel_time = round(distance / 2, 2)
        
        
        return travel_time

    elif destination == player_location:
        print("You are already at that grid location ")

    else:
        print("Please enter a valid grid location ")



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

        scavenge(player_location)



    def do_travel(self, arg):
        # Moves player to new grid location
        global player_location
        destination = input("Enter desired grid location ")
        tt= travel_time(player_location, destination)
        location_hold = player_location
        player_location = travel(player_location, destination) 
        
        if player_location == None:
            player_location = location_hold

        else:
            print(f'You travel for {tt} hours to reach grid location {destination} ')
        





    ### HELP_ FUNCTIONS - will run when players types 'help' followed by a valid help command (ex: 'help travel')
    
    def help_combat(self):
        print('Yeah, that is not a thing yet...maybe in the update ')



    def help_inventory(self):
        print('Type "inventory" to show a list of what you\'ve gathered so far')



    def help_location(self):
        print('Type "location" to show current location along with its scavenged level')



    def help_map(self):
        print('Draw one, ya lazy ')



    def help_scavenge(self):
        print('Type "scavenge" to check location for food/drink/surivivors')
        print('Each location can be scavenged up to 3 times')



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