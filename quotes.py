from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Monday09@localhost/quotes'
#app.config['SQLALCHEMY_DATABASE_URI']='postgres://dqdasjgibihrfu:e91bfe3483b8988ac715abb3d4445a2e842abf1bcdc44221fc23879368fd10d7@ec2-3-231-46-238.compute-1.amazonaws.com:5432/d69c0jelktl1fm'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://cdtcemgacxxofp:9d5721d33e5eb20fdc191f2d5e0ed39704ab08f0c3039ead051f4b9aa3179620@ec2-54-246-90-10.eu-west-1.compute.amazonaws.com:5432/d9sa57fakvu6r7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Favquotes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))




@app.route('/')
def index():
	result = Favquotes.query.all()

	return render_template('index.html', result=result)

    
 

# Creating more endpoints
@app.route('/about')
def about():
    return '<h1>This is a simple guestbook application</h1>'


@app.route('/quotes')
def quotes():
	return render_template('quotes.html')

@app.route('/process', methods=['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']

	signature = Favquotes(author=author, quote=quote)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))



'''
if __name__ == '__main__':
    app.run(debug=True)
'''