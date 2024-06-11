import dotenv from "dotenv";
import { GoogleGenerativeAI } from "@google/generative-ai";

dotenv.config();

const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);

let submit = document.getElementById('submit')
submit.addEventListener('submit', async function(event) {
    event.preventDefault();

    const place = document.getElementById('place').value;
    const budget = document.getElementById('budget').value;
    const people = document.getElementById('number-of-people').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const description = document.getElementById('activities').value;

    const prompt = `I am planning a trip to ${place}. My budget is ${budget} dollars for ${people} people. 
    The trip will start on ${startDate} and end on ${endDate}.Here is a brief description of activities they would like to do on trip: ${description}. 
    Please provide a detailed itinerary and recommendations as per my interest ans also recommend the hotels .`;

    // const response = await getGeminiResponse(prompt);
    // document.getElementsByClassName('response-content').innerText = response;

    console.log(prompt)
});

async function getGeminiResponse(prompt) { 
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
}


