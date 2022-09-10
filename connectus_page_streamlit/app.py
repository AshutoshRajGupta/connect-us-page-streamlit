#streamlit run filename.py
from pickle import NONE
#from tkinter import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# setting page configuration
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return NONE
    return r.json()

#----use local css-----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


#----load assets
lottie_coding=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_todo = Image.open("images/todo.png")
img_keepnotes = Image.open("images/keep_notes.png")


#-------header section----
with st.container():
    st.header("Hi,I am Ashutosh :wave:")
    st.title("A web Developer and Data Analyst from India")
    st.write("I am passionate about finding ways to use python in more efficient way")
    st.write("[About me >](https://portfolio-ashutosh.netlify.app/)")
    st.title("[lets connect >](https://www.linkedin.com/in/ashutosh-raj-gupta-18230820b/)")

#----About myself-----
with st.container():
    st.write("----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("About my self")
        st.write("##")
        st.write(
            """
            Hi 👋, I'm Ashutosh Raj Gupta.
            I am currently pursuing my second year Bachelor of Engineering in Computer Engineering from D Y Patil College Of Engineering Akurdi,pune.
            Currently learning React,Flutter and Java ,have a knowledge of python ,c++ and Web Development(HTML & CSS & JS & MySQL).
            Love to help and work with people.
            Hobbies - listening musics,playing volleyball,cricket and learning new things and sketching.
            """
        )
        st.write("[Github profile >](https://github.com/AshutoshRajGupta/AshutoshRajGupta)")
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_todo)
    with text_column:
        st.subheader("TODO APP MADE USING REACT JS")
        st.write(
            """
            to-do app using react js.
            user can add the todo ,edit the todo.
            user can delete the todo.
            """
        )
        st.markdown("[project link....](https://todo-app-delta-beryl.vercel.app/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_keepnotes)
    with text_column:
        st.subheader("KEEP-NOTES-APP")
        st.write(
            """
             keep notes app made using react js.
             user can add the notes with its own color,user can edit the notes.
             user can delete the notes.
            """
        )
        st.markdown("[project link...](https://keep-notes-app-alpha.vercel.app/)")



#-----contact me-----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/ag2364443@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name"  placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here"required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()

#-----connect us ------
with st.container():
    st.write("---")
    st.header("lets connect with each other")
    st.title("[GITHUB >](https://github.com/AshutoshRajGupta/AshutoshRajGupta)")
    st.title("[LINKEDIN >](https://www.linkedin.com/in/ashutosh-raj-gupta-18230820b)")
    st.title("[INSTAGRAM >](https://www.instagram.com/guptaashutoshraj?r=nametag)")
    st.title("[FACEBOOK >](https://www.facebook.com/profile.php?id=100022615870474)")

