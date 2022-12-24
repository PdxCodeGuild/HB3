import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
import requests
import webbrowser

root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('250x150')

def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    return colors
    root.configure(bg=colors[1])

ttk.Button(
    root,
    text='Select a Color',
    command=change_color).pack(expand=True)
root.mainloop

# root.mainloop() #----root.mainloop() loops forever until user exits program
color = change_color()
color = color[1]
color = color.replace('#','')
# print(color)

color_link = requests.get(f'https://www.thecolorapi.com/id?hex={color}')
color_json = color_link.json()
color_name = color_json['name']['value']
print(f'You chose {color} also known as {color_name}')

#---------------------------------------------------------------User Interaction-------------------------
user = input('Would you like to see matching colors? Y/N ')

if user == 'yes' or user == 'Y':
    schemes = requests.get(f'https://www.thecolorapi.com/scheme?hex={color}')
    scheme = schemes.json()
    color_scheme = scheme['colors']
    for names in color_scheme:
        print(names['name']['value'])
    new_command = (input('Contiue to visual board..?'))
    if new_command == 'Y' or new_command == 'yes':
        webbrowser.open(f'https://www.thecolorapi.com/scheme?hex={color}&format=html')
    elif new_command == 'no' or new_command == 'N':
        print("Exit")
    else: 
        print('Unknown command\\Returning home.')
elif user == 'no' or user == 'N':
    print('Come back again!!')
else:
    if user != 'yes' or user != 'Y' or user != 'N' or user != 'no':
        print('Exit')




    
    
# color_info = list(color_json.values('name','value'))
# print(color_info)
# for name in color_info:
#     print(name['name']['value'])

#------------------------------------------------------Scheme Info--------------------------------------------------------

# schemes = requests.get(f'https://www.thecolorapi.com/scheme?hex={color}')
# #------ Tell user the name of the color they chose
# scheme = schemes.json()
# color_scheme = scheme['colors']



# for names in color_scheme:
#     print(names['name']['value'])
# ---print(color_scheme)
# ---print(names)
# webbrowser.open_new_tab(f'https://www.thecolorapi.com/scheme?hex={color}&format=html')