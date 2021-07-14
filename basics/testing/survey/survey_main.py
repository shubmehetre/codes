# import survey_class
from survey_class import AnonSurvey

question = "your fav football club?"

my_club = AnonSurvey(question)

# survey_class.AnonSurvey.show_question()
my_club.show_question()

while True:
    response = input("Answer: ")
    if response == 'q':
        break
    my_club.store_response(response)


# show results
my_club.show_results()

