import pyodbc


class DBFuncs:
    def __init__(self):
        self.conn = pyodbc.connect(r"************************************")
        self.cursor1 = self.conn.cursor()
        self.cursor2 = self.conn.cursor()
        self.cursor3 = self.conn.cursor()
        self.cursor4 = self.conn.cursor()

    def select(self, table: str):
        """Selects a table for the database to grab data"""
        data = self.cursor1.execute(f"SELECT * from {table}")
        data = data.fetchall()
        return data

    def insert(self, table: str, **args):
        """Inserts a new document into the SQL Database"""
        try:
            print(args)
            allarg = ""
            allvalue = ""
            for i in args:
                allarg += f"{i} "
                allvalue += f"'{args[i]}' "
            else:
                allarg = allarg.strip().replace(' ', ",")
                allvalue = allvalue.strip().replace(' ', ", ")
            self.cursor2.execute(f"INSERT INTO {table} ({allarg}) VALUES({allvalue})")
            self.cursor2.commit()
            return
        except Exception as e:
            print(e)
            raise Exception("Error while using INSERT")

    def overwrite(self, table: str, column: str, column2: str, verifier, newdata):
        """Overwrites any data in the current query! Use Carefully."""
        # verifier is the info in column2
        # column 2 is the criteria is checked
        try:
            self.cursor3.execute(f"""UPDATE {table} SET {column} = '{newdata}' WHERE [{column2}] = '{verifier}'""")
            self.cursor3.commit()
        except Exception:
            raise Exception("Error while using OVERWRITE")

    def update(self, table: str, column: str, olddata, newdata):
        """Update (APPENDING) a query to the SQL database"""
        lst = []
        new = ""
        try:
            info = self.cursor4.execute(f"SELECT * from {table}")
            for i in info:
                lst = i[2].split(", ")
                if '' == lst[-1]:
                    lst.remove(lst[-1])
                    lst.append(newdata)
                else:
                    lst.append(newdata)
                break

            for i in lst:
                new += f"{i}, "
            self.cursor4.execute(f"UPDATE {table} SET {column} = '{new}' WHERE {column} = '{olddata}'")
            self.cursor4.commit()
        except Exception as e:
            print(e)
            raise Exception("Error while using UPDATE")
