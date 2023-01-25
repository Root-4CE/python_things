import os

#Privetstvie
print('Hi! Today we gona fuck this machine! Lets create a new directory for it first! Set new fuking name of this shit:')
dir_name = input()
print(dir_name)

while dir_name == 0:
    print('Wrong things! Write again! Pisdec...')
    dir_name(input())

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
