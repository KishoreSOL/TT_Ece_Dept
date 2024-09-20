from flask import Flask, request, redirect, url_for, render_template, session
from pymongo import MongoClient
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Replace with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017/")
db = client['ECE_DPT']
student_collection = db['students']
teacher_collection = db['teachers']



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')

        collection = teacher_collection if user_type == 'teacher' else student_collection

        user = collection.find_one({'email': email})
        if user and user['password'] == password:
            session['user'] = email
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials', 401

    return render_template('login.html')

@app.route('/onduty', methods=['GET'])
def onduty():
    return render_template('ondutystudent.html')


@app.route('/preodform', methods=['GET', 'POST'])
def preodform():
    if request.method == 'POST':
        register_number = request.form.get('register_number')
        name = request.form.get('name')
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        time_from = request.form.get('time_from')
        time_to = request.form.get('time_to')
        purpose = request.form.get('purpose')
        event_name = request.form.get('event_name')
        venue = request.form.get('venue')
        class_advisor = request.form.get('class_advisor')
        
        data = {
            'register_number': register_number,
            'name': name,
            'date_from': date_from,
            'date_to': date_to,
            'time_from': time_from,
            'time_to': time_to,
            'purpose': purpose,
            'event_name': event_name,
            'venue': venue,
            'class_advisor': class_advisor
        }
        
        student_collection.insert_one(data)
        return redirect(url_for('onduty'))
    
    return render_template('form.html')


@app.route('/getstudentpreoddetails', methods=['GET', 'POST'])
def getstudentpreoddetails():
    students = list(student_collection.find())
    return render_template('studentpreodlist.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)

