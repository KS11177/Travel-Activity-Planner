import requests
from flask import request, jsonify, Flask # Adjust import as necessary
#from backend.utils import load_json_data  # Adjust import as necessary
import openai

users = {}

def init_routes(app):
    def get_maps():
        location = request.args.get('location')
        api_key = app.config['GOOGLE_MAPS_API_KEY']
        maps_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
        response = requests.get(maps_url)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"message": "Error fetching maps data"}), response.status_code

    def get_directions():
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        api_key = app.config['GOOGLE_MAPS_API_KEY']
        directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
        response = requests.get(directions_url)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"message": "Error fetching directions data"}), response.status_code
