from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        input1 = request.form.get('input1')
        input2 = request.form.get('input2')
        input3 = request.form.get('input3')
        input4 = request.form.get('input4')
        result = f"Received: {input1}, {input2}, {input3}, {input4}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
