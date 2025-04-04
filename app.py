from flask import Flask, render_template, request
from decision_rules import get_farm_advice  # Assuming the decision rules are in this module
import sqlite3

app = Flask(__name__)

def save_recommendation(farmer_id, advice):
    conn = sqlite3.connect('farming.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO recommendations (
            farmer_id, soil_type, rainfall, temperature, soil_moisture, 
            soil_nitrogen, organic_fertilizer_available, price_trend, 
            storage_available, chemical_usage, water_usage, organic_farming_possible, 
            recommended_crop, irrigation_advice, fertilizer_advice, market_advice, sustainability_advice
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        farmer_id, advice['soil_type'], advice['rainfall'], advice['temperature'],
        advice['soil_moisture'], advice['soil_nitrogen'], advice['organic_fertilizer_available'],
        advice['price_trend'], advice['storage_available'], advice['chemical_usage'], 
        advice['water_usage'], advice['organic_farming_possible'], 
        advice['crop'], advice['irrigation'], advice['fertilizer'], 
        advice['market'], advice['sustainability']
    ))

    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])



def recommend():
    # Get input data from the form
    soil_type = request.form['soil_type']
    rainfall = request.form['rainfall']
    temperature = request.form['temperature']
    soil_moisture = int(request.form['soil_moisture'])
    soil_nitrogen = request.form['soil_nitrogen']
    organic_fertilizer_available = request.form['organic_fertilizer_available']
    price_trend = request.form['price_trend']
    storage_available = request.form['storage_available']
    chemical_usage = int(request.form['chemical_usage'])
    water_usage = int(request.form['water_usage'])
    organic_farming_possible = request.form['organic_farming_possible']
    
    # Create a dictionary to mimic the args object
    args = {
        'soil_type': soil_type,
        'rainfall': rainfall,
        'temperature': temperature,
        'soil_moisture': soil_moisture,
        'soil_nitrogen': soil_nitrogen,
        'organic_fertilizer_available': organic_fertilizer_available,
        'price_trend': price_trend,
        'storage_available': storage_available,
        'chemical_usage': chemical_usage,
        'water_usage': water_usage,
        'organic_farming_possible': organic_farming_possible
    }

    # Call the get_farm_advice function with the dictionary
    farm_advice = get_farm_advice(args)
    
    # Render the recommendations on a new page
    return render_template('recommendations.html', advice=farm_advice)

if __name__ == '__main__':
    app.run(debug=True)
