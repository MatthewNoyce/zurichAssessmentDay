"""
Flask backend server for life insurance application form.
Receives form data via POST request and saves it as a JSON file.
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime
from bmi_calculator import BMICalculator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

@app.route('/submit-complete', methods=['POST'])
def submit_complete():
    """
    Handle complete application submission endpoint.
    Receives all form data combined, saves it to a single JSON file, and returns success response.
    """
    try:
        # Get JSON data from the request
        complete_application = request.get_json()
        
        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'life_insurance_application_complete_{timestamp}.json'
        
        # Save the JSON data to a file in the current directory
        with open(filename, 'w') as f:
            json.dump(complete_application, f, indent=2)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Complete application saved successfully',
            'filename': filename
        }), 200
        
    except Exception as e:
        # Return error response if something goes wrong
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    """
    Calculate BMI from height and weight.
    Receives JSON with height_cm and weight_kg, returns BMI calculation.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        height_cm = data.get('height_cm')
        weight_kg = data.get('weight_kg')
        
        # Validate inputs
        is_valid, error_message = BMICalculator.is_valid_input(height_cm, weight_kg)
        if not is_valid:
            return jsonify({
                'status': 'error',
                'message': error_message
            }), 400
        
        # Calculate BMI
        result = BMICalculator.calculate(float(height_cm), float(weight_kg))
        
        # Return success response with BMI data
        return jsonify({
            'status': 'success',
            'data': result
        }), 200
        
    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Unexpected error: {str(e)}'
        }), 500

@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/styles.css')
def styles_css():
    """Serve the stylesheet from the project root."""
    return send_file(os.path.join(BASE_DIR, 'styles.css'))

@app.route('/personal.html')
def personal():
    """Serve the personal information page."""
    return send_file(os.path.join(BASE_DIR, 'personal.html'))

@app.route('/health.html')
def health():
    """Serve the health history page."""
    return send_file(os.path.join(BASE_DIR, 'health.html'))

@app.route('/lifestyle.html')
def lifestyle():
    """Serve the lifestyle history page."""
    return send_file(os.path.join(BASE_DIR, 'lifestyle.html'))

@app.route('/financial.html')
def financial():
    """Serve the financial information page."""
    return send_file(os.path.join(BASE_DIR, 'financial.html'))

if __name__ == '__main__':
    # Run the Flask development server
    # host='0.0.0.0' makes it accessible from other devices on the network
    # port=5000 is the default Flask port
    # debug=True enables auto-reload and detailed error messages
    app.run(host='0.0.0.0', port=5000, debug=True)
