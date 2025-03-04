import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "metre-to-kilometre" : 0.001,
        "kilometre-to-metre" : 1000,
        "gram-to-kilogram" : 0.001,
        "kilogram-to-gram" : 1000
    }

    key = f"{unit_from}-to-{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion Failed"
    

st.title("Unit Convertor") 
value = st.number_input("Enter the Value", min_value=1.0 , step = 1.0 )
unit_from = st.selectbox("Convert from:", ["metre" ,"kilometre", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["metre" ,"kilometre", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value,unit_from,unit_to)
    st.write(f"Converted Value {result}")