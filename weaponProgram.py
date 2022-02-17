from email import header
import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
readFile = open("weapons.txt","r")

# create a csv object from the file object

csvObj = csv.reader(readFile, delimiter = ',')

#skip the header row
next(csvObj)




#create an empty dictionary named 'weapons_dict'
weapons_dict = {}



#use a for loop to iterate through every row of the csv file
for record in csvObj:

    name = record[0]
    speed = record[1]
    weaponRange = record[2]
    #use variables for name,speed and range (optional)
    

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    weaponSpecs = w.weapon(name,speed,weaponRange)


    # append the name and bullet count to 'weapons_dict'
    weapons_dict[name] = weaponSpecs.get_bullets()


    # print out the name of the weapon using the appropriate method of the object 
    print("Weapon Name:",weaponSpecs.get_name())

    # print out the speed of the weapon using the appropriate method of the object
    print("Weapon Speed:",weaponSpecs.get_speed())

    # print out the range of the weapon using the appropriate method of the object
    print("Weapon Range:",weaponSpecs.get_range())

    # print out the number of bullets of the weapon using the appropriate method of the object
    print("Bullets:",weaponSpecs.get_bullets())


    #use an input statement to halt the program and wait for the user - 
    input("Enter any key to fire")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    while weaponSpecs.get_status() == "Active":

        # call the appropriate method to fire a bullet
        weaponSpecs.fire_bullet()
        
        # print out the bullet count every time the weapon is fired
        print("Bullets Remaining:",weaponSpecs.get_bullets(),end="\r")
    
    print ("Bullets Remaining:",weaponSpecs.get_bullets())

    

#using a loop print out the name and number of bullets from the dictionary
for element in weapons_dict:
    print ("{:<25} {:<25}".format("Weapon Name: "+element,"Number of Bullets: "+str(weapons_dict[element])))



    


    



