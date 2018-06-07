from flask import Flask
from flask import render_template
from flask import request
from flask import redirect,url_for

from block import write_block

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']
        write_block(name=lender, amount=amount , to=borrower)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/checking')
def check():
    pass
if __name__ == '__main__':
    app.run(debug=True)