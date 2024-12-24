import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
# ===================================CREATE TABLE FOR EMPLOYEE PAGE======================================================================================================================================================
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,cnic text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
# ===================================CREATE TABLE FOR SUPPLIER PAGE======================================================================================================================================================

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()
    
# ===================================CREATE TABLE FOR CATEGORY PAGE======================================================================================================================================================

    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    
    
    
create_db()