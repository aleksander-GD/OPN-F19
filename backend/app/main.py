from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error, errorcode
import logging
import json
import hashlib

app = Flask(__name__)
    
def dbConnection():
    connection = mysql.connector.connect(host='database',
                                         database='person',
                                         user='root',
                                         password='')
    return connection

#@app.route('/')
#def index():
#    return 'Index page of the backend'
#

@app.route("/person", methods=['POST'])
def person():
    
    db = dbConnection()
    cursor = db.cursor()
    
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    
    sqlInsert = "INSERT INTO personTable (firstname, lastname) VALUES (%s, %s)"
    value = (firstname, lastname)
    cursor.execute(sqlInsert, value)
    try:
        db.commit()
        return "%s:%d:%s" % ("OK",cursor.rowcount,"record inserted.")
        
        
    except mysql.connector.Error as error:
        logging.warn("Failed to insert values %s, %s", firstname, lastname)
        return str(error)
        
    finally:
        if (db.is_connected()):
            db.close()
            cursor.close()
            print("MySQL connection is closed")
            
@app.route('/persons', methods=['GET'])
def persons():
    db = dbConnection()
    
    cursor = db.cursor()
    
    sqlSelect = "SELECT * FROM personTable"
    
    try:
        row_count = cursor.execute(sqlSelect)
        result = cursor.fetchall()
        if row_count == 0:
            print("No results fetched from database")
        else:
            payload = []
            content = {}
            for data in result:
                personID = data[0]
                firstname = data[1]
                lastname = data[2]
                
                content = {'Firstname': firstname,
                            'PersonID': personID, 
                            'Lastname': lastname
                            }
                payload.append(content)
                #content = {}
            return jsonify(payload)
            
    except mysql.connector.Error as error:
        print(error)
    finally:
        if (db.is_connected()):
            db.close()
            cursor.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    app.run(host='0.0.0.0')