from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/algorithm')
def alg():
	def shorty(list):
		list = sorted(list) #init the list in sorted order
		list.pop(0)
		list.pop(len(list)-1)
		print sum(list)/len(list)	
	return str(shorty([1, 2, 3, 4, 100]))
	# shorty([1, 1, 5, 5, 10, 8, 8, 7])
	# shorty([-10, -4, -2, -4, -2, 0])

@app.route('/login')
def login():
	return render_template('login.html',
		name = "Rob",
		title = "American Ninja Warrior",
		a_list = [1,2,5,3,9],
		a_dict = {
			'boy1': "Mike TV",
			'boy2': "Augustus Gloop"
		},
		wannabetitle = "Willy Wonka")

@app.errorhandler(404)
def page_missing(e):
	print e
	return redirect('/')

@app.route('/user/<user_name>')
def user_page(user_name):
	return "user %s" % user_name

if __name__ == "__main__":
	app.run(debug=True)

