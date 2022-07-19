from flask import Flask, render_template

# create an app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/addstud',methods =['POST','GET'])
def add():
    if request.method =='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cwd = request.form['cwd']
        phone = request.form['phone']
        dob = request.form['dob']

        # above we captured the details from the form
        # Next we save to the database

        connection = pymysql.connect(host='localhost', user='root', password='', database='mind_db')

        # we now do an insert sql query
        sql = "insert into students(firstname, lastname, username, email, password, cwd, phone, dob)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

        # run above sql, you run sql using cursor
        cursor = connection.cursor()
        # run/execute sql and provide the values


        cursor.execute(sql, (firstname, lastname, username, email, password, cwd, phone, dob))
        connection.commit()
        return render_template('addstud.html', message= "Record Saved Successfully, Thank you.")




    else:
        # we pause, then we go create a template for add.html
        return render_template('addstud.html')



@app.route("/viewstud")
def view_students():
    connection = pymysql.connect(host='localhost', user='root', password='', database='mind_db')
    sql = "select * from students"

    # create cursor
    cursor = connection.cursor()

    # execute sql using the cursor
    cursor.execute(sql)

    # you check are there any  patients
    if cursor.rowcount == 0:
        return render_template('viewstud.html', message = "No students, Please navigate to add student page")

    else:
        # here means there are patients, fetch all
        rows = cursor.fetchall()
        return render_template('viewstud.html', rows = rows)



from flask import request
import pymysql
@app.route('/addment', methods=['POST','GET'])
def mentors():
    if request.method =='POST':
        firstname = request.form['firstname']
        lastname= request.form['lastname']
        email = request.form['email']
        password= request.form['password']

        connection = pymysql.connect(host='localhost', user='root', password='', database='mind_db')

        sql="insert into mentors(firstname,lastname,email,password) VALUES(%s,%s,%s,%s)"

        cursor = connection.cursor()

        cursor.execute(sql,(firstname,lastname,email,password))

        connection.commit()
        return render_template('addment.html', message= "Record Saved Successfully, Thank you.")


    else:
        return render_template('addment.html')



@app.route('/viewment')
def view_mentors():
    connection = pymysql.connect(host='localhost', user='root', password='', database='mind_db')

    sql = "select * from mentors"
    # create cursor
    cursor = connection.cursor()

    # execute sql using the cursor
    cursor.execute(sql)

    # you check are there any  mentors
    if cursor.rowcount == 0:
        return render_template('viewment.html', message = "No mentors, Please navigate to add mentor page")

    else:
        # here means there are patients, fetch all
        rows = cursor.fetchall()
        return render_template('viewment.html', rows = rows)


# create dummy domain(double underscores)
if__name__ = '__main__'
app.run()
