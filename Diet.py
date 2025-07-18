import streamlit as st
import base64


def encode_image(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def set_background_responsive(desktop_image, mobile_image):
    desktop_encoded = encode_image(desktop_image)
    mobile_encoded = encode_image(mobile_image)

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{desktop_encoded}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    @media only screen and (max-width: 768px) {{
        .stApp {{
            background-image: url("data:image/jpg;base64,{mobile_encoded}");
            background-size: cover;
            background-position: center center;
            background-attachment: scroll;
        }}
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.5);
        z-index: -1;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
 

# 👇 Set background image here
set_background_local("delicious-healthy-lettuce-salad.jpg,delicious-2.jpg")
st.title("🥗 Personal Diet Recommender")
st.header("👤 Personal Details")
name=st.text_input("Enter your name","Type Here...")
age=st.number_input("Enter your Age",step=1,placeholder="How Old are you?")
gender=st.radio('Select Your Gender',('Male','Female'))
st.header("📏 Body Measurements")
weight=st.number_input("Weight in Kgs",placeholder="How much do you weigh?")
status=st.radio('Select your height format:',('cms','meters','feet'))
if(status=='cms'):
    height=st.number_input("Height in  Centimeters",placeholder="How high are you?")
elif(status=='meters'):
    height=st.number_input("Height in  Meters",placeholder="How high are you?")
else:
    height=st.number_input("Height in  Feet",placeholder="How high are you?")
st.header("🧬 Body Composition & Lifestyle")    
know_body_fat = st.checkbox("Do you know your Body Fat Percentage?")
bodyFat = None
if know_body_fat:
    bodyFat = st.slider("Select your Body Fat Percentage:", 5, 60)
else:
    st.info("You can skip this if you don't know your body fat percentage.")

activeness=st.selectbox("How Physically active are you on daily basis?",['Sedentary (little or no exercise)','Lightly active (light exercise 1–3 days/week)','Moderately active (moderate exercise 3–5 days/week)','Very active (hard exercise 6–7 days/week)','Extra active (very intense physical job or training)'])
st.header("💊 Medical Information")
Diabetic=st.checkbox("I have diabetes")

BP=st.radio('Blood Pressure status',('Normal','High','Low'))

sleep=st.number_input("How many hours do you sleep daily on average?",1,12)

st.markdown("**Are you lactose intolerant?**")
st.caption("Lactose intolerance means your body cannot easily digest lactose, a type of sugar found in milk and dairy products.")
lactose = st.selectbox("Please select an option:", ['No', 'Yes', "I'm not sure"])
preference=st.radio('Do you follow Vegetarian or Non-vegetarian diet?',('Vegetarian','Non-Vegetarian','Vegan'))
meals=st.number_input("How many meals do you have daily on average?",1,8)
medical=st.text_input("Any other medical conditions to be considered?","Type Here...")
if st.button("Submit"):
    if height > 0 and weight > 0:
        if status == 'cms':
            bmi = weight / ((height / 100) ** 2)
        elif status == 'meters':
            bmi = weight / (height ** 2)
        else:
            bmi = weight / ((height * 0.3048) ** 2)
        bmi = round(bmi, 2)

        st.markdown(f"### 👋 Hello {name}!")
        st.markdown(f"✅ **Your BMI is:** `{bmi}`")
        st.markdown(f"🎂 **You are:** `{int(age)}` years old.")


        if bmi < 16:
            st.error("You are **Extremely Underweight**")
        elif 16 <= bmi < 18.5:
            st.warning("You are **Underweight**")
        elif 18.5 <= bmi < 25:
            st.success("You are **Healthy**")
        elif 25 <= bmi < 30:
            st.warning("You are **Overweight**")
        else:
            st.error("You are **Extremely Overweight**")

        if Diabetic:
            st.info("🩺 You mentioned you're Diabetic.")
        else:
            st.info("🩺 You are Non-Diabetic.")

        # ✅ Move this block inside
        st.markdown("### 📋 Here is your basic diet chart (sample):")
        try:
            st.image("diet-chart.png", use_column_width=True)
        except:
            st.warning("⚠️ diet-chart.png not found in your directory.")
    else:
        st.error("Please enter valid height and weight to calculate BMI.")
