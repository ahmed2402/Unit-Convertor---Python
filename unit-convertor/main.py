import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
    # Length Conversions
    "metre-to-kilometre": 0.001,
    "kilometre-to-metre": 1000,
    "metre-to-centimetre": 100,
    "centimetre-to-metre": 0.01,
    "metre-to-millimetre": 1000,
    "millimetre-to-metre": 0.001,
    "kilometre-to-miles": 0.621371,
    "miles-to-kilometre": 1.60934,
    "inch-to-centimetre": 2.54,
    "centimetre-to-inch": 0.393701,
    "foot-to-metre": 0.3048,
    "metre-to-foot": 3.28084,
    "yard-to-metre": 0.9144,
    "metre-to-yard": 1.09361,

    # Weight Conversions
    "gram-to-kilogram": 0.001,
    "kilogram-to-gram": 1000,
    "pound-to-kilogram": 0.453592,
    "kilogram-to-pound": 2.20462,
    "ounce-to-gram": 28.3495,
    "gram-to-ounce": 0.035274,

    # Time Conversions
    "second-to-minute": 1/60,
    "minute-to-second": 60,
    "minute-to-hour": 1/60,
    "hour-to-minute": 60,
    "hour-to-day": 1/24,
    "day-to-hour": 24,

    # Temperature Conversions (Handled Differently)
    "celsius-to-fahrenheit": lambda c: (c * 9/5) + 32,
    "fahrenheit-to-celsius": lambda f: (f - 32) * 5/9,
    "celsius-to-kelvin": lambda c: c + 273.15,
    "kelvin-to-celsius": lambda k: k - 273.15,

    # Volume Conversions
    "litre-to-millilitre": 1000,
    "millilitre-to-litre": 0.001,
    "gallon-to-litre": 3.78541,
    "litre-to-gallon": 0.264172,

    # Speed Conversions
    "kilometre per hour-to-metre per second": 0.277778,
    "metre per second-to-kilometre per hour": 3.6,
    "mile per hour-to-kilometre per hour": 1.60934,
    "kilometre per hour-to-mile per hour": 0.621371
}


    key = f"{unit_from}-to-{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "⚠️ Conversion not supported!"

    

st.title("Unit Convertor") 
value = st.number_input("Enter the Value", min_value=1.0 , step = 1.0 )
units = [
    "metre", "kilometre", "centimetre", "millimetre", "mile", "inch", "foot", "yard",
    "gram", "kilogram", "pound", "ounce",
    "second", "minute", "hour", "day",
    "celsius", "fahrenheit", "kelvin",
    "litre", "millilitre", "gallon",
    "kilometre per hour", "metre per second", "mile per hour"
]

unit_from = st.selectbox("Convert from:", units)
unit_to = st.selectbox("Convert to:", units)

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if isinstance(result, str) and "⚠️" in result:
        st.error(result)
    else:
        st.success(f"✅ {value} {unit_from} = {result} {unit_to}")

