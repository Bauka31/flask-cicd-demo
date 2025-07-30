from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return render_template('contact.html', submitted=True, name=name, message=message)
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
