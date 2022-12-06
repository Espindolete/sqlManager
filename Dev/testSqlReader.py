import unittest
from sqlManagerLib.SqlReader import sqlManager

class sqlTester(unittest.TestCase):
    def testOffices(self):
        record=dict()
        
        record["city"]="uno"
        record["phone"]="dos"
        manager=sqlManager(server="localhost",database="cochesDb",username="Libreria",password="monkey1!")
        manager.insertOffice(record)



def testorders(self):
    manager=sqlManager(server="localhost",database="cochesDb",username="Libreria",password="monkey1!")
    a=manager.Get5Orders()
    print(a)
    b=[('10100', '2003-01-06', '2003-01-13', '2003-01-10', 'Shipped', 'NULL', '363'), ('10101', '2003-01-09', '2003-01-18', '2003-01-11', 'Shipped', 'Check on availability.', '128'), ('10102', '2003-01-10', '2003-01-18', '2003-01-14', 'Shipped', 'NULL', '181'), ('10103', '2003-01-29', '2003-02-07', '2003-02-02', 'Shipped', 'NULL', '121'), ('10104', '2003-01-31', '2003-02-09', '2003-02-01', 'Shipped', 'NULL', '141')]
    print(a==b)
    #self.assertEqual(a,b)
   
unittest.main()