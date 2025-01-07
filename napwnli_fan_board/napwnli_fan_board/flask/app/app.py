from flask import Flask, render_template, request, redirect, url_for, session, make_response
import os
from flask_mysqldb import MySQL
from hashlib import md5
import board_manager


app = Flask(__name__)

# Setting up database details
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'napwnli'
app.config['MYSQL_DB'] = 'napwnli_fan_board'

# Setting up session secret key
app.secret_key = 'napwnli_fan_board_secret_key'

blacklist = [';', '-', '\'', 'all', 'and', 'any', 'as', 'asc', 'avg', 'between', 'by', 'case', 'count', 'create', 'cross', 'database',  'delete', 'desc', 'distinct', 'drop', 'else', 'end', 'exists', 'false', 'from', 'group', 'having', 'in', 'inner',  'insert', 'is', 'join', 'left', 'like', 'limit', 'max', 'min', 'natural', 'not', 'null', 'on', 'or', 'order', 'outer',  'regexp', 'right', 'schema', 'select', 'some', 'sum', 'table', 'then', 'true', 'union', 'update', 'using', 'when',  'where', 'xor']
mysql = MySQL(app)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('board'))
    return render_template('index.html', data = board_manager.get_random_board_content())

@app.route('/login', methods=['GET'])
def login_template():
    if 'user' in session:
        return redirect(url_for('board'))

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    if 'user' in session:
        return make_response({"message" : "You are already logged in", "success" : False}, 500)

    username = request.form['username']
    password = request.form['password']

    for i in blacklist:
        if i in password.lower():
            password = password.replace(i, "")

        elif i in username.lower():
            username = username.replace(i, "")


    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'")
        user = cur.fetchone()
        cur.close()
    except Exception as e:
        return make_response({"message" : f"Login error: {e}"}, 500)

    if user:
        # Create a session
        session['user'] = user
        return make_response({"message" : "Login successful", "success" : True}, 200)
    else:
        return make_response({"message" : "Login failed", "success" : False}, 500)
    

@app.route('/register', methods=['GET'])
def register_template():
    if 'user' in session:
        return redirect(url_for('board'))
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():

    if 'user' in session:
        return make_response({"message" : "You are already logged in", "success" : False}, 500)

    username = request.form['username']
    password = request.form['password']

    if len(username) < 8 or len(password) < 8:
        return make_response({"message" : "Username and password must be at least 8 characters long"}, 500)

    if len(username) > 127 or len(password) > 127:
        return make_response({"message" : "Username and password must be at most 31 characters long"}, 500)
    
    for i in blacklist:
        if i in password or i in username:
            return make_response({"message" : f"Username and password cannot contain '{i}'! Don't try to hack me!!1!"}, 500)
    
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        mysql.connection.commit()
        cur.close()

        directory = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_name = md5(username.encode()).hexdigest()
        with open(os.path.join(directory, file_name), 'w') as f:
            f.write('')

    except Exception as e:
        return make_response({"message" : f"Registration error: {e}"}, 500)

    return make_response({"message" : "Registration successful", "success" : True}, 200)
    

@app.route('/board', methods=['GET'])
def board():
    if 'user' in session:
        id = request.args.get('id')
        #real_id = md5(session['user'][0].encode()).hexdigest()
        if id is None:# or id != real_id:
            id = md5(session['user'][0].encode()).hexdigest()
            return redirect(url_for('board', id=id))
        return render_template('board.html', data = board_manager.get_board_content(id))
    else:
        return redirect(url_for('index'))
    
@app.route('/save', methods=['POST'])
def save():
    if 'user' not in session:
        return make_response({"message" : "You are not logged in", "success" : False}, 500)

    id = md5(session['user'][0].encode()).hexdigest()
    content = request.form['content']
    if board_manager.save_board_content(id, content):
        return make_response({"message" : "Content saved", "success" : True}, 200)
    else:
        return make_response({"message" : "You can't overwrite a flag!", "success" : False}, 500)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    board_manager.initialize_board()
    app.run(debug=True, host='0.0.0.0')