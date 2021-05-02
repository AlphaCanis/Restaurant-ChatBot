# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class TimeCheck(Action):

    def name(self) -> Text:
        return "action_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        num = tracker.get_slot['hour']
        # print(entities)

        
            if num == '7':
                
                message = "You have reserved {} seats in our {} section for {}pm. Thanks!".format(nos,section,hour)
            elif num == '7:30':
                
                message = "You have reserved {} seats in our {} section for {}pm. Thanks!".format(nos,section,hour)  
            elif num == '8':
                
                message = "You have reserved {} seats in our {} section for {}pm. Thanks!".format(nos,section,hour)
            elif num == '8:30':
                
                message = "You have reserved {} seats in our {} section for {}pm. Thanks!".format(nos,section,hour)
            elif num == '9':
                
                message = "You have reserved {} seats in our {} section for {}pm. Thanks!".format(nos,section,hour)             

            elif num == '9:30':
                message = "You have reserved {} seats in our {} section for {}pm. Thanks!".format(nos,section,hour)
            elif num == '5':
                 message = "We are not open at that time. We are only open from 7pm to 10pm"  

            elif num == '4:30':
                message = "We are not open at that time. We are only open from 7pm to 10pm"   
            elif num == '3':
                message = "We are not open at that time. We are only open from 7pm to 10pm"                    


        dispatcher.utter_message(text=message)

        return []
