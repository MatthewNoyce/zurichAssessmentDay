"""
Flask backend server for life insurance application form.
Receives form data via POST request and saves it as a JSON file.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
# Enable CORS to allow requests from the HTML file
CORS(app)

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handle form submission endpoint.
    Receives JSON data, saves it to a file, and returns success response.
    """
    try:
        # Get JSON data from the request
        form_data = request.get_json()
        
        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'life_insurance_application_{timestamp}.json'
        
        # Save the JSON data to a file in the current directory
        with open(filename, 'w') as f:
            json.dump(form_data, f, indent=2)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Application saved successfully',
            'filename': filename
        }), 200
        
    except Exception as e:
        # Return error response if something goes wrong
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/submit-health', methods=['POST'])
def submit_health():
    """
    Handle health form submission endpoint.
    Receives JSON data, saves it to a file, and returns success response.
    """
    try:
        # Get JSON data from the request
        health_data = request.get_json()
        
        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'health_history_{timestamp}.json'
        
        # Save the JSON data to a file in the current directory
        with open(filename, 'w') as f:
            json.dump(health_data, f, indent=2)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Health history saved successfully',
            'filename': filename
        }), 200
        
    except Exception as e:
        # Return error response if something goes wrong
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/submit-lifestyle', methods=['POST'])
def submit_lifestyle():
    """
    Handle lifestyle form submission endpoint.
    Receives JSON data, saves it to a file, and returns success response.
    """
    try:
        # Get JSON data from the request
        lifestyle_data = request.get_json()
        
        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'lifestyle_history_{timestamp}.json'
        
        # Save the JSON data to a file in the current directory
        with open(filename, 'w') as f:
            json.dump(lifestyle_data, f, indent=2)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Lifestyle history saved successfully',
            'filename': filename
        }), 200
        
    except Exception as e:
        # Return error response if something goes wrong
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/')
def index():
    """Serve the main HTML page."""
    return app.send_static_file('index.html')

@app.route('/health.html')
def health():
    """Serve the health history page."""
    return app.send_static_file('health.html')

@app.route('/lifestyle.html')
def lifestyle():
    """Serve the lifestyle history page."""
    return app.send_static_file('lifestyle.html')

if __name__ == '__main__':
    # Run the Flask development server
    # host='0.0.0.0' makes it accessible from other devices on the network
    # port=5000 is the default Flask port
    # debug=True enables auto-reload and detailed error messages
    app.run(host='0.0.0.0', port=5000, debug=True)
