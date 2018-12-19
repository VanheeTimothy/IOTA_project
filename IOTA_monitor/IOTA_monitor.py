from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def analytics():
    return render_template('Analytics.html')

@app.route('/transactions')
def transactions():
    return render_template('Transactions.html')

@app.route('/settings')
def settings():
    return render_template('Settings.html')




if __name__ == '__main__':
    app.run(debug=True)
