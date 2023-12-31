from flask import Flask, render_template, request
import string
import random

password_generator = Flask(__name__)

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@password_generator.route('/', methods=['GET', 'POST'])
def index():
    generated_password = ''
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        include_symbols = 'include_symbols' in request.form
        generated_password = generate_password(password_length, include_symbols)
    return render_template('password_generator.html', generated_password=generated_password)

if __name__ == '__main__':
    password_generator.run(debug=True)
