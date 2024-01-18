import dbwrapper
import os

def __resetDB() -> None:
    global shopDatabase
    shopDatabase = dbwrapper.DBWrapper("SHOP DATABASE.db")
    
    shopDatabase.execute("""CREATE TABLE bikes(
                            bikeID TEXT PRIMARY KEY,
                            make TEXT,
                            model TEXT,
                            size TEXT,
                            supplier TEXT,
                            buyingPrice REAL,
                            sellingPrice REAL,
                            stockLevel INTEGER,
                            reorderLevel INTEGER,
                            reorderAmount INTEGER)""")
    
    data = [
        ('WW23', 'Merlin', 'Wizard', 'L', 'XBikes', 200.99, 310.99, 7, 2, 10)
    ]
    
    shopDatabase.executeMany("INSERT INTO bikes VALUES(?,?,?,?,?,?,?,?,?,?)", data)
    shopDatabase.saveChanges()
    
    shopDatabase.execute("""CREATE TABLE suppliers(
                            supplierID TEXT PRIMARY KEY,
                            company TEXT,
                            address TEXT,
                            phone TEXT,
                            email TEXT)""")
    
    data = [
        ('XBikes', 'XBikes Ltd', '123 Biker Avenue', '02734 063365', 'contact@xbikes.org')
    ]
    
    shopDatabase.executeMany("INSERT INTO suppliers VALUES(?,?,?,?,?)", data)
    shopDatabase.saveChanges()
    

def __setDB():
    global shopDatabase
    shopDatabase = dbwrapper.DBWrapper("SHOP DATABASE.db")

#### Global Declarations ####
shopDatabase = None