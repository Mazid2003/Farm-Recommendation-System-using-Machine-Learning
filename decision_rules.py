import argparse
import sys

def crop_recommendation(soil_type, rainfall, temperature, soil_moisture, soil_nitrogen, organic_fertilizer_available, price_trend):
    if soil_type == "loamy" and rainfall == "moderate":
        if temperature == "high" and soil_moisture < 50:
            return "Grow Rice"
        elif temperature == "moderate" and soil_moisture >= 50:
            return "Grow Wheat"
        else:
            return "Grow Barley"
    elif soil_type == "sandy" and rainfall == "low":
        if price_trend == "high":
            return "Grow Maize"
        else:
            return "Grow Sorghum"
    else:
        return "Grow Soybean"

def irrigation_advice(soil_moisture, rainfall):
    if soil_moisture < 50:
        return "Irrigate every 2 days"
    elif rainfall == "high":
        return "Monitor irrigation weekly"
    else:
        return "Monitor irrigation daily"

def fertilizer_advice(soil_nitrogen, organic_fertilizer_available):
    if soil_nitrogen == "low" and organic_fertilizer_available == "yes":
        return "Use organic fertilizers (compost, manure)"
    elif soil_nitrogen == "low" and organic_fertilizer_available == "no":
        return "Use chemical fertilizers"
    else:
        return "Use balanced fertilizers"

def market_advice(price_trend):
    if price_trend == "high":
        return "Sell now"
    elif price_trend == "dropping":
        return "Wait for prices to stabilize"
    else:
        return "Sell when prices rise"

def sustainability_advice(organic_farming_possible):
    if organic_farming_possible == "yes":
        return "Switch to organic fertilizers for better sustainability"
    else:
        return "Continue using conventional farming methods"

def get_farm_advice(args):
    # Crop recommendation based on conditions
    crop = crop_recommendation(
        args['soil_type'], 
        args['rainfall'], 
        args['temperature'], 
        args['soil_moisture'], 
        args['soil_nitrogen'], 
        args['organic_fertilizer_available'], 
        args['price_trend']
    )
    
    # Irrigation advice based on moisture and rainfall
    irrigation = irrigation_advice(args['soil_moisture'], args['rainfall'])
    
    # Fertilizer recommendation based on nitrogen and fertilizer availability
    fertilizer = fertilizer_advice(args['soil_nitrogen'], args['organic_fertilizer_available'])
    
    # Market advice based on price trend
    market = market_advice(args['price_trend'])
    
    # Sustainability advice based on organic farming possibility
    sustainability = sustainability_advice(args['organic_farming_possible'])
    
    # Return a dictionary with the recommendations
    return {
        'crop': crop,
        'irrigation': irrigation,
        'fertilizer': fertilizer,
        'market': market,
        'sustainability': sustainability
    }


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Farm Decision Recommendation System")
    
    # Arguments for input
    parser.add_argument('--soil_type', required=True, help="Type of soil (e.g., loamy, sandy, clay)")
    parser.add_argument('--rainfall', required=True, choices=['low', 'moderate', 'high'], help="Rainfall level")
    parser.add_argument('--temperature', required=True, choices=['low', 'moderate', 'high'], help="Temperature range")
    parser.add_argument('--soil_moisture', required=True, type=int, help="Soil moisture percentage")
    parser.add_argument('--soil_nitrogen', required=True, choices=['low', 'high'], help="Soil nitrogen level")
    parser.add_argument('--organic_fertilizer_available', required=True, choices=['yes', 'no'], help="Availability of organic fertilizers")
    parser.add_argument('--price_trend', required=True, choices=['high', 'dropping', 'stable'], help="Market price trend")
    parser.add_argument('--storage_available', required=False, choices=['yes', 'no'], help="Is storage available?")  # Optional
    parser.add_argument('--chemical_usage', required=False, type=int, help="Chemical usage in kg per hectare")  # Optional
    parser.add_argument('--water_usage', required=False, type=int, help="Water usage in liters per hectare")  # Optional
    parser.add_argument('--organic_farming_possible', required=True, choices=['yes', 'no'], help="Is organic farming possible?")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get farm advice based on parsed arguments
    get_farm_advice(args)  # Passing args as a single object
