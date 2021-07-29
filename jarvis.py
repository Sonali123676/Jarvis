from sys import path
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

#importing the audio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[1].id)
engine.setProperty('voice', voices[0].id)

#define the speak func
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#define the wish funch which takes date time to wish 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir !!")
    else:
        speak("Good evening sir !!")

    speak("I am jarvis  !! How may I help you sir")

#It is used to take input audio and returns a query
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        
        audio = r.listen(source)

    try:
        print("recognizing......")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"User said : {query}")

    except Exception as e:
        print("Say that again please .....")
        return "None"
    return query


if __name__ == '__main__':
    # speak ("I am making jarvis")
    wishMe()
    while True:
        # Logic of jarvis
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia..")
                print(result)
                speak(result)
            except Exception as e:
                speak("please try again something went wrong")

        elif 'open youtube' in query:
            print("Opening youtube...")
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening google ....")
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'play music' in query:
            print("Playing music....")
            speak("Playing music")
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            a= []
            for i in range (0 , songs.__len__()):
                a.append(i)
            num = random.choice(a)
            speak(f"Playing {songs[num]}")
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'open vs code' in query:
            print("Opening vs code.....")
            speak("Opening vs code")
            path_vs = "C:\\Users\\umang\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path_vs)

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {time}")
            speak(f"Sir , the time is {time}")

        elif 'typing master' in query:
            path_type = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
            print("Opening typing master.....")
            speak("Opening typing master")
            os.startfile(path_type)

        elif 'code blocks' in query:
            path_blocks = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            print("Opening codeblocks.......")
            speak("opening codeblocks")
            os.startfile(path_blocks)

        elif 'chrome' in query:
            path_chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            print("Opening google chrome......")
            speak("Opening google chrome")
            os.startfile(path_chrome)

        elif 'open website' in query:
            speak("Which website you want to open")
            web = takeCommand().lower()
            speak(f"Opening {web}'s website")
            webbrowser.open(f"{web}.com")

        elif 'search' in query:
            speak("What do u want to search ")
            s = takeCommand().lower()
            speak("Here's what i found")
            webbrowser.open(s)

        elif 'movie' in query:
            print("Here are some movies in your pc :")
            speak("Here are some movies in your pc :")
            path_movies = "E:\\movies"
            movies = os.listdir(path_movies)
            print (movies)
            speak ("Which movie u want to watch")
            mov = takeCommand().lower()
            if 'man' in mov:
                print ("Playing IPMAN 4......")
                speak("playing IPman 4")
                os.startfile("E:\\movies\\Ip Man 4 The Finale 2019 1080p HC HDRip x264 1.8GB - MkvHub.Com")
            elif 'interstellar' in mov:
                print ("Playing Interstellar....")
                speak("playing Interstellar")
                os.startfile("E:\\movies\\Interstellar.2014.4K.UltraHD.BluRay.2160p.x264.DTS-HD.MA.5.1.AAC.5.1-POOP\\Interstellar.2014.4K.UltraHD.BluRay.2160p.x264.DTS-HD.MA.5.1.AAC.5.1-POOP.mkv")
            elif 'baby' in mov:
                print ("Playing Baby Driver....")
                speak("playing Baby Driver")
                os.startfile("E:\movies\Baby Driver (2017)\\Baby Driver.mkv")
            else :
                speak("something went wrong....    try again later")
    

        elif 'excel' in query:
            print ("Opening Excel .....")
            speak ("Opening Excel")
            path_excel = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.exe"
            os.startfile(path_excel)
          
        elif 'ms word' in query:
            print ("Opening MS Word .....")
            speak ("Opening MS Word")
            path_word = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.exe"
            os.startfile(path_word)

        elif 'hello' in query:
            speak('''Hello my name is jarvis ...,I can search anything u want ....,   i can open youtube , music ,  chrome ,
                google , vscode , codeblocks , typing master , websites ,word , excel , movies
                and can search in wikipedia and last but not the least 
                sir i can play games as well which are available in your pc ''')
            speak("and sir  if u want me to leave ....just say leave ")

        elif 'play games' in query:
            path_game = "C:\\Users\\umang\\Desktop\\Games"
            print("Here are some game available in your pc")
            speak("Here are some game available in your pc")
            games = os.listdir(path_game)
            print(games)
            speak("Which one u want to play")
            choice = takeCommand().lower()

            if 'cricket' in choice:
                print("Opening cricekt....")
                speak("Opening cricekt")
                os.startfile(os.path.join(path_game, games[0]))

            elif 'fifa' in choice:
                print("Opening fifa14.....")
                speak("Opening fifa14")
                os.startfile(os.path.join(path_game, games[1]))

            elif 'tekken' in choice:
                print("Opening tekken.....")
                speak("Opening tekken")
                os.startfile(os.path.join(path_game, games[2]))

            elif 'tesv' in choice:
                print("Opening TESV....")
                speak("opening TESV")
                os.startfile(os.path.join(path_game, games[3]))

        elif 'thank' in query:
            speak("My pleasure sir !!....  is there anything else i can do ?")
            y = takeCommand().lower()
            if y == "no" or y == "nope" :
                speak ("Thanks for your time sir !!")
                break

        elif 'leave' in query:
            # print ("Thanks for your time sir !!!!\nIf u need anything just call me \nHave a good day sir")
            speak(
                "Thanks for your time sir !!!! , If u need anything just call me , have a good day sir")
            break
