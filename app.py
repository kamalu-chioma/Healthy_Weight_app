# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:36:35 2022

@author: user
"""
import streamlit as st


st.title('Aim for a HEALTHY WEIGHT')

menu = ["Home", "BMI Calculator", "Tips for Healthy Weight"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.info("What is Healhty Weight?")
    st.success("Reaching and maintaining a healthy weight is important for overall health and can help you prevent and control many diseases and conditions. Being over-weight or Obese increases your risk of a heart disease, high blood pressure, type 2 diabetes, breathing problems, and certain types of cancer. On the other hand,  being under-weight can increase your risk of Anemia, and other complications.                ____ How is Healhty Weight measured? BMI is a simple metric system that classifies a person's thickness or thinness.")
    if st.checkbox("Click here to know more about BMI"):
    	st.text("The BMI is generally used as a means of correlation between groups related by general")
    	st.text("mass and can serve as a vague means of estimating adiposity.The duality of the BMI is")
    	st.text("that, while it is easy to use as a general calculation, it is limited as to how accurate")
    	st.text("and pertinent the data obtained from it can be. Generally, the index is suitable for")
    	st.text("recognizing trends within sedentary or overweight individuals because there is a smaller")
    	st.text("margin of error.The BMI has been used by the WHO as the standard for recording obesity")
    	st.text("statistics since the early 1980s.")

elif choice == "BMI Calculator":
    st.header("Here you can checkout your BMI category")
    name=st.text_input("Enter your name:")
    gender=st.radio("What is your Gender?",("Male","Female"))
    selection=st.selectbox("Select your age group",["10-17","18-34","35-44","45-54","55-64","65-74","75-79"])
    height=st.slider("Your Height(in metres)",0.55,2.72)
    weight=st.slider("Your Weight(in kilograms)",5,120)
    bmi=weight/(height*height)
    if bmi==0.11:
            st.text("      ")
    if st.button("Submit"):
    	result=("Hi "+str(name)+", your bmi is "+ str(bmi))
    	st.text(result)
    	
    if bmi < 14:
    	st.warning("You are very THIN! This BMI is pretty much unhealthy!!")
    	
    else:
            if bmi > 35 :
                    st.warning("You are OBESE! This is unhealhty for you")
                    
                   
            else :
                    st.success("You have an acceptable bmi")
                    

    if bmi>35:
    	if (gender=="Female"):
             st.write("Head over to the 'Tips for Healthy weight' tab")
    		
    	else:	
             st.write("Head over to the 'Tips for Healthy weight' tab")
    		
    else :
            if bmi<16:
                    if (gender=="Female"):
                        st.write("Head over to the 'Tips for Healthy weight' tab")

                           
                    else:	
                        st.write("Head over to the 'Tips for Healthy weight' tab")

                           
            else:
                    if (gender=="Male"):
                        st.write("You are good to go; Keep it up!")

                         
                    else :
                        st.write("You are good to go; Keep it up!")

                          
else:
    st.write("Tips FOR HEALTHY WEIGHT")
    st.text("")
    
    st.warning("Healthy Weight tips for those under the 'THIN' category ")
    st.text("")
    if st.checkbox("Click here to know important tips to gain weight."):
        st.info("1.) Eat more calories than your body burns.")
        st.info("2.) Increase your fibre intake.")
        st.info("3.) Eat Energy-Dense Foods and Use Sauces, Spices and Condiments.")
        st.info("4.) Eat plenty of proteins.")
        st.info("5.) Drink high-calorie smoothies or shakes.")
        st.info("6.) Get quality Sleep.")
        st.text("")
        st.text("")
        
		
        
    
    st.warning("Healthy Weight tips for those under the 'OBESE/FAT' category ")
    st.text("")
    
    if st.checkbox("Click here to know how to get and maintain a good BMI."):
        st.info("1.) Try to make physical activity a regular part of your day, just like brushing your teeth.")
        st.info("2.) Stay hydrated and eat balanced diet.")
        st.info("3.) Avoid random snacking and junk food.")
        st.info("4.) Eat high fibre foods, as they tend to be more filling")
        st.info("5.) Read food labels; ensure they have low calorie impact ")
 
   