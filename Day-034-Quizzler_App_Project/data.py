import requests

# here we are using public API of open trivia data base to get new question. each time app is launched.
URL = "https://opentdb.com/api.php?amount=10&type=boolean"

quiz_data = requests.get(url=URL)
quiz_data.raise_for_status()
data  = quiz_data.json()

question_data = data["results"]
