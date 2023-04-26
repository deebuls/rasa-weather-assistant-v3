# https://rasa.com/docs/rasa/core/actions/#custom-actions/
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionGetWeather(Action):
    """ Return today's weather forecast"""

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):

        city = tracker.get_slot('location')
        print ("Requested city : ", city)
        api_token = "85a4e3c55b73909f42c6a23ec35b7147"
        url = "https://api.openweathermap.org/data/2.5/weather"
        payload = {"q": city, "appid": api_token, "units": "metric", "lang": "en"}
        response = requests.get(url, params=payload)
        print ("Response ok", response.ok)
        print ("response text", response.text)
        if response.ok:
            description = response.json()["weather"][0]["description"]
            temp = round(response.json()["main"]["temp"])
            cityGR = response.json()["name"]

            msg = f"The current temperature in {cityGR} is {temp} degree Celsius. Today's forecast is {description}"
        else:
            msg= "I'm sorry, an error with the requested city as occured."+response.text


        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]
