from flask import Flask,render_template


import pymysql

con=None
cur=None

def connectToDb():
    global con,cur
    con=pymysql.connect(host="localhost",user="root",password="",database="cricket")
    
    cur=con.cursor()

def disconnectToDb():
    cur.close()
    con.close()

def getAllLapdata():
    connectToDb()
    selectquery="SELECT * from rankingsinfo;"
    cur.execute(selectquery)
    data=cur.fetchall()
    disconnectToDb()
    return data

def getAllLapdata1():
    connectToDb()
    selectquery="SELECT * from femalerankingsinfo;"
    cur.execute(selectquery)
    data1=cur.fetchall()
    disconnectToDb()
    return data1   

app=Flask(__name__)

@app.route('/')
def first():
    return render_template("first.html")

@app.route("/second")

def index():
    data=getAllLapdata()
    return render_template("index.html",data=data)

@app.route("/search/", methods=['GET','POST'])

def onerecordm():
    return render_template("search.html")

def getoneTeam(Teams):
    connectToDb()
    selectquery="SELECT * fron rankingsinfo where Teams=%s;"
    cur.execute(selectquery,(Teams,))
    data=cur.fetchone()
    disconnectToDb
    return data


@app.route("/third")

def index2():
    
    data1=getAllLapdata1()

    return render_template("index2.html",data1=data1)

@app.route("/search2/", methods=['GET','POST'])

def onerecordf():
    return render_template("search2.html")



def getoneTeam(Teams):
    connectToDb()
    selectquery="SELECT * fron femalerankingsinfo where Teams=%s;"
    cur.execute(selectquery,(Teams,))
    data1=cur.fetchone()
    disconnectToDb
    return data1


if __name__=='__main__':
    app.run(debug=True)   





