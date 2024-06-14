import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import markdown2


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

        
            prompt = f'''I am planning a trip to ${place}. My budget is ${budget} rupees for ${people} people. 
                        The trip will start on ${startdate} and end on ${enddate}.Here is a brief description of activities 
                        they would like to do on trip: ${activities}. Please provide a detailed itinerary and recommendations 
                        as per my interest and also recommend the hotels and way to transport to the place and within the place . '''

            response = model.generate_content(prompt)
            markdown_content = response.text
            itinerary_data = markdown2.markdown(markdown_content)

            itinerary_code = model.generate_content(f'''{itinerary_data}. I already have a code for my page and want to add this data
                                                     in the middle of it. please provide only div code and add its css within div so that 
                                                    I can add it to my existing code. provide only code no further information''')
            
            return render_template('index_itinerary.html', itinerary_code=itinerary_code.text)
        return render_template('index_itinerary.html')



if __name__ == '__main__':
    app.run(debug=True)
