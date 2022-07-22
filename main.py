import os
from pathlib import Path
"""

-> File Type Database
-> Created by Sibin Thomas
-> Created on 2022/07/22

"""
class Collection:
    def create(self,collection_name):
        try:
            os.mkdir(collection_name)
            return True
        except:
            return False
    
    
    def insertData(self,collection_name,data_name,data):
        try:
            full_path = os.path.join(collection_name, str(data_name)+".data")
            file = open(full_path, "a")
            file.write(str(data))
            file.close()
            return True
        except:
            return False
    
    
    def getData(self,collection_name,data_name):
        try:
            full_path = os.path.join(collection_name, str(data_name)+".data")
            file = open(str(full_path), "r")
            datas = file.read()
            return datas
        except:
            return False
    
    
    def deleteData(self,collection_name,data_name):
        try:
            os.remove(os.path.join(collection_name, str(data_name)+".data"))
            return True
        except:
            return False
    
    
    def updateData(self,collection_name,data_name,data):
        try:
            os.remove(os.path.join(collection_name, str(data_name)+".data"))
            full_path = os.path.join(collection_name, str(data_name)+".data")
            file = open(full_path, "a")
            file.write(str(data))
            file.close()
            return True
        except:
            return False
    
    
    def appendData(self,collection_name,data_name,data):
        try:
            full_path = os.path.join(collection_name, str(data_name)+".data")
            file = open(full_path, "a")
            file.write(str(data))
            file.close()
            return True
        except:
            return False





#-----USE----------

#db declaration
db = Collection()
collection = 'Names'

#creating collection
db.create(collection)

#insert data to a dataset
db.insertData(collection,'first_name','sibin thomas')

#update data to dataset
db.updateData(collection,'first_name','New Name')

#view datas from data set
print(db.getData(collection,'first_name'))
