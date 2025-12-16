from flask import Flask,render_template

app = Flask(__name__) 

@app.route('/')
def index():
    tiile = 'Home Page'
    return render_template('index.html', title=tiile)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'piaporn silsart'
    email = 'std.67122420229@ubru.ac.th'
    mobile = '0979545891'
    age = 20
    return render_template('about.html', title=title, name=name, email=email, mobile=mobile, age=age)
  
@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods'
    foods = ['Pizza', 'Sushi', 'Ice Cream']
    return render_template('favorite_foods.html', title=title, foods=foods)
    
@app.route('/favorite/sports')
def favorite_sports():
    title = 'Favorite Sports'
    sports = ['ว่ายนํ้า', 'ฟุตบอล', 'วอลเล่ย์บอล']
    return render_template('favorite_sports.html', title=title, sports=sports)

@app.route('/favorite/movies')
def favorite_movies():
    title = 'Favorite movies'
    movies = ['สัปเหร่อ', 'นางอาย', 'ธี่หยด','ข้างบ้าน','เดอะฮัก']
    return render_template('favorite_movies.html', title=title, movies=movies)