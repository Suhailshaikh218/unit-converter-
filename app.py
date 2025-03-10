import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu  # For improved UI
from streamlit_lottie import st_lottie  # For animations
import json  # For loading Lottie animations

# Load Lottie animation
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Title and animation
st.title("Unit Converter")
lottie_animation = load_lottie("animation.json")  # Replace with your Lottie JSON file
st_lottie(lottie_animation, height=200)

# Custom CSS for improved UI
st.markdown(
    """
    <style>
    .stSelectbox, .stNumberInput, .stButton {
        margin: 10px 0;
    }
    .stMarkdown h1 {
        color: #4F8BF9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dark/Light theme toggle
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Sidebar for history
st.sidebar.title("Conversion History")
history = []

# Unit categories
unit_categories = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Feet": 3.28084,
        "Miles": 0.000621371,
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K",
    },
    "Time": {
        "Seconds": 1,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400,
    },
    "Speed": {
        "Meters/Second": 1,
        "Kilometers/Hour": 3.6,
        "Miles/Hour": 2.23694,
        "Feet/Second": 3.28084,
    },
    "Energy": {
        "Joules": 1,
        "Kilojoules": 0.001,
        "Calories": 0.239006,
        "Kilocalories": 0.000239006,
    },
    "Custom": {},  # For user-defined units
}

# Add custom units
st.sidebar.title("Custom Units")
custom_from = st.sidebar.text_input("Define custom unit (From)")
custom_to = st.sidebar.text_input("Define custom unit (To)")
custom_factor = st.sidebar.number_input("Conversion factor (To = From * factor)", value=1.0)
if st.sidebar.button("Add Custom Unit"):
    unit_categories["Custom"][custom_from] = 1
    unit_categories["Custom"][custom_to] = custom_factor
    st.sidebar.success(f"Added custom unit: {custom_from} to {custom_to} with factor {custom_factor}")

# Main app
unit_category = option_menu(
    "Select a unit category",
    list(unit_categories.keys()),
    orientation="horizontal",
)

input_value = st.number_input("Enter the value to convert", value=1.0)

if unit_category in unit_categories:
    units = list(unit_categories[unit_category].keys())
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)

    # Conversion logic
    if unit_category == "Temperature":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                converted_value = (input_value * 9 / 5) + 32
            elif to_unit == "Kelvin":
                converted_value = input_value + 273.15
            else:
                converted_value = input_value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                converted_value = (input_value - 32) * 5 / 9
            elif to_unit == "Kelvin":
                converted_value = (input_value - 32) * 5 / 9 + 273.15
            else:
                converted_value = input_value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                converted_value = input_value - 273.15
            elif to_unit == "Fahrenheit":
                converted_value = (input_value - 273.15) * 9 / 5 + 32
            else:
                converted_value = input_value
    else:
        converted_value = input_value * (
            unit_categories[unit_category][to_unit] / unit_categories[unit_category][from_unit]
        )

    st.write(f"**{input_value} {from_unit} = {converted_value} {to_unit}**")

    # Add to history
    history.append(f"{input_value} {from_unit} = {converted_value} {to_unit}")
    st.sidebar.write("### History")
    for entry in history[-5:]:  # Show last 5 entries
        st.sidebar.write(entry)

# 3D Animation (using Lottie)
st.write("### 3D Animation")
lottie_3d = load_lottie("3d_animation.json")  # Replace with your 3D Lottie JSON file
st_lottie(lottie_3d, height=300)
# Load and display 3D animation
st.write("### 3D Animation")
lottie_3d = load_lottie("3d_animation.json")
if lottie_3d:
    st_lottie(lottie_3d, height=300)
else:
    st.write("3D Animation not available.")

# Footer with developer details
st.markdown("---")
st.write("Developed by **Muhammad Suhail Shaikh**")
st.write("Contact: **mmuhammadsuhail234@gmail.com**")