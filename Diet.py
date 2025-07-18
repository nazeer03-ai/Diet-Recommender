import streamlit as st
import base64

# Background image setup
def set_background_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Use relative path to image
set_background_local("delicious-healthy-lettuce-salad.jpg")

# Main app
st.title("Personal Diet Recommender")
name = st.text_input("Enter your name", "Type Here...")
age = st.number_input("Enter your Age", placeholder="How Old are you?")
gender = st.radio('Select Your Gender', ('Male', 'Female'))
weight = st.number_input("Weight in Kgs", placeholder="How much do you weigh?")
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

if(status == 'cms'):
    height = st.number_input("Height in  Centimeters", placeholder="How high are you?")
elif(status == 'meters'):
    height = st.number_input("Height in  Meters", placeholder="How high are you?")
else:
    height = st.number_input("Height in  Feets", placeholder="How high are you?")

bodyFat = st.slider("If you know your Body Fat Percentage,Select it on the slider:", 5, 60)
activeness = st.selectbox("How Physically active are you on daily basis?", [
    'Sedentary (little or no exercise)',
    'Lightly active (light exercise 1–3 days/week)',
    'Moderately active (moderate exercise 3–5 days/week)',
    'Very active (hard exercise 6–7 days/week)',
    'Extra active (very intense physical job or training)'
])
Diabetic = st.checkbox("Check this box if you have diabetes")
BP = st.radio('Do you have low or high blood pressure', ('High', 'Normal', 'Low'))
sleep = st.number_input("How many hour do you sleep daily on average?", 1, 12)
lactose = st.selectbox("Are you Lactose Intolerant?", ['Yes', 'No'])
preference = st.radio('Do you follow Vegetarian or Non-vegetarian diet?', ('Vegetarian', 'Non-Vegetarian', 'Vegan'))
meals = st.number_input("How many meals do you have daily on average?", 1, 8)
medical = st.text_input("Any other medical conditions to be considered?", "Type Here...")

if(st.button('Submit')):
    if(status == 'cms'):
        bmi = weight / ((height / 100) ** 2)
    elif(status == 'meters'):
        bmi = weight / (height ** 2)
    else:
        bmi = weight / (((height / 3.28)) ** 2)

    st.text(f"Hey! {name}. Your weight is {weight}. Your height is {height}. So, your BMI is {bmi}.")
    
    if(Diabetic):
        st.text("Your are Diabetic")
    else:
        st.text("You are Non-Diabetic")

    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    else:
        st.error("Extremely Overweight")

    st.text("Here is your diet chart:")
    st.image('diet-chart.png')
