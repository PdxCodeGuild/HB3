print('Lab 11: Jackalope Lab')

jackalope_guys = [0, 0]
years = 0

while len(jackalope_guys) < 1000:
    for index in range(len(jackalope_guys)):
        jackalope_guys[index] += 1
        
        if jackalope_guys[index] >= 4 and jackalope_guys[index] <= 8:
            jackalope_guys.append(0)
            
        jackalope_guys = list(filter(lambda a: a!= 10, jackalope_guys))
        
    years += 1
    
print(f'''It will take {years} years for 2 jackalope guys to turn into 1000 lopes...
      seriously build a fence or something!''')