from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
# from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/university'
db = SQLAlchemy(app)
# mysql = MySQL()


@app.route('/Augusta.com')
def homepage():
    return render_template('/university.html')

class Register(db.Model):
    reg_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    con_pass = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name=request.form.get('fname')
        phone=request.form.get('mnum')
        email=request.form.get('email')
        password=request.form.get('password')
        con_password=request.form.get('pass')
        gen=request.form.get('gen')

        entry=Register(name=name, phone=phone,email=email,password=password,con_pass=con_password,gender=gen)
        db.session.add(entry)
        db.session.commit()

    return render_template('/register.html')

@app.route('/login')
def signin():
    return render_template('/signin.html')

# @app.route('/Augusta.com/hostel')
# def hostel():
#     return render_template('/indexhostel.html')

# @app.route('/login/success/')
# def serve_login_success():
#     return 'login success'

# @app.route('/login/failure/')
# def serve_login_failure():
#     return 'login failure'


# @app.route('/indexhostel', methods=['GET','POST'])
# def complain():
#     if request.method == 'POST':
#         cursor = get_cursor()
#         name = request.form['full_name']
#         contact_no = request.form['no']
#         email = request.form['email']
#         father = request.form['f_name']
#         father_no = request.form['f_no']
#         mother = request.form['m_name']
#         mother_no = request.form['m_no']
#         attendance = request.form['attendance']
#         result = request.form['result']
#         dob = request.form['dob']
#         roll_no = request.form['roll_no']
#         category = request.form['cat']
#         income = request.form['income']
#         gender = request.form['gen']
#         current_year = request.form['year']
#         cursor.execute("INSERT INTO personal() VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,contact_no,email,father,father_no,mother,mother_no,attendance,result,dob,roll_no,category,income,gender,current_year))
#         connection.commit()
#         cursor.close()
#         return redirect(url_for('data'))
#     return render_template('indexhostel.html')


# @app.route('/login/auth/', methods = ['POST', 'GET'])
# def auth_login():
    
#     if request.method == 'POST':

#         username = request.form['username']
#         password = request.form['password']

#         if username == 'sajib' and password == 'password':
#             return redirect(url_for('serve_login_success'))
#         else:
#             return redirect(url_for('serve_login_failure'))

# @app.route('/certificate/<name>/<int:marks>/', methods = ['GET'])
# def serve_certificate(name, marks):
#     return render_template('certificate.html', name = name, marks = marks)

# @app.route('/routine')
# def serve_routine():
#     routine = { 'Physics': '10:00 am', 'Computer': '11:30 am', 'English': '2:30 pm' }
#     return render_template('routine.html', routine = routine)

# @app.route('/insert')
# def insert_db():

#     cursor = get_cursor()

#     cursor.execute("insert into ex1(col1, col2) values (%s, %s)", (26, "xyz"))
#     connection.commit()
#     cursor.close()

#     return "success"

# @app.route('/select')
# def select_db():

#     cursor = get_cursor()

#     cursor.execute("select * from ex1")
#     data = cursor.fetchall()
#     cursor.close()

#     return render_template('db_select.html', data = data)

# def get_cursor():
#     global connection
#     return connection.cursor()

if __name__ == '__main__':
    app.run(port = 8080, debug = True)