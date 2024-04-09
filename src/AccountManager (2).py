
import random
import sqlite3

class AccountManager:
    
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        with self.conn:
            self.conn.execute("create table users (username text, password text, userid integer primary key, admin integer)")
    
    def verifyUser(self, uname, passwd ):
        if type(uname) != str or type(passwd) != str:
            raise RuntimeError("Not a string")
        cur = self.conn.execute("select userid from users where username=:uname and password=:passwd",
            {"uname":uname, "passwd":passwd}
        )
        L = cur.fetchall()
        return len(L) == 1
    
    def addUser(self, uname, passwd):
        if type(uname) != str or type(passwd) !=  str:
            raise RuntimeError("Not a string")
        if len(uname) == 0 or len(passwd) == 0:
            return False
        if self.getUID(uname) != None:
            return False
        with self.conn:
            self.conn.execute("insert into users (username,password,admin) values ( :uname, :passwd, 0 )",
                {
                    "uname":uname,
                    "passwd":passwd,
                }
            )
        return True
     
    def getUID(self,username):
        if type(username) != str:
            raise RuntimeError("Not a string")
        cur = self.conn.execute("select userid from users where username=:uname",
            {"uname":username}
        )
        L = cur.fetchall()
        if len(L) != 1:
            return None
        return L[0]["userid"]
    
    def isAdmin(self,userid):
        if type(userid) != int:
            raise RuntimeError("Not an int")
        cur = self.conn.execute("select admin from users where userid=:userid",
            {"userid":userid}
        )
        L = cur.fetchall()
        if len(L) != 1:
            return False
        return (L[0]["admin"] == 1)

    def setAdmin(self,userid,isAdmin):
        if type(userid) != int:
            raise RuntimeError("Not an int")
        if type(isAdmin) != bool:
            raise RuntimeError("Not a bool")
        with self.conn:
            cur = self.conn.execute("update users set admin=:val where userid=:userid",
                { "val":1 if isAdmin == True else 0,
                  "userid":userid
            })
            L=cur.fetchall()      #ensure row count has been updated
            return cur.rowcount == 1
