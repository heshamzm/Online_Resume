from flask import Flask, render_template, url_for, request, redirect
import random 

myapp = Flask(__name__)

me = {
	"first_name":"Reema",
	"last_name":"Eilouti",
	"description": "",
	"social_links": [
			{"site":"Twitter","url":"https://twitter.com/ReemaEilouti"}, 
			{"site": "GitHub", "url": "https://github.com/reema-eilouti"},
			{"site": "LinkedIn", "url": "https://linkedin.com/in/reema-eilouti"}
	],
	"age": 25,
	"email": "reema.eilouti@gmail.com",
	"skills": [{"number": "1","course" : "Python","year":"2020","uni":"htu"},
				{"number": "2","course" : "javascript","year":"2019","uni":"Philadelphia"},
				{"number": "3","course" : "HTML","year":"2018","uni":"Philadelphia"},
				{"number": "4","course" : "flask","year":"2020","uni":"htu"}
				],
	"projects": [
		{"name":"Tic-Tac-Toe", "description":"A description for the project.", "tags":["functions", "control structures", "game"]},
		{"name":"Battle of Teams", "description":"A description for the project.", "tags":["functions", "OOP"]},
		{"name":"Resume", "description":"A description for the project.", "tags":["flask", "web application", "HTTP routes"]}
	],
	"favourite_quotes": [
		{"quote":"Hasta la vesta baby", "author":"Terminator"},
		{"quote":"Say hello to my lettle friend", "author":"Tony Montana"},
		{"quote":"You talkin to me?", "author":"someone3"}
	]
}

@myapp.route('/')
def home():
    menu = [
        {"title":"About Me", "url":url_for("about_me")},
        {"title":"Skills", "url":url_for("skills")},
        {"title":"Projects", "url":url_for("projects")},
        {"title":"Quotes", "url":url_for("quotes")}
        ]
    return render_template("home.html", menu = menu, me = me, image1 = url_for('static', filename='images/python_logo.png'))

@myapp.route('/me')
def about_me():
	return render_template("me.html", me = me, go_home = url_for("home"), pic = url_for('static', filename='images/hesham.jfif'))


@myapp.route('/editme', methods=["GET", "POST"])
def edit_me():
	if request.method == 'GET':
		return render_template("editme.html")
	else:
		age = int(request.form['age'])   
		email = request.form['email']
		# change values in dictionary
		me['age']= age
		me['email']= email
		return redirect(url_for("about_me"))


@myapp.route('/add_quote', methods=["GET", "POST"])
def add_quote():
	if request.method == 'GET':
		return render_template("add_quote.html")
	else:
		newquote = request.form['newquote']
		newauthor = request.form['newauthor']
		me['favourite_quotes'].append({'quote':newquote,'author':newauthor})
		return redirect(url_for("quotes"))

@myapp.route('/del_quote', methods=["GET", "POST"])
def del_quote():
	if request.method == 'GET':
		return render_template("del_quote.html", me = me)
	else:
		quotenumber = int(request.form['quotenumber'])
		me['favourite_quotes'].pop(quotenumber)
		return redirect(url_for("quotes"))

		
@myapp.route('/skills')
def skills():
    return render_template("skills.html", me = me, go_home = url_for("home"))

@myapp.route('/projects')
def projects():
    return render_template("projects.html", me = me, go_home = url_for("home"))

@myapp.route('/quotes')
def quotes():
	#random quote

	# the_quotes_list = me.get("favourite_quotes")
	# the_quote = random.choice(the_quotes_list)

	return render_template("quotes.html", go_home = url_for("home"), me = me)
	# favourite = the_quote