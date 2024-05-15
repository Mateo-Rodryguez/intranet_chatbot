
from typing import Any, Text, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa import dialogue

class UtterSecondUtterance(Action):
    def name(self):
        return "utter_second_utterance"
    def run(self,dispatcher,tracker,domain):
      #customizing my response here
        response = "I understand it might be frustrating. Let's try something else."
        dispatcher.utter_message(text=response)
        return []

class ActionCheckInternetConfirmation(Action):

    def name(self) -> Text:
        return "action_check_internet_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Okay, let's troubleshoot your internet issue. Say 'yes' if you want to proceed.")
        return []  # No need to return any events



# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
