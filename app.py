from  flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

# Mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_contacts'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    return  render_template('index.html')

@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        fullname    = request.form['fullname']
        phone       = request.form['phone']
        email       = request.form['email']
        # Cursor created
        cur = mysql.connection.cursor()
        # Request
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)',
        (fullname, phone, email))
        # Aplly request
        mysql.connection.commit()
        flash('Contact Added successfully!')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)