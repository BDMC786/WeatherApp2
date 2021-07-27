from flask import Flask, request, render_template
#import getData ##FOR LOCAL
## from .getData import getWeather  ##FOR LIVE SITE
from my_modules import getweather_input , getweather_link

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html') 


@app.route('/', methods=['POST'])
def function():
    city = request.form['text']
    print(city)


    try:
        data = getweather_input(city) 
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/bayonne")
def bayonne():
    city = "Bayonne, NJ"
    print("Good to Here")
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/bayonne', methods=['POST'])
def bayonneFunction():
    city = request.form['text']

    

    try:
        data = getweather_input(city) 
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)


@app.route("/montclair")
def montclair():
    city = "Montclair, NJ"
    try:
        data = getweather_link(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/montclair', methods=['POST'])
def montclairFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)


@app.route("/new_york")
def NYC():
    city = "New York, NY"
    try:
        data = getweather_link(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/new_york', methods=['POST'])
def NYCFunction():
    city = request.form['text']

    try:
        data = getweather_input(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/culver_IN")
def Culver():
    city = "Culver, IN"
    try:
        data = getweather_link(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/culver_IN', methods=['POST'])
def CulverFunction():
    city = request.form['text']
    try:
        data = getweather_input(city) 
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/hightstown")
def Hightstown():
    city = "Hightstown, NJ"
    try:
        data = getweather_link(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/hightstown', methods=['POST'])
def HightstownFunction():
    city = request.form['text']
    try:
        data = getweather_input(city) 
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/atlanta")
def atlanta():
    city = "Atlanta, GA"
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/atlanta', methods=['POST'])
def atlantaFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/easton")
def easton():
    city = "Easton, PA"
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/easton', methods=['POST'])
def eastonFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)  
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)


@app.route("/disney")
def disney():
    city = "Magic Kingdom, Disney World, Florida"  
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/disney', methods=['POST'])
def disneyFunction():
    city = request.form['text']
    try:
        data = getweather_input(city) 
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/cranston")
def cranston():
    city = "Cranston, RI"
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route('/cranston', methods=['POST'])
def cranstonFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/w_ny")
def westNY():
    city = "West New York, NJ"
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/w_ny", methods=['POST'])
def westNYFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/warren_township")
def warren_twnshp():
    city = "Warren Township, NJ"
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/warren_township", methods=['POST'])
def warren_twnshpFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/lincoln_park")
def lincoln_park():
    city = "Lincoln Park, NJ"
    try:
        data = getweather_link(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

@app.route("/lincoln_park", methods=['POST'])
def lincoln_parkFunction():
    city = request.form['text']
    try:
        data = getweather_input(city)
    except:
        return render_template("error.html")

    return render_template('results.html', data = data)

    


if __name__=='__main__':
    app.run() #
