# Import the necessary packages
import click
import os
from cursesmenu import *
from cursesmenu.items import *
import datetime
import fileinput
# Create the menu
def login():
    root  = os.getcwd()
    notes = root+'/notes/'
    print('welconme Back..User')
    name =str(input('Enter your Name..'))
    with open(os.getcwd()+'/confi.txt','r+') as f:
        outter  =f.read().split(',')
        for u in outter:
            inner = u.split(':')
            if inner[0]  == name:
                password = str(input('Please ENter your Password..'))
                if inner[1] == password:
                    show(name)
                else:
                    print('Wrong Password')
        if inner[0] != name: 
                print('ooops..')
                confi = str(input('No user '+name+' Would you Like to add..(y/n)'))
                if confi == 'y':
                    try:
                        with open(root+'/confi.txt','a+') as foo:
                            password = str(input("Please Choose Password"))
                            foo.write(','+name+':'+password)
                            os.mkdir(notes+'/'+name)
                            show(name)
                    except:
                        print('error')
    

                
def show(name):

    menu = CursesMenu("Diary in python", "hello "+name)

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Menu Item")

    # A FunctionItem runs a Python function when selected
    function_item = FunctionItem("Add new Note",add_note,[name])

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command",  "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(os.listdir(os.getcwd()+'/notes/'))

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Previous Notes", selection_menu,add_note,)
    menu.append_item(function_item)
    '''user_list  =os.listdir(os.getcwd()+'/cnf/')
    if user_list == '':
        menu.append_item(FunctionItem('Login..',login))
        menu.append_item(FunctionItem('Signup',login))'''
    for x in os.listdir(os.getcwd()+'/notes/'+name):
        #all_items.append()
        #menu.append_item(menu_item)
        #menu.append_item(function_item)
        #menu.append_item(command_item)
        menu.append_item(FunctionItem(x,show_note,[name,x]))        
    menu.show()
def add_note(name):
    time = str(datetime.datetime.now())
    data = str(input('write here..'))
    save  = str(input('Would You like to save this note..(y/n)'))
    dicto = os.getcwd()+'/notes/'+name+'/'
    if save  =='y':
        with open(dicto+time+'.txt','w+') as f:
            f.write(data)
            f.close()
            print('saved Successfully')

def show_note(folder_name,name):
    print('Previous notes')
    with open(os.getcwd()+'/notes/'+folder_name+'/'+name,'r+') as files:
        data = files.read()
    print(data)


if __name__ == "__main__":
    login()