from  flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from numpy import MAY_SHARE_BOUNDS


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
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return  render_template('index.html', contacts = data)

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

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

    