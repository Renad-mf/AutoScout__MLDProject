# Streamlit Documentation: https://docs.streamlit.io/

from textwrap import fill
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# Title/Text
st.title("Auto Scout Project")
st.text("This is the MLD project")

# Add image
img = Image.open("car_img.jpg")
st.image(img, caption="cars", width=300)

# Text_input
name = st.text_input("write your name", placeholder="Your name here")
if st.button("Greeting"):
    st.write("Hello {}, Welcome to our site for car price prediction".format(name.title()))

html_temp = """
<div style="background-color:red;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Car Price Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

# Header/Subheader
st.header('choose the car configuration from the side bar')

# Success/Info/Error
st.success('This is a success message!')
st.info('This is a purely informational message')
st.error("This is an error.")
st.warning("This is a warning message!")
st.exception("NameError('name there is not defined')")


# Dataframe
df=pd.read_csv("Ready_to_ML.csv")

# To load machine learning model
import pickle
filename = "final_pipe_pickle_model"
#scalername = "trans_pickle_Auto_Scout"
model=pickle.load(open(filename, "rb"))
#scaler=pickle.load(open(scalername, "rb"))


# To take feature inputs
age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25))
power_kW=st.sidebar.slider("What is the hp_kw of your car?", 40, 500, step=10)
mileage=st.sidebar.slider("What is the km of your car", 0,415000, step=1000)
engine_size=st.sidebar.slider("What is the size of the engine", 0,6000, step=50)
car_type=st.sidebar.radio('Select car type',('Used', 'Pre-registered', 'Demonstration', "Employee's car"))
car_model=st.sidebar.selectbox("Select model of your car", ('Mercedes-Benz A 180', 'Opel Corsa', 'Opel Astra', 'Opel Adam',
                                                            'Opel Insignia', 'Opel Cascada', 'Opel Grandland X',
                                                            'Renault Megane', 'Renault Clio', 'Renault Captur',
                                                            'Renault Talisman', 'Renault Kadjar', 'Peugeot 308', 'Peugeot 206',
                                                            'Peugeot 208', 'Peugeot 207', 'Peugeot 3008', 'Peugeot 508',
                                                            'Peugeot RCZ', 'Peugeot 2008', 'Fiat 500', 'Fiat Tipo',
                                                            'Fiat 500X', 'Fiat Panda', 'Fiat 500C', 'SEAT Leon', 'SEAT Ibiza',
                                                            'SEAT Arona', 'SEAT Ateca', 'Skoda Octavia', 'Skoda Scala',
                                                            'Skoda Fabia', 'Skoda Superb', 'Skoda Kodiaq', 'Skoda Karoq',
                                                            'Dacia Sandero', 'Dacia Logan', 'Dacia Duster', 'Toyota Yaris',
                                                            'Toyota Aygo', 'Toyota Corolla', 'Toyota Auris', 'Toyota C-HR',
                                                            'Toyota RAV 4', 'Nissan Micra', 'Nissan Qashqai', 'Nissan Juke',
                                                            'Nissan Pulsar', 'Nissan 370Z', 'Nissan 350Z', 'Nissan X-Trail',
                                                            'Ford Fiesta', 'Ford Focus', 'Ford Mondeo', 'Ford Kuga',
                                                            'Ford Mustang', 'Hyundai i30', 'Hyundai i20', 'Hyundai IONIQ',
                                                            'Hyundai TUCSON', 'Volvo V40', 'Volvo S60', 'Volvo XC60',
                                                            'Volvo C30', 'Volvo C70', 'Volvo XC90', 'Volvo S90', 'Volvo XC40',
                                                            'Volvo V90', 'Volvo V60'))



# Create a dataframe using feature inputs
my_dict = {
    "make_model": car_model,
    "power_kW": power_kW,
    "mileage": mileage,
    "age": age,
    "engine_size": engine_size,
    "type": car_type
}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    #st.success(result[0])
    st.success("The estimated price of your car is €{} ".format(result[0]))