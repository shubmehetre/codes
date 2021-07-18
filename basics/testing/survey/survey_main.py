# import survey_class
import survey_class

question = "your fav football club?"

my_club = survey_class.AnonSurvey(question)

# survey_class.AnonSurvey.show_question()
my_club.show_question()

while True:
    response = input("Answer: ")
    if response == 'q':
        break
    my_club.store_response(response)

print()
# show results
my_club.show_results()

