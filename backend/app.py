import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import markdown2


# from config import config
# app.config.from_object(Config)

load_dotenv()
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')


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
        #     return f"Place: {place}, Start-Date: {startdate}, End-Date: {enddate}, No. of people: {people}, Budget: {budget}, Activities: {activities}"
        
            prompt = f'''I am planning a trip to ${place}. My budget is ${budget} rupees for ${people} people. 
                        The trip will start on ${startdate} and end on ${enddate}.Here is a brief description of activities 
                        they would like to do on trip: ${activities}. Please provide a detailed itinerary and recommendations 
                        as per my interest ans also recommend the hotels . '''

            response = model.generate_content(prompt)
            markdown_content = response.text
            itinerary_data = markdown2.markdown(markdown_content)

            return render_template('index_itinerary.html', itinerary_data=itinerary_data)
        return render_template('index_itinerary.html')



if __name__ == '__main__':
    app.run(debug=True)
