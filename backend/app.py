from flask import Flask, render_template, request
from dotenv import load_dotenv

# from backend import routes
# from config import config


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
# app.config.from_object(Config)

# Initialize routes
# routes.init_routes(app)

@app.route('/')
def index():
        return render_template('index_itinerary.html')

@app.route('/submit', methods=['POST'])
def submit():
        if request.method == 'POST':
            # Retrieve form data
            place = request.form['place']
            startdate= request.form['startdate']
            enddate = request.form['enddate']
            people= request.form['people']
            budget = request.form['budget']
            activities = request.form['activities']

            # Process the data (e.g., store in a database, perform some logic, etc.)
            return f"Place: {place}, Start-Date: {startdate}, End-Date: {enddate}, No. of people: {people}, Budget: {budget}, Activities: {activities}"



if __name__ == '__main__':
    app.run(debug=True)
