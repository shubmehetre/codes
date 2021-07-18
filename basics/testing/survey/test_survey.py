import unittest
import survey_class
# import survey_main

class TestSurvey(unittest.TestCase):

    def setUp(self) -> None:
        """
        creating a survey and a set of sampple responses
        """
        question = 'fav food?'
        self.survey_class_obj = survey_class.AnonSurvey(question)
        self.responses = ['chinese', 'italian', 'indian']

        return super().setUp()

    def test_single_response(self):

        # sending/storing first element of self.responses list from setUp() into store_response
        self.survey_class_obj.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.survey_class_obj.responses[0])

    def test_multiple_response(self):

        # storing sample responses using store_response method
        for response in self.responses:
            self.survey_class_obj.store_response(response)

        # checking if response properly stored in the list
        for response in self.survey_class_obj.responses:
            self.assertIn(response, self.survey_class_obj.responses)

if __name__ == "__main__":
    unittest.main()