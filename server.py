from flask import Flask,render_template

app = Flask(__name__) 

@app.route('/')
def index():
    tiile = 'Home Page'
    return render_template('index.html', tiile=tiile)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'piaporn silsart'
    email = 'std.67122420229'@ubru.ac.th'
    mobile = '0979545891'
    return render_template('about.html', title=title, name=name, email=email, mobile=mobile age=age)
  
@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods'
    foods = ['Pizza', 'Sushi', 'Ice Cream']
    return render_template('favorite_foods.html', title=title, foods=foods)