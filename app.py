from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('username')

    # Fix: only apply .title() when name is not None
    if name:
        name = name.title()

    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
