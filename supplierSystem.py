import dbwrapper
import os

import shopdb
import bikeSystem

#===========================================================#

#### Global Declarations ####
shopdb.__setDB()
shopDatabase = shopdb.shopDatabase

#===========================================================#

def supplierMenu() -> None:
    bikeSystem.cls()
    
    choiceMap = {
        "1": displaySuppliers,
        "2": addSupplier,
        "3": editSupplier,
        "4": deleteSupplier,
        "5": reorderNotes,
    }
    
    choice = ""
    
    while choice != "x":
        print()
        print("=========================================")
        print("|  BARRY ISLAND BIKES => Supplier Menu  |")
        print("=========================================")
        print()
        
        print("1 - Display all suppliers")
        print("2 - Add a new supplier")
        print("3 - Edit a supplier")
        print("4 - Delete a supplier")
        print("5 - Display reorder notes")
        print("X - Back")
        print() 
        
        choice = input("[Choice] > ").lower()
        
        if choice in choiceMap:
            choiceMap[choice]()
            
            input("[Press ENTER] > ")
            bikeSystem.cls()
        elif choice == "x": 
            break
        else:
            print(f"Unrecognised choice '{choice}'")
            
def displaySuppliers():
    bikeSystem.cls()
    
    print("Displaying all Suppliers:")
    print("---------------------")
    print()
    shopDatabase.printQuery("suppliers", shopDatabase.getFields("suppliers"))
    print()


def addSupplier():
    bikeSystem.cls()

    choice = ""
    
    supplierID = ""
    supplierName = ""
    supplierAddress = ""
    supplierPhoneNum = ""
    supplierEmail = ""
    
    while True: 
        bikeSystem.cls()   
        print("Add new Supplier:")
        print("-----------------")
        print()
        
        print(f" 1 - Supplier ID   : {supplierID if supplierID else 'N/A'}")
        print(f" 2 - Company Name  : {supplierName if supplierName else 'N/A'}")
        print(f" 3 - Address       : {supplierAddress if supplierAddress else 'N/A'}")
        print(f" 4 - Phone Number  : {supplierPhoneNum if supplierPhoneNum else 'N/A'}")
        print(f" 5 - Email Address : {supplierEmail if supplierEmail else 'N/A'}")
        print(f" 6 - Submit")
        
        choice = input("[Choice] > ")
        
        if choice == "1":
            supplierID = input("[Change ID] > ")
        elif choice == "2":
            supplierName = input("[Change Name] > ")
        elif choice == "3":
            supplierAddress = input("[Change Address] > ")
        elif choice == "4":
            supplierPhoneNum = input("[Change Phone Number] > ")
        elif choice == "5":
            supplierEmail = input("[Change Email] > ")
        elif choice == "6":
            if not(supplierID or supplierName or supplierAddress or supplierPhoneNum or supplierEmail):
                print("All fields must be defined!")
                continue
            
            data = [
                (supplierID, supplierName, supplierAddress, supplierPhoneNum, supplierEmail)
            ]
            
            shopDatabase.executeMany(f"INSERT INTO suppliers VALUES(?,?,?,?,?)", data)
            shopDatabase.saveChanges()
            return

def editSupplier():
    bikeSystem.cls()
    print("=============================")
    print("| Edit Supplier Information |")
    print("=============================")
    print()
    
    supplierID = input("[Supplier ID] > ")
    
    queryResult = shopDatabase.execute(f"SELECT * FROM suppliers WHERE supplierID = '{supplierID}'")
    
    while len(queryResult) == 0:
        print(f"ERROR : Supplier with ID {supplierID} was not found!")
        supplierID = input("[Supplier ID] > ")
    
    supplierName = queryResult[1]
    supplierAddress = queryResult[2]
    supplierPhoneNum = queryResult[3]
    supplierEmail = queryResult[4]
    
    while True:
        bikeSystem.cls()
        print("=============================")
        print("| Edit Supplier Information |")
        print("=============================")
        print()
        
        print(f" 1 - Supplier ID  : {supplierID if supplierID else 'N/A'}")
        print(f" 2 - Company Name : {supplierName if supplierName else 'N/A'}")
        print(f" 3 - Address      : {supplierAddress if supplierAddress else 'N/A'}")
        print(f" 4 - Phone Number : {supplierPhoneNum if supplierPhoneNum else 'N/A'}")
        print(f" 5 - Email        : {supplierEmail if supplierEmail else 'N/A'}")
        print(f" 6 - Back")
        
        choice = input("[Choice] > ")
        
        if choice == "1":
            supplierID = input("[Change ID] > ")
        elif choice == "2":
            supplierName = input("[Change Make] > ")
        elif choice == "3":
            supplierAddress = input("[Change Model] > ")
        elif choice == "4":
            supplierPhoneNum = input("[Change Size] > ")
        elif choice == "5":
            supplierEmail = input("[Change Supplier] > ")
        elif choice == "6":
            shopDatabase.execute(f"UPDATE suppliers SET supplierID='{supplierID}', name='{supplierName}', address='{supplierAddress}', phone='{supplierPhoneNum}', email='{supplierEmail}' WHERE supplierID='{supplierID}'")
            shopDatabase.saveChanges()
            return
        

def deleteSupplier():
    bikeSystem.cls()
    print("===================")
    print("| Delete Supplier |")
    print("===================")
    print()
    
    supplierID = input("[Supplier ID] > ")
    
    queryResult = shopDatabase.execute(f"SELECT * FROM suppliers WHERE supplierID = '{supplierID}'")
    
    while len(queryResult) == 0:
        print(f"ERROR : Supplier with ID {supplierID} was not found!")
        supplierID = input("[Supplier ID] > ")
        
    shopDatabase.execute(f"DELETE from suppliers WHERE supplierID='{supplierID}'")
    shopDatabase.saveChanges()
    
    print("-_- Supplier Deleted -_-")

def reorderNotes():
    suppliers = shopDatabase.execute("SELECT * FROM suppliers")
    
    for supplier in suppliers:
        id = supplier[0]
        
        queryResult = shopDatabase.execute(f"SELECT bikes.bikeID FROM bikes, suppliers WHERE suppliers.supplierID='{id}' AND bikes.supplier=suppliers.supplierID AND bikes.stockLevel < bikes.reorderLevel")
        if len(queryResult) == 0: continue
        
        name = supplier[1]
        address = supplier[2]
        phone = supplier[3]
        email = supplier[4]
        
        print(f"** Reorder Note for {name} (ID : {id}) **")
        print(f" |-> Company Name    : {name}")
        print(f" |-> Company Address : {address}")
        print(f" |-> Phone Number    : {phone}")
        print(f" |-> Email Address   : {email}")
        
        print()
        print("Requesting order of the following to be sent to Barry Island Bikes Ltd:")
        print("-----------------------------------------------------------------------")
        print()
        shopDatabase.printQuery("bikes, suppliers", ["bikes.bikeID", "bikes.make", "bikes.model", "bikes.buyingPrice", "bikes.reorderAmount"], fieldsRenamed=["ID", "Make", "Model", "Price", "Amount"], condition=f"suppliers.supplierID='{id}' AND bikes.supplier=suppliers.supplierID")
        
        print("\n")