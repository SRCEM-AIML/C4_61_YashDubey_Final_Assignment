from flask import Flask, render_template, request, flash, redirect, url_for # type: ignore

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for flashing messages

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = None
    age = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        # Basic validation
        if not name or not age:
            flash('Name and age are required.', 'error')
        elif not age.isdigit() or int(age) <= 0:
            flash('Age must be a positive number.', 'error')
            age = None # Clear invalid age so it doesn't display
        else:
            # Valid input, render with greeting
            return render_template('form.html', name=name, age=age)
        # Invalid input or GET request, render form possibly with errors
        return render_template('form.html', name=name, age=age)

    # Initial GET request
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)