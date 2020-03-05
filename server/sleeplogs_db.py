import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor, description):
        d[col[0]] = row[idx]
    return d

class SleepLogDB:
    def __init__(self):
        self.connnection = sqlite3.connect("sleeplogs.db")
        self.connnection.row_factory = dict_factory
        self.cursor = self.connnection.cursor()

    def insertSleepLog(self,day,hours,e,expected,actual,mood,notes):
        data = [day,hours,e,expected,actual,mood,notes]
        self.cursor.execute("INSERT INTO sleeplogs (day, hours, phone, late, mood) VALUES (?,?,?,?,?)", data)
        self.connnection.commit()

    def getAllSleeplogs(self):
        self.cursor.execute("SELECT * FROM sleeplogs")
        sleeplogs = self.cursor.fetchall()

    def getOneSleeplog(self, log_id):
        data = [log_id]
        self.cursor.execute("SELECT * FROM restuarant WHERE id = ?", data)
        return self.cursor.fetchone()
