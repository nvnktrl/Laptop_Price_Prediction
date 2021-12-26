import streamlit as st
import pickle
import numpy as np

# Importing the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Prediction")

# Brand
company = st.selectbox('Brand',df['Company'].unique())

# Type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight of the Laptop(in KG)')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['Yes','No'])

# IPS LCD
ips = st.selectbox('IPS Panel',['Yes','No'])

#Screen Size
screen_size = st.number_input('Screen Size(in Inches)')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768',
  '1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440',
  '2304x1440'])

# Processor
cpu = st.selectbox('Processor',df['ProcessorBrand'].unique())

# Hard Drive
hdd = st.selectbox('Hard Drive(in GB)',[0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD(in GB)',[0,128,256,512,1024])

# GPU
gpu = st.selectbox('Graphic Card',df['GPU_Brand'].unique())

# Operating System
os = st.selectbox('Operating System',df['OperatingSystem'].unique())

if st.button('Predict Price'):
    # main code
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == 'Yes':
         ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The Predicted Price of given configuration is INR " + str(int(np.exp(pipe.predict(query)[0]))))


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
