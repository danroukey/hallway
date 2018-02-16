map_hold = 0

answer = input("Do you want to pick up the map? (yes/no): ").strip().lower()

if answer not in ["yes", "no"]:
    print("Please choose a valid answer.")
    answer = input("Do you want to pick up the map? (yes/no): ").strip().lower()

if answer == "yes" :
    map_hold = 1
    print("You now have a map!")

if answer == "no" :
    map_hold = 0
    print("You choose to not pick up the map.")
    print("What would you like to do next?")
    choice = input("What would you like to do next?").strip().lower()


if map_hold == 1 :
    display_map = input("Do you want to open the map? (yes/no): ").strip().lower()
    
    if display_map not in ["yes", "no"]:
        print("Please choose a valid answer.")

    if display_map == "yes":
        #open map file
        map_file = open("mapfile.txt", "r")
        display = map_file.read(100000)
        print(display)

        #close map file
        map_file.close()
        choice = input("What would you like to do next?").strip().lower()

    if display_map == "no":
        print("You put the map in your bag.")
        choice = input("What would you like to do next?").strip().lower()


#if user types map, display map
while choice == "map" :
    #open map file
    map_file = open("mapfile.txt", "r")
    display = map_file.read(100000)
    print(display)

    #close map file
    map_file.close()
    choice = input("What would you like to do next?").strip().lower()




