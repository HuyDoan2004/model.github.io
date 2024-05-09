from tkinter import *
import speech_recognition
import speech_recognition as sr
import pyttsx3
import webbrowser
from gtts import gTTS
import os
from playsound import playsound
from datetime import date
from datetime import datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[0].id)
robot = ""
robot = " Hi, I'm an artificial intelligence "
print("Robot:" + robot)
robot_mouth.say(robot)
robot_mouth.runAndWait()
while True:
    voices = robot_mouth.getProperty('voices')
    robot_mouth.setProperty('voice', voices[0].id)
    with speech_recognition.Microphone() as mic:
            robot_ear.adjust_for_ambient_noise(mic) 
            robot = " Select a language you want to communicate! "
            print("Robot:" + robot)
            robot_mouth.say(robot)
            robot_mouth.runAndWait()
            robot_ear.adjust_for_ambient_noise(mic)
            audio = robot_ear.record(mic, duration = 2)
            print("Robot:...")
    try:
            you = robot_ear.recognize_google(audio)
    except:
            you = ""
    print(" You:  " + you)
    if you == "":
            robot = " Sorry, I can't hear your answer, please try again ! "
    elif "English" in you:
            voices = robot_mouth.getProperty('voices')
            robot_mouth.setProperty('voice', voices[3].id)
            robot = " OK! I will use English to communicate with you"
            print("Robot:" + robot)
            robot_mouth.say(robot)
            robot_mouth.runAndWait()
            while True:
                with speech_recognition.Microphone() as mic:
                    robot_ear.adjust_for_ambient_noise(mic) 
                    robot = "I'm listening "
                    print("Robot:" + robot)
                    robot_mouth.say(robot)
                    robot_mouth.runAndWait()
                    robot_ear.adjust_for_ambient_noise(mic)
                    audio = robot_ear.record(mic, duration = 2)
                    print("Robot:...")
                try:
                    you = robot_ear.recognize_google(audio)
                except:
                    you = ""
                print(" You:  " + you)
                if you == "":
                         robot = " I'm hearing your question or request "
                elif "hello" in you:
                        robot = "Hello my friend, have a nice day!"
                elif "morning" in you:
                        robot = "Goodmorning my friend, have a nice day!"
                elif "afternoon" in you:
                        robot = " Hello, Have a nice afternoon!"
                elif "Love" in you:
                        robot = "Hmm.... of course I love you too :>>"
                elif "today" in you:
                        today = date.today()
                        robot = today.strftime("%B %d, %Y")
                elif "time" in you:
                        now = datetime.now()
                        robot = now.strftime("%H hours %M minutes %S seconds")
                elif "YouTube" in you:
                        webbrowser.open('https://www.youtube.com',new = 2)
                        robot ="Ok! I will open for you!"
                        break
                elif "Google" in you:
                        webbrowser.open('https://www.google.com.vn/',new = 2)
                        robot = "Ok! I will open for you!"
                        break
                elif "bye" in you:
                        robot = "OK! Goodbye, see you again!"
                        break
                elif "Goodnight" in you:
                        robot = "Ok! Goodnight !"
                else:
                        robot = "Sorry, i don't understand you!"

                print("Robot:" + robot)
                robot_mouth.say(robot)
                robot_mouth.runAndWait()
    elif "Japanese" in you:
            voices = robot_mouth.getProperty('voices')
            robot_mouth.setProperty('voice', voices[4].id)
            robot = " はい。日本語を話している"
            print("Robot:" + robot)
            robot_mouth.say(robot)
            robot_mouth.runAndWait()
            while True:
                with speech_recognition.Microphone() as mic:
                    robot_ear.adjust_for_ambient_noise(mic) 
                    robot = " 聞いている "
                    print("Robot:" + robot)
                    robot_mouth.say(robot)
                    robot_mouth.runAndWait()
                    robot_ear.adjust_for_ambient_noise(mic)
                    audio = robot_ear.record(mic, duration = 2)
                    print("Robot:...")
                try:
                    you = robot_ear.recognize_google(audio, language="ja-JP")
                except:
                    you = ""
                print(" You:  " + you)
                if you == "":
                         robot = " 要求を聞いている "
                elif "おはよう" in you:
                        robot = "良い１日を!"
                elif "おはよう" in you:
                        robot = "おはよう。良い１日を!"
                elif "こんにちは" in you:
                        robot = " こんにちは!"
                elif "愛" in you:
                        robot = "本当，私も愛しているよ"
                elif "今日" in you:
                        today = date.today()
                        robot = today.strftime("%B %d, %Y")
                elif "時間" in you:
                        now = datetime.now()
                        robot = now.strftime("%H 時 %M 分 %S 秒")
                elif "YouTube" in you:
                        webbrowser.open('https://www.youtube.com',new = 2)
                        robot ="はい、私はあなたのために開きます"
                        break
                elif "Google" in you:
                        webbrowser.open('https://www.google.com.vn/',new = 2)
                        robot = "はい、私はあなたのために開きます"
                        break
                elif "お休み" in you:
                        robot = "はい。おやすみなさい"
                        break
                elif "さよなら" in you:
                        robot = "さよなら。またね!"
                        break
                else:
                        robot = "すみません、言ってる意味がわかりません もう一度言ってください!"

                print("Robot:" + robot)
                robot_mouth.say(robot)
                robot_mouth.runAndWait()
    elif "Vietnamese" in you:
            voices = robot_mouth.getProperty('voices')
            robot_mouth.setProperty('voice', voices[1].id)
            robot = " Ok! Tôi sẽ sử dụng ngôn ngữ Tiếng Việt"
            print("Robot:" + robot)
            robot_mouth.say(robot)
            robot_mouth.runAndWait()
            while True:
                with speech_recognition.Microphone() as mic:
                    robot_ear.adjust_for_ambient_noise(mic) 
                    robot = " Tôi đang nghe "
                    print("Robot:" + robot)
                    robot_mouth.say(robot)
                    robot_mouth.runAndWait()
                    robot_ear.adjust_for_ambient_noise(mic)
                    audio = robot_ear.record(mic, duration = 2)
                    print("Robot:...")
                try:
                    you = robot_ear.recognize_google(audio, language="vi-VN")
                except:
                    you = ""
                print(" You:  " + you)
                if you == "":
                         robot = " Tôi không nghe thấy bạn, hãy nói lại "
                elif "xin chào" in you:
                        robot = "xin chào bạn"
                elif "sáng" in you:
                        robot = "Chúc bạn một buổi sáng tốt lành"
                elif "ngày" in you:
                        today = date.today()
                        robot = today.strftime("%B %d, %Y")
                elif "giờ" in you:
                        now = datetime.now()
                        robot = now.strftime("%H giờ %M phút %S giây")
                elif "YouTube" in you:
                        webbrowser.open('https://www.youtube.com',new = 2)
                        robot ="Ok, tôi sẽ bật lên cho bạn!"
                        break
                elif "Google" in you:
                        webbrowser.open('https://www.google.com.vn/',new = 2)
                        robot = "Ok, tôi sẽ bật lên cho bạn!"
                        break
                elif "Tạm biệt" in you:
                        robot = "OK! Tạm biệt bạn"
                        break
                elif "ngủ ngon" in you:
                        robot = "Ok! Ngủ ngon!"

                else:
                        robot = "Xin lỗi, Tôi không hiểu bạn đang nói gì, hãy thử lại!"

                print("Robot:" + robot)
                robot_mouth.say(robot)
                robot_mouth.runAndWait()
    elif "stop" in you:
            robot = "Ok, see you!"
            print("Robot:" + robot)
            robot_mouth.say(robot)
            robot_mouth.runAndWait()
            break
    else:
            robot = "Sorry, I don't understand you"

    print("Robot:" + robot)
    robot_mouth.say(robot)
    robot_mouth.runAndWait()