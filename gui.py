from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES,Translator
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
window=Tk() #create a window
window.geometry("900x400")
window.config(bg='#40E0D0')
window.title("Language Translator")
Label(text='Language Translator',font='Arial 20 bold').place(x=240,y=50)
Label(text='Source Language',font='Arial 14 bold').place(x=50,y=120)
Label(text='Destination Language',font='Arial 14 bold').place(x=440,y=120)
def language_translate():
    x = Translator()
    translated = x.translate(text=t1.get(1.0, END), src=s1.get(), dest=d1.get())
    t2.delete(1.0, END)
    t2.insert(END, translated.text)
def Speak_output_text():
    translated_text = t2.get(1.0, END).strip()
    if translated_text:
        lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(d1.get())]
        print(lang_code)
        tts = gTTS(text=translated_text, lang=lang_code)
        audio_file = "translated_text.mp3"
        tts.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file) 

def Speak_input_text():
    translated_text = t1.get(1.0, END).strip()
    if translated_text:
        lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(s1.get())]
        print(lang_code)
        tts = gTTS(text=translated_text, lang=lang_code)
        audio_file = "translated_text.mp3"
        tts.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file) 
def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            t1.delete(1.0, END)
            t1.insert(END, text)
        except sr.UnknownValueError:
            t1.delete(1.0, END)
            t1.insert(END, "Sorry, I did not understand that.")
        except sr.RequestError:
            t1.delete(1.0, END)
            t1.insert(END, "Sorry, the service is unavailable at the moment.")

            
lang_list=list(LANGUAGES.values())
print(lang_list)
#input language selection
s1=ttk.Combobox(window,values=lang_list)
s1.place(x=240,y=120)
#output language selection
d1=ttk.Combobox(window,values=lang_list)
d1.place(x=680,y=120)
#input language text
t1=Text(window,height=4,width=18,font='Arial 12 bold')
t1.place(x=50,y=180)
#output language text
t2=Text(window,height=4,width=18,font='Arial 12 bold')
t2.place(x=440,y=180)
Button(text='Translate',font='Arial 12 bold',command=language_translate).place(x=280,y=230)
Button(text='Speak Output Text',font='Arial 12 bold',command=Speak_output_text).place(x=280,y=350)
Button(text='Speak Input Text',font='Arial 12 bold',command=Speak_input_text).place(x=100,y=350)
Button(text='Audio Text',font='Arial 12 bold',command=voice_to_text).place(x=475,y=350)
window.mainloop()