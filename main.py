from flask import Flask, render_template,request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///order.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)


class Order(db.Model):
    sno = db.Column(db.Integer, primary_key= True)
    medicine_name = db.Column(db.String(200), nullable = False)
    quantity = db.Column(db.Integer)
    contact =db.Column(db.Integer)
    address= db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"




@app.route("/")
def homlogin():
    return render_template("login.html")
    
@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/home")
def home():
    return render_template("home.html")

database={'shivanshmehta2003@gmail.com':'123', 'srijankoshti0000':'456'}

@app.route("/login_validation", methods=['POST', 'GET'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    
    if email not in database:
        return render_template('login.html', info ="invalid email please check")

    else:
        if database[email]!= password:
            return render_template('login.html', info="invalid password, please check")

        else:
            return render_template('home.html')


@app.route('/logout')
def logout():
    return redirect('/')

@app.route("/order", methods=['GET','POST'])
def order():
    if request.method=="POST":
        medicine_name= request.form['medicine_name']
        quantity= request.form['quantity']
        contact=request.form['contact']
        address = request.form['address']
        order= Order(medicine_name=medicine_name, quantity=quantity, contact=contact, address=address)
        db.session.add(order)
        db.session.commit()
    
    return render_template('order.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)