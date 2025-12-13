import streamlit as st
import requests

API_KEY = "cf8cb0e46b008554948cd7b23e882906"

def funny_comment(temp, condition):
    if temp < 10:
        return "🥶 Itna thand hai ki WiFi bhi kaanp raha!"
    elif temp < 20:
        return "😐 Jacket pehno boss!"
    elif temp < 30:
        return "🙂 Mausam perfect hai, chai lao ☕"
    else:
        return "🥵 Garmi itni hai ki phone bhi pighal raha!"

st.title("🌦️ Weather App ☁️")
st.write("Live weather + funny comments")

city = st.text_input("Enter city name")

if st.button("Check Weather"):
    if city == "":
        st.warning("Please enter a city name")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data["cod"] != 200:
            st.error("City not found ❌")
        else:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]

            st.success(f"🌡️ {temp}°C | ☁️ {condition}")
            st.info(funny_comment(temp, condition))
