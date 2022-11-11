
from flask import Flask, request, render_template
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

print(db)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String(100), nullable=False)
    quant = db.Column(db.Integer, nullable=False)
    meal_type = db.Column(db.String(80), nullable=False)

@app.route('/',methods = ['POST', 'GET'])

def index():
    try:
        meal = request.form['meal']
        no_of_meals = request.form['no_of_meals']
        type_of_meal = request.form['meal_type']
        
        with sql.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS meals (id INTEGER PRIMARY KEY AUTOINCREMENT, meal TEXT NOT NULL UNIQUE, quantity integer, type_of_meal text)" )
            
            cur.execute("INSERT INTO meals (meal, quantity, type_of_meal) VALUES (?,?,?)", (meal, no_of_meals, type_of_meal) )
            con.commit()
    except:
        con.rollback()
        
    finally:
        con = sql.connect("database.db")
        con.row_factory = sql.Row
   
        cur = con.cursor()
        cur.execute("select * from meals")
   
        rows = cur.fetchall();

        return render_template('index.html', rows = rows)
            



if __name__ == "__main__":
    db.create_all()
    app.run(host="127.0.0.1", port=8080, debug=True)