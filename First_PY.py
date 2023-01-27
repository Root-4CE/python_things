import os

#Privetstvie
print('Hi! Today we gona fuck this machine! Lets create a new directory for it first! Set new fuking name of this shit:')
dir_name = None
dir_name = input()
print(dir_name)

if dir_name is None and type(dir_name) != str:
    while dir_name is None:
        print('Error')
        dir_name == input()
else:
    print('Finaly!')

#Perduprejdenie

print('Are you realy shure what you want became a programmer?')

#chek 

check = input()

if check != 'yes' or 'y' and type(check) != str:
    print('Are you ebani tupoi? Just write "Yes or No" or for little babys "y / n"! Is that so hard?')
elif check == 'No' or 'n':
    quit() 
else:
    print ('OKeushki! Poehali!')

os.mkdir(dir_name, mode=0o777)
quit()