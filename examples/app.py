from flask import Flask
from flask_mysqlcnx import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database'

mysql = MySQL(app)


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)


if __name__ == '__main__':
    app.run(debug=True)
