import unittest
from sqlManagerLib.SqlReader import sqlManager

class sqlTester(unittest.TestCase):
    def testOffices(self):
        record=dict()
        
        record["city"]="uno"
        record["phone"]="dos"
        manager=sqlManager(server="localhost",database="cochesDb",username="Libreria",password="monkey1!")
        manager.insertOffice(record)



def testorders():
    manager=sqlManager(server="localhost",database="cochesDb",username="Libreria",password="monkey1!")
    a=manager.Get5Orders("asc")
    print(a)
    #self.assertEqual(a,b)


testorders()