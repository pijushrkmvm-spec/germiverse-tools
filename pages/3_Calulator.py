from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        operation = request.form.get('operation', 'add')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error'

        return render_template('calculator.html', result=result)

    return render_template('calculator.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
