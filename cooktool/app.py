import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt


#load model

model = pickle.load(
    open("food_model.pkl", "rb")
)

dish_encoder = pickle.load(
    open("dish_encoder.pkl","rb")
)

day_encoder = pickle.load(
    open("day_encoder.pkl","rb")
)
df = pd.read_csv(
    "restaurant_sales.csv"
)



# Page setup

st.set_page_config(
    page_title="CookTool",
    page_icon="🍽️",
    layout="wide"
)

st.title("CookTool Dashboard")

st.write(
    "AI-powered food demand prediction system to reduce wastage and optimize preparation."
)



# Dashboard Metrics

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Dishes",
        df["dish"].nunique()
    )

with col2:
    st.metric(
        "Total Records",
        len(df)
    )

with col3:
    top_dish = (
        df.groupby("dish")["previous_sales"]
        .mean()
        .idxmax()
    )

    st.metric(
        "Most Popular Dish",
        top_dish
    )


st.divider()


# Sales Trend Graph

st.subheader("Sales Trend")


sales_chart = (
    df.groupby("date")["previous_sales"]
    .sum()
)


st.line_chart(
    sales_chart
)



col1, col2 = st.columns(2)


with col1:

    dish = st.selectbox(
        "Choose Dish",
        sorted(df["dish"].unique())
    )


    day = st.selectbox(
        "Day",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )


with col2:

    temp = st.number_input(
        "Temperature (°C)",
        min_value=10,
        max_value=45,
        value=30
    )


    holiday = st.selectbox(
        "Holiday?",
        [
            "Yes",
            "No"
        ]
    )


previous_sales = st.number_input(
    "Previous Sales",
    min_value=0,
    value=80
)



# Prediction

if st.button("Predict Demand"):
    dish_encoded = dish_encoder.transform([dish])[0]
    day_encoded = day_encoder.transform([day])[0]

    holiday_encoded = (
        1 if holiday == "Yes"
        else 0
    )

    prediction = model.predict(
        [[
            dish_encoded,
            day_encoded,
            temp,
            holiday_encoded,
            previous_sales
        ]]
    )


    demand = int(prediction[0])


    preparation = demand + 5


    waste = preparation - demand



    st.success(
        f"Recommended preparation: {preparation} portions"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Expected Demand",
            f"{demand} portions"
        )


    with col2:

        st.metric(
            "Expected Waste",
            f"{waste} portions"
        )


    st.divider()


    st.subheader("💡 Restaurant Insight")


    if temp > 35:

        st.write(
            "Hot weather detected. Cold beverages and lighter meals may perform better."
        )

    elif holiday == "Yes":

        st.write(
            "Holiday detected. Expect higher customer demand."
        )

    else:

        st.write(
            "Normal day demand pattern."
        )