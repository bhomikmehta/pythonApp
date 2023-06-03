from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os
import MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQL_DATABASE']
mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET'])
def get_users():
    users = []
    try:
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        for (id, name, email) in cursor:
            users.append({'id': id, 'name': name})
        mysql.connection.commit()
        cursor.close()
    except MySQLdb.OperationalError as e:
        error_message = str(e)
        if "Can't connect to MySQL server" in error_message:
            return jsonify({'error': 'Failed to connect to MySQL server'})
        else:
            return jsonify({'error': 'An error occurred while retrieving users'})
    return jsonify({'users': users})


@app.route('/users', methods=['POST'])
def create_user():
    try:
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (request.json['name'], request.json['email'])
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'User created successfully'})
    except MySQLdb.OperationalError as e:
        return jsonify({'error': 'Failed to connect to MySQL server'})


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        val = (request.json['name'], request.json['email'], id)
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'User updated successfully'})
    except MySQLdb.OperationalError as e:
        return jsonify({'error': 'Failed to connect to MySQL server'})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "DELETE FROM users WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()
        return "Done!!"
    except MySQLdb.OperationalError as e:
        return jsonify({'error': 'Failed to connect to MySQL server'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)