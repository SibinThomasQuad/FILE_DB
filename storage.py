import os
from pathlib import Path
from shutil import rmtree



"""
-------------------------------------------------------------------------------

                File Type Database
                
->      Created by       :   Sibin Thomas
->      Created on       :   2022/07/22
->      Last updated on  :   2022/07/22

-------------------------------------------------------------------------------

"""
class Collection:
    def root(self):
        return 'MAIL'
    def remove(self,collection_name):
        dir_path = os.path.join(str(self.root()), collection_name)
        try:
            rmtree(dir_path)
            return True
        except:
            return False
    
    def create(self,collection_name):
        try:
            os.mkdir(os.path.join(str(self.root()), collection_name))
            return True
        except:
            return False
    
    
    def insertData(self,collection_name,data_name,data):
        try:
            full_path = os.path.join(str(self.root()), collection_name+"/"+str(data_name)+".data")
            file = open(full_path, "a")
            file.write(str(data))
            file.close()
            return True
        except:
            return False
    
    
    def getData(self,collection_name,data_name):
        try:
            full_path = os.path.join(str(self.root()), collection_name+"/"+str(data_name)+".data")
            file = open(str(full_path), "r")
            datas = file.read()
            return datas
        except:
            return False
    
    
    def deleteData(self,collection_name,data_name):
        try:
            os.remove(os.path.join(str(self.root()), collection_name+"/"+str(data_name)+".data"))
            return True
        except:
            return False
    
    
    def updateData(self,collection_name,data_name,data):
        try:
            os.remove(os.path.join(str(self.root()), collection_name+"/"+str(data_name)+".data"))
            full_path = os.path.join(str(self.root()), collection_name+"/"+str(data_name)+".data")
            file = open(full_path, "a")
            file.write(str(data))
            file.close()
            return True
        except:
            return False
    
    
    def appendData(self,collection_name,data_name,data):
        try:
            full_path = os.path.join(str(self.root()), collection_name+"/"+str(data_name)+".data")
            file = open(full_path, "a")
            file.write(str(data))
            file.close()
            return True
        except:
            return False
