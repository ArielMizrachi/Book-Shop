from flask import Flask, render_template
import database

database.Base.metadata.create_all(database.engine)

from customer_bluprint import customer
from loan_bluprint import loan
from book_bluprint import book

app = Flask(__name__)
app.register_blueprint(book)
app.register_blueprint(customer)
app.register_blueprint(loan)

@app.route('/')
def hello():
    return render_template ('main.html')



if __name__ == '__main__':
    
    app.run(debug=True) 