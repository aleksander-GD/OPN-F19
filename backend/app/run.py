from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
def dbConnection():
    config = {
        'user': 'root',
        'password': '',
        'host': 'database',
        'port': '3306',
        'database': 'person'
    }
    connection = mysql.connector.connect(**config)
    return connection

@app.route('/')
def index():
    return 'Index page'


@app.route("/person/insert.html", methods=["POST"])
def insertPerson(firstname, lastname):
    
    #db = mysql.connector.connect(host="localhost")
    db = dbConnection()
    cursor = db.cursor()
    
    firstname = request.values.get('firstname')
    lastname = request.values.get('lastname')
    
    sqlInsert = "INSERT INTO person (firstname, lastname) VALUES (%s, %s)"
    value = (firstname, lastname)
    cursor.execute(sqlInsert, value)
    
    db.commit()
    
    print(cursor.rowcount, "record inserted.")
    
    db.close()
    
@app.route('/persons/select.html', methods=["GET"])
def selectPersons():
    db = dbConnection()
    
    cursor = db.cursor()
    
    sqlSelect = "SELECT * FROM person"
    cursor.execute(sqlSelect)
    
    result = cursor.fetchall()
    
    
    db.close()
    return json.dumps(result)