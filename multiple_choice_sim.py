class MultipleChoice:
    def __init__(self, choices, questions, point_correct, point_incorrect):
        self.choices = choices
        self.questions = questions
        self.point_correct = point_correct
        self.point_incorrect = point_incorrect

class Student:
    def __init__(self, knowledge, slip_correct, slip_incorrect):
        self.knowledge = knowledge
