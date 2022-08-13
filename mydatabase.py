import mysql.connector

class database():
    def __init__(self, hostname, username, password):
        self.config = {
            "host": hostname,
            "user": username,
            "password": password,
            }        
        self.mydb = mysql.connector.connect(**self.config)
        if self.mydb:
            print ("Connected Successfully")
        else:
            print ("Connection Not Established")
        self.mycursor = self.mydb.cursor()
    
    # Create a new Database
    def createDB(self, named_db):
        self.named_db = named_db
        self.mycursor.execute("CREATE DATABASE {}".format(self.named_db))
        print("Create Database {} Succesfully".format(self.named_db))
    
    # Create a new Table in Database
    def createTableDB(self, named_db, tablename, name1, name2, name3, name4):
        self.named_db = named_db
        self.tablename = tablename
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.named_db
            
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("CREATE TABLE {} ( \
                               {} INT AUTO_INCREMENT PRIMARY KEY,\
                               {} VARCHAR(255), {} INT UNIQUE, {} BOOLEAN)"
                               .format(self.tablename, self.name1, self.name2, self.name3, self.name4))
        print("Create Database Table Succesfully")
    
    # Insert data on table from new
    def insertDataDBNew(self, named_db, table_name, inTable1, inTable2, inTable3, data):
        self.dataIn = data
        self.named_dbIn = named_db
        self.table_name = table_name
        self.inTable1 = inTable1
        self.inTable2 = inTable2
        self.inTable3 = inTable3
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.named_dbIn
        
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(self.table_name, self.inTable1, self.inTable2, self.inTable3)
        self.mycursor.executemany(self.sql, self.dataIn)
        self.mydb.commit()
        print(self.mycursor.rowcount, "was inserted.")
    
    # Insert data in database if Not Exists
    def insertDataDBIfNotExists(self, named_db, table_name, inTable1, inTable2, inTable3, data):
        self.dataIn = data
        self.named_dbIn = named_db
        self.table_name = table_name
        self.inTable1 = inTable1
        self.inTable2 = inTable2
        self.inTable3 = inTable3
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.named_dbIn
        
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "INSERT IGNORE INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(self.table_name, self.inTable1, self.inTable2, self.inTable3)
        self.mycursor.executemany(self.sql, self.dataIn)
        self.mydb.commit()
        print(self.mycursor.rowcount, "was inserted.")
    
    # Insert Data on table database if exists
    def insertDataDBIfExists(self, named_db, table_name, inTable1, inTable2, inTable3, data):
        self.dataIn = data
        self.named_dbIn = named_db
        self.table_name = table_name
        self.inTable1 = inTable1
        self.inTable2 = inTable2
        self.inTable3 = inTable3
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.named_dbIn
        
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "REPLACE INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(self.table_name, self.inTable1, self.inTable2, self.inTable3)
        self.mycursor.executemany(self.sql, self.dataIn)
        self.mydb.commit()
        print(self.mycursor.rowcount, "was inserted.")
    
    # read table on database
    def readDB(self, named_db, namedTable):
        self.readnamed_db = named_db
        self.namedTable = namedTable
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.readnamed_db
 
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "SELECT * FROM {}".format(self.namedTable)
        self.mycursor.execute(self.sql)
        self.myresult = self.mycursor.fetchall()
        return self.myresult
        #for x in self.myresult:
            #print(x)
        
    # read database column
    def readColumnDB(self, named_db, namedTable, nameColumn, rowColumn):
        self.readnamed_db = named_db
        self.namedTable = namedTable
        self.nameColumn = nameColumn
        self.rowColumn = rowColumn
        if 'database' not in self.config.keys():
            self.config['database'] = self.readnamed_db
 
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "SELECT * FROM {} WHERE {} = {}".format(self.namedTable)
        self.mycursor.execute(self.sql)
        self.myresult = self.mycursor.fetchall()
        return self.myresult
       
    # delete table from database
    def deleteTableDB(self, named_db, namedTable):
        self.readnamed_db = named_db
        self.namedTable = namedTable
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.readnamed_db
 
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "DROP TABLE IF EXISTS {}".format(self.namedTable)
        self.mycursor.execute(self.sql)
        print("Table {} in {} Database Deleted".format(self.namedTable, self.readnamed_db))
    
    # select database for view
    def selectDB(self, named_db):
        self.readnamed_db = named_db
        if 'database' not in self.config.keys():
            self.config['database'] = self.readnamed_db
        return self.readnamed_db
    
    # connection data from database to dashboard
    def connectDB(self, named_db):
        self.readnamed_db = named_db
        if 'database' not in self.config.keys():
            self.config['database'] = self.readnamed_db
        self.mydb = mysql.connector.connect(**self.config)
        return self.mydb
    
    # change value in database
    def updateTableDB(self, named_db, table_name, nameColumn1, nameColumn2, newVal, lastVal):
        self.named_dbIn = named_db
        self.table_name = table_name
        self.nameColumn1 = nameColumn1
        self.nameColumn2 = nameColumn2
        self.newVal = newVal
        self.lastVal = lastVal
        
        self.dataIn = (newVal,lastVal)
        if 'database' not in self.config.keys():
            self.config['database'] = self.named_dbIn
        
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "UPDATE {} SET {} = %s WHERE {} = %s".format(self.table_name, self.nameColumn1, self.nameColumn2)
        self.mycursor.execute(self.sql, self.dataIn)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) affected")
     
     # add new table to database
    def alterTableDB(self, named_db, tablename, nameCol, tipeData):
        self.named_db = named_db
        self.tablename = tablename
        self.nameCol = nameCol
        self.tipeData = tipeData
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.named_db
            
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("ALTER TABLE {} ADD COLUMN {} {}".format(self.tablename, self.nameCol, self.tipeData))
        print("Create Database Table Succesfully")
    
    # convert database data to json
    def convertJson(self, named_db, namedTable, colum1, colum2, colum3):
        self.readnamed_db = named_db
        self.namedTable = namedTable
        self.colum1 = colum1
        self.colum2 = colum2
        self.colum3 = colum3
        
        if 'database' not in self.config.keys():
            self.config['database'] = self.readnamed_db
 
        self.mydb = mysql.connector.connect(**self.config)
        self.mycursor = self.mydb.cursor()
        self.sql = "SELECT JSON_ARRAYAGG(JSON_OBJECT('name', {}, 'value', {}, 'detection', {})) FROM {}".format(self.colum1, self.colum2, self.colum3, self.namedTable)
        self.mycursor.execute(self.sql)
        self.myresult = self.mycursor.fetchall()
        return self.myresult
        