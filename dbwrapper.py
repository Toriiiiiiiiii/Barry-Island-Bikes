import sqlite3

class DBWrapper:
    def __init__(self, path: str) -> None:
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
    
    def execute(self, sql: str):
        query = self.cursor.execute(sql).fetchall()
        
        return [ row for row in query ]
    
    def executeMany(self, sql, data):
        query = self.cursor.executemany(sql, data).fetchall()
        return [row for row in query]
    
    def saveChanges(self):
        self.connection.commit()
        
    def revertChanges(self):
        self.connection.rollback()
        
    def getFields(self, tableName: str) -> list:
        result = []

        tableInfo = self.execute(f"PRAGMA table_info({tableName});")
        
        for record in tableInfo:
            result.append(record[1])
            
        return result
    
    def printQuery(self, tableName: str, fields: list, fieldsRenamed: list = None, condition: str = None, showFieldNames: bool = True) -> None:
        if fieldsRenamed: 
            for index, field in enumerate(fields):
                fields[index] = field + f" AS {fieldsRenamed[index]}"
        if condition:
            queryResult = self.execute(f"SELECT {', '.join(fields)} FROM {tableName} WHERE {condition}")
        else:
            queryResult = self.execute(f"SELECT {', '.join(fields)} FROM {tableName}")
        
        fieldLengths = {}
        
        if not fieldsRenamed:
            for field in fields:
                fieldLengths[field] = len(field)
        else:
            for field in fieldsRenamed:
                fieldLengths[field] = len(field)
        
        for record in queryResult:
            for fieldIndex in range(len(fields)):
                fieldName = fields[fieldIndex] if not fieldsRenamed else fieldsRenamed[fieldIndex]
                
                if len(str(record[fieldIndex])) > fieldLengths[fieldName]:
                    fieldLengths[fieldName] = len(str(record[fieldIndex]))
                 
        print("| ", end="")
        if not fieldsRenamed:
            for field in fields:
                print(f"%-{fieldLengths[field]}s" %(field), end=" | ")
            print("\n|-", end="")
            
            for field in fields:
                print(f"-" * fieldLengths[field], end="-|")
                
                if field != fields[len(fields)-1]:
                    print("-", end="")
        else:
            for field in fieldsRenamed:
                print(f"%-{fieldLengths[field]}s" %(field), end=" | ")
                
            print("\n|-", end="")
            for field in fieldsRenamed:
                print(f"-" * fieldLengths[field], end="-|")
                
                if field != fieldsRenamed[len(fields)-1]:
                    print("-", end="")
            
                
        for record in queryResult:
            print("\n| ", end="")
            for fieldIndex in range(len(fields)):
                fieldName = fields[fieldIndex] if not fieldsRenamed else fieldsRenamed[fieldIndex]
                
                print(f"%-{fieldLengths[fieldName]}s" % record[fieldIndex], end=" | ")
            
        
        print()
        