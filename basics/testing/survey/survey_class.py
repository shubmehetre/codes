class AnonSurvey:
    """Anonymous survey"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """shows question on call"""
        print(self.question)
        # print("press q to quit")

    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print("Survey Results:")
        for i in self.responses:
            print(f"- {i}")

