from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
#create an instance of the mysql class
mysql = MySQL()
#add to the app (Flask object) some config data for our connection
app.config['MYSQL_DATABASE_USER'] = 'x'
app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
#The name of the database we want to connect to at the DB server
app.config['MYSQL_DATABASE_DB'] = 'restaurants_V2'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# user the mysql object's method "init_app" and pass it the flask object
mysql.init_app(app)

@app.route("/", methods=["GET"])
def index():
	
	# set up a cursor object which is what the sql object users to connect and run queries
	cursor = mysql.connect().cursor()
	# execute a query with the execute method
	cursor.execute("SELECT * FROM restaurant WHERE 1")
	# Turn the mysql object into something we can use	
	data = cursor.fetchall()
	if data is None:
		return "Your query returns no results"
	else:
		return render_template('rest.html',
			data = data)

@app.route("/restaurant/<id>")
def restaurant_info(id):
	# set up a cursor object which is what the sql object uses to connect and run queries
	cursor = mysql.connect().cursor()
	#execute a query with the execute method
	cursor.execute("select name, title, review, address, category, user_name, stars from review inner join restaurant on restaurant.id = review.restaurant_id inner join user on user.id = review.author_user_id where restaurant_id = %s" % id)
	data = cursor.fetchall()
	if data is None:
		return "Your query returns no results"
	else:
		print(data)
		return render_template('taurant.html',
			data = data)

if __name__ == "__main__":
	app.run(debug=True)