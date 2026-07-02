import pandas as pd
import random
from datetime import datetime, timedelta


dishes = [
    "Margherita Pizza",
    "Farmhouse Pizza",
    "Veggie Supreme Pizza",
    "Pasta Alfredo",
    "Pasta Arrabbiata",
    "Pesto Pasta",
    "Lasagna Primavera",
    "Veg Lasagna",
    "Mac and Cheese",
    "Veg Risotto",
    "Mushroom Risotto",
    "Veg Burger",
    "Paneer Burger",
    "Grilled Vegetable Sandwich",
    "Club Sandwich Veg",
    "Grilled Cheese Sandwich",
    "Caesar Salad",
    "Greek Salad",
    "Garden Fresh Salad",
    "French Fries",
    "Cheese Garlic Bread",
    "Bruschetta",
    "Mushroom Soup",
    "Tomato Basil Soup",
    "Cream of Broccoli Soup",
    "Nachos with Cheese",
    "Veg Quesadilla",
    "Pancakes",
    "Waffles",
    "Chocolate Brownie",
    "Cheesecake",
    "Tiramisu",
    "Cold Coffee",
    "Iced Tea",
    "Lemonade",
    "Fresh Fruit Smoothie"
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


start_date = datetime(2025,1,1)

data = []


for i in range(500):

    date = start_date + timedelta(days=i)

    dish = random.choice(dishes)

    day = days[date.weekday()]


    temp = random.randint(15,40)


    holiday = random.choice(["Yes","No"])


    # realistic sales logic

    base_sales = random.randint(40,120)


    if day in ["Saturday","Sunday"]:
        base_sales += random.randint(20,60)


    if holiday == "Yes":
        base_sales += random.randint(30,80)


    if temp > 35:
        if dish in ["Coffee","Salad"]:
            base_sales += 20
        else:
            base_sales -= 10


    sales = max(base_sales,10)



    data.append([
        date.strftime("%Y-%m-%d"),
        dish,
        day,
        temp,
        holiday,
        sales
    ])



df = pd.DataFrame(
    data,
    columns=[
        "date",
        "dish",
        "day",
        "temp",
        "holiday",
        "previous_sales"
    ]
)


df.to_csv(
    "restaurant_sales.csv",
    index=False
)


print("Wooohooo! Dataset created!")
print(df.head())