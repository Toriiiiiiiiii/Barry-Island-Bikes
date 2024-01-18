#===========================================================#
# BARRY ISLAND BIKES                                        #
# v1.0                                                      #
#                                                           #
# START:  08/01/24                                          #
# FINISH: --/--/--                                          #
# AUTHOR: Cory 'Tori' Hall                                  #
#===========================================================#

#### Imports ####
import shopdb
import os

if not os.path.isfile("SHOP DATABASE.db"):
    shopdb.__resetDB()

shopdb.__setDB()
import bikeSystem
import supplierSystem

if __name__ == "__main__":
    
    while True:
        bikeSystem.cls()
        
        print("======================")
        print("| BARRY ISLAND BIKES |")
        print("======================")
        
        print()
        print("1 - Bike Menu")
        print("2 - Supplier Menu")
        print("x - Exit")
        
        choice = input("[Choice] > ")
        
        if choice == "1":
            bikeSystem.bikeMenu()
        elif choice == "2":
            supplierSystem.supplierMenu()
        elif choice == "x":
            break
        
        else:
            print("Please enter a valid option.")
            input("[Press ENTER] > ")