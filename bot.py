from tkinter import *
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='en-in')
            print(Query)
        except Exception as e:
            print(e)
            print("I was unable to hear")
            return "None"

        return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    time = datetime.datetime.now().strftime("%H:%M")
    hour, minute = time.split(':')
    speak(f"The time is {hour} hours and {minute} minutes")

def Hello():
    speak("Hello Pranali! I am your desktop assistant Pixie. Tell me, how may I help you?")

def action(query):
    query = query.lower()
    if "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("www.youtube.com")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("www.google.com")

    elif "which day it is" in query:
        tellDay()

    elif "tell me the time" in query:
        tellTime()

    elif "bye" in query:
        speak("Bye and thank you for your time")
        exit()

    elif "from wikipedia" in query or "search" in query:
        speak("Checking Wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=4)
        speak("According to Wikipedia")
        speak(result)
        return result

    elif "tell me your name" in query:
        speak("I am Pixie, your desktop assistant")
    else:
        speak("I am not sure how to help with that")
    return None

def User_send():
    send = entry1.get()
    response = action(send)
    text.insert(END, "Me --> " + send + "\n")
    if response is not None:
        text.insert(END, "Bot <-- " + str(response) + "\n")
    if response == "ok sir":
        root.destroy()

def ask():
    ask_val = takeCommand()
    text.insert(END, "Me --> " + ask_val + "\n")
    response = action(ask_val)
    if response is not None:
        text.insert(END, "Bot <-- " + str(response) + "\n")
    if response == "ok sir":
        root.destroy()


root = Tk()
root.geometry("550x675")
root.title("Voice Assistant")
root.resizable(False, False)
root.config(bg="#edb4e6")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#edb4e6")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
Text_label = Label(Main_frame, text="Voice Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
img_path = "pixeiImgg.jpg"  # Replace with your image path
try:
    original_image = Image.open(img_path)
    resized_image = original_image.resize((200, 200), Image.Resampling.LANCZOS)
    Display_Image = ImageTk.PhotoImage(resized_image)

    # Place the image label
    image_label = Label(root, image=Display_Image, bg="#edb4e6")
    image_label.place(x=175, y=140)  # Adjust x, y coordinates as needed
except FileNotFoundError:
    print(f"Image file not found at {img_path}")
except Exception as e:
    print(f"Error loading image: {e}")

# Add a text widget
text = Text(root, font='Courier 10 bold', bg="#edb4e6")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

# Add an entry widget
entry1 = Entry(root, justify=CENTER)
entry1.place(x=100, y=500, width=350, height=30)

# Add button1
button1 = Button(root, text="ASK", bg="#ed80df", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
button1.place(x=70, y=575)

# Add button2
button2 = Button(root, text="Send", bg="#ed80df", pady=16, padx=40, borderwidth=3, relief=SOLID, command=User_send)
button2.place(x=400, y=575)


Hello()  # Greet the user when the program starts
root.mainloop()
