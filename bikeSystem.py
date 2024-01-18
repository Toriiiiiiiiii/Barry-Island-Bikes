import dbwrapper
import os

#===========================================================#

import shopdb

shopdb.__setDB()
shopDatabase = shopdb.shopDatabase

#===========================================================#
#### Utility Functions ####

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
#===========================================================#
#### Bike Database Systems ####

def bikeMenu() -> None:
    cls()
    
    choiceMap = {
        "1": displayAllBikes,
        "2": addNewBike,
        "3": editBike,
        "4": deleteBike
    }
    
    choice = ""
    
    while choice != "x":
        print()
        print("===========================================")
        print("|  BARRY ISLAND BIKES => Bike Stock Menu  |")
        print("===========================================")
        print()
        
        print("1 - Display all bikes")
        print("2 - Add a new bike")
        print("3 - Edit a bike")
        print("4 - Delete a bike")
        print("X - Back")
        print() 
        
        choice = input("[Choice] > ").lower()
        
        if choice in choiceMap:
            choiceMap[choice]()
            
            input("[Press ENTER] > ")
            cls()
        elif choice == "x": 
            break
        else:
            print(f"Unrecognised choice '{choice}'")


def displayAllBikes() -> None:
    cls()
    
    print("Displaying all Bikes:")
    print("---------------------")
    print()
    shopDatabase.printQuery("bikes", shopDatabase.getFields("bikes"))
    print()


def addNewBike() -> None:
    cls()

    choice = ""
    
    bikeID = ""
    bikeMake = ""
    bikeModel = ""
    bikeSize = ""
    bikeSupplier = ""
    bikeBuyingPrice = 0
    bikeSellingPrice = 0
    bikeStockLevel = 0
    bikeReorderLevel = 0
    bikeReorderAmount = 0
    
    while True: 
        cls()   
        print("Add new Bike:")
        print("-------------")
        print()
        
        print(f" 1 - Bike ID        : {bikeID if bikeID else 'N/A'}")
        print(f" 2 - Make           : {bikeMake if bikeMake else 'N/A'}")
        print(f" 3 - Model          : {bikeModel if bikeModel else 'N/A'}")
        print(f" 4 - Size           : {bikeSize if bikeSize else 'N/A'}")
        print(f" 5 - Supplier       : {bikeSupplier if bikeSupplier else 'N/A'}")
        print(f" 6 - Buy Price      : {bikeBuyingPrice if bikeBuyingPrice else 'N/A'}")
        print(f" 7 - Sale Price     : {bikeSellingPrice if bikeSellingPrice else 'N/A'}")
        print(f" 8 - In Stock       : {bikeStockLevel if bikeStockLevel else 'N/A'}")
        print(f" 9 - Reorder Level  : {bikeReorderLevel if bikeReorderLevel else 'N/A'}")
        print(f"10 - Reorder Amount : {bikeReorderAmount if bikeReorderAmount else 'N/A'}")
        print(f"11 - Submit")
        
        choice = input("[Choice] > ")
        
        if choice == "1":
            bikeID = input("[Change ID] > ")
        elif choice == "2":
            bikeMake = input("[Change Make] > ")
        elif choice == "3":
            bikeModel = input("[Change Model] > ")
        elif choice == "4":
            bikeSize = input("[Change Size] > ")
        elif choice == "5":
            bikeSupplier = input("[Change Supplier] > ")
        elif choice == "6":
            bikeBuyingPrice = float(input("[Change Buy Price] > "))
        elif choice == "7":
            bikeSellingPrice = float(input("[Change Sale Price] > "))
        elif choice == "8":
            bikeStockLevel = int(input("[Change Stock Level] > "))
        elif choice == "9":
            bikeReorderLevel = int(input("[Change Reorder Level] > "))
        elif choice == "10":
            bikeReorderAmount = int(input("[Change Reorder Amount] > "))
        elif choice == "11":
            if not(bikeID or bikeMake or bikeModel or bikeSize or bikeSupplier or bikeBuyingPrice or bikeSellingPrice or bikeStockLevel or bikeReorderLevel or bikeReorderAmount):
                print("All fields must be defined!")
                continue
            
            data = [
                (bikeID, bikeMake, bikeModel, bikeSize, bikeSupplier, bikeBuyingPrice, bikeSellingPrice, bikeStockLevel, bikeReorderLevel, bikeReorderAmount)
            ]
            
            shopDatabase.executeMany(f"INSERT INTO bikes VALUES(?,?,?,?,?,?,?,?,?,?)", data)
            shopDatabase.saveChanges()
            return
        

def editBike() -> None:
    cls()
    print("=========================")
    print("| Edit Bike Information |")
    print("=========================")
    print()
    
    bikeID = input("[Bike ID] > ")
    
    queryResult = shopDatabase.execute(f"SELECT * FROM bikes WHERE bikeID = '{bikeID}'")
    
    while len(queryResult) == 0:
        print(f"ERROR : Bike with ID {bikeID} was not found!")
        bikeID = input("[Bike ID] > ")
    
    bikeMake = queryResult[0][1]
    bikeModel = queryResult[0][2]
    bikeSize = queryResult[0][3]
    bikeSupplier = queryResult[0][4]
    bikeBuyingPrice = queryResult[0][5]
    bikeSellingPrice = queryResult[0][6]
    bikeStockLevel = queryResult[0][7]
    bikeReorderLevel = queryResult[0][8]
    bikeReorderAmount = queryResult[0][9]
    
    while True:
        cls()
        print("=========================")
        print("| Edit Bike Information |")
        print("=========================")
        print()
        
        print(f" 1 - Bike ID        : {bikeID if bikeID else 'N/A'}")
        print(f" 2 - Make           : {bikeMake if bikeMake else 'N/A'}")
        print(f" 3 - Model          : {bikeModel if bikeModel else 'N/A'}")
        print(f" 4 - Size           : {bikeSize if bikeSize else 'N/A'}")
        print(f" 5 - Supplier       : {bikeSupplier if bikeSupplier else 'N/A'}")
        print(f" 6 - Buy Price      : {bikeBuyingPrice if bikeBuyingPrice else 'N/A'}")
        print(f" 7 - Sale Price     : {bikeSellingPrice if bikeSellingPrice else 'N/A'}")
        print(f" 8 - In Stock       : {bikeStockLevel if bikeStockLevel else 'N/A'}")
        print(f" 9 - Reorder Level  : {bikeReorderLevel if bikeReorderLevel else 'N/A'}")
        print(f"10 - Reorder Amount : {bikeReorderAmount if bikeReorderAmount else 'N/A'}")
        print(f"11 - Back")
        
        choice = input("[Choice] > ")
        
        if choice == "1":
            bikeID = input("[Change ID] > ")
        elif choice == "2":
            bikeMake = input("[Change Make] > ")
        elif choice == "3":
            bikeModel = input("[Change Model] > ")
        elif choice == "4":
            bikeSize = input("[Change Size] > ")
        elif choice == "5":
            bikeSupplier = input("[Change Supplier] > ")
        elif choice == "6":
            bikeBuyingPrice = float(input("[Change Buy Price] > "))
        elif choice == "7":
            bikeSellingPrice = float(input("[Change Sale Price] > "))
        elif choice == "8":
            bikeStockLevel = int(input("[Change Stock Level] > "))
        elif choice == "9":
            bikeReorderLevel = int(input("[Change Reorder Level] > "))
        elif choice == "10":
            bikeReorderAmount = int(input("[Change Reorder Amount] > "))
        elif choice == "11":
            shopDatabase.execute(f"UPDATE bikes SET bikeID='{bikeID}', make='{bikeMake}', model='{bikeModel}', size='{bikeSize}', supplier='{bikeSupplier}', buyingPrice={bikeBuyingPrice}, sellingPrice={bikeSellingPrice}, stockLevel={bikeStockLevel}, reorderLevel={bikeReorderLevel}, reorderAmount={bikeReorderAmount} WHERE bikeID='{bikeID}'")
            shopDatabase.saveChanges()
            return
        

def deleteBike() -> None:
    cls()
    print("===============")
    print("| Delete Bike |")
    print("===============")
    print()
    
    bikeID = input("[Bike ID] > ")
    
    queryResult = shopDatabase.execute(f"SELECT * FROM bikes WHERE bikeID = '{bikeID}'")
    
    while len(queryResult) == 0:
        print(f"ERROR : Bike with ID {bikeID} was not found!")
        bikeID = input("[Bike ID] > ")
        
    shopDatabase.execute(f"DELETE from bikes WHERE bikeID='{bikeID}'")
    shopDatabase.saveChanges()
    
    print("-_- Bike Deleted -_-")