import pyodbc


driver = "{ODBC Driver 17 for SQL Server}"


class sqlManager:
    def __init__(self, server, database, username, password):
        self.cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='\
                                    +server+';DATABASE='+database+';ENCRYPT=no;UID='\
                                    +username+';PWD='+ password+";Trust Server Certificate=yes")
        self.cursor=self.cnxn.cursor()

    def Get5Orders(self):
        return self.cursor.execute("select * from dbo.orders").fetchmany(5)
    
    def insertOffice(self,myDict:dict):
        placeholders = ', '.join(['%s'] * len(myDict))
        columns = ', '.join(myDict.keys())
        for x,y in myDict.items():
            try:
                int(y)
                myDict[x]=y
            except ValueError:
                myDict[x]="\'"+y+"\'"

        values=','.join(myDict.values())
        print(values)
        sql = "INSERT INTO dbo.offices ( %s ) VALUES ( %s )"\
                % (columns, values)

        print(sql)
        self.cursor.execute(sql)
        self.commit()

    def commit(self):
        self.cnxn.commit()
