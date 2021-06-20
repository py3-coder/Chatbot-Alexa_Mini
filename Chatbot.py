

import speech_recognition as sr
import pyttsx3
import pywhatkit as pykit
import datetime
import wikipedia
import pyjokes
import requests, json , sys


r =sr.Recognizer()

engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
def user_command():
    try :
        with sr.Microphone() as source:
            print('Start Speaking......')
            audio =r.listen(source)
            command =r.recognize_google(audio)
            command =command.lower()
            if 'Saurabh' in command:
                command = command.replace('Saurabh', '') 
                print(command)
    except:
        pass
    return command




def weather(city):
    # Enter your API key here 
    api_key = "XXXXXXXXXXXXXXXXXXXX"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = city
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        #z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = [current_humidiy,current_pressure,current_temperature]
        
        return weather_description
    


def run_bot():
    command =user_command()
    if 'play' in command :
        song = command.replace('play','')
        print('Playing' + song)
        engine_talk('Playing'+song)
        pykit.playonyt(song)
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%I:%M %p')
        now = datetime.date.today().strftime("%B %d, %Y")
        engine_talk('The current time is '+time)
        engine_talk('Today' +now)
    elif 'who is' in command:
        name =command.replace('who is','')
        information =wikipedia.summary(name,10)
        print(information)
        engine_talk(information)
    elif 'define' in command:
        defi =command.replace('define','')
        defi =wikipedia.summary(defi,10)
        print(defi)
        engine_talk(defi)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'weather' in command:
        print('Please tell your city name:')
        engine_talk('Please tell the name of the city')
        city = user_command()
        
        weather_api = weather(city)
        weather_api[0] =(weather_api[0]-32)*5/9
        
        engine_talk(str(round(weather_api[0],3) )+ 'degree calsius' )
        engine_talk(str(weather_api[1]) + 'pascal' )
        engine_talk(str(weather_api[2]) + '% humidity' )
    elif 'send message' in command:
        pykit.sendwhatmsg("+91(xxxxxxx)","hi saurabh I am your bot",00,42)
        engine_talk('Message sended')
    elif 'Search' in command:
        find =command.replace('Search','')
        print(find)
        pykit.search(find)
    elif 'stop' in command:
        engine_talk('Thanks Its Saurabh Bot..Good Luck')
        sys.exit()
    else:
        engine_talk('I am not able to hear you')
while True:
    run_bot()
