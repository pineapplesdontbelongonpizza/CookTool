import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import pickle


df = pd.read_csv("restaurant_sales.csv")


# Encoders
dish_encoder = LabelEncoder()
day_encoder = LabelEncoder()


df["dish"] = dish_encoder.fit_transform(df["dish"])

df["day"] = day_encoder.fit_transform(df["day"])


df["holiday"] = df["holiday"].map({
    "Yes": 1,
    "No": 0
})


# IMPORTANT: 5 FEATURES
X = df[
    [
        "dish",
        "day",
        "temp",
        "holiday",
        "previous_sales"
    ]
]


y = df["previous_sales"]



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


model.fit(
    X_train,
    y_train
)


pred = model.predict(X_test)


print(
    "Error:",
    mean_absolute_error(y_test,pred)
)



pickle.dump(
    model,
    open("food_model.pkl","wb")
)


pickle.dump(
    dish_encoder,
    open("dish_encoder.pkl","wb")
)


pickle.dump(
    day_encoder,
    open("day_encoder.pkl","wb")
)


print("Phew its over! Model trained and saved successfully!")