from project import get_level_difficulty, generate_hint, get_numbers, validation_answer, apps, start_level
import unittest
from unittest.mock import MagicMock
from gui.application import Application

class TestValidationAnswer(unittest.TestCase):

    def setUp(self):
        # Creating an instance of your application
        self.apps = Application(start_level)
        # Waiting for the 'frame3' object to be created
        self.apps.show_frame3()

        # Setting up mock objects after the 'frame3' is created
        self.apps.frame3 = MagicMock()
        self.apps.frame3.answer_var = MagicMock()

        #Setting the 'apps' object in your module to an instance of your application
        validation_answer.apps = self.apps
    
    def test_validation_answer_correct(self):
        # Setting the value of the 'answer_var' attribute
        self.apps.frame3.answer_var.get.return_value = 30

        result = validation_answer(self.apps, 5, 6)
        self.assertTrue(result)

    def test_validation_answer_wrong(self):
        # Setting the value of the 'answer_var' attribute
        self.apps.frame3.answer_var.get.return_value = 28

        result = validation_answer(self.apps, 5, 6)
        self.assertFalse(result)

    def test_validation_answr_exeption(self):
        # Setting the value of the 'answer_var' attribute
        self.apps.frame3.answer_var.get.return_value = "No"

        result = validation_answer(self.apps, 5, 6)
        self.assertFalse(result)   



def test_get_level_difficulty_easy():
    # Testing the function for the Easy level
    result = get_level_difficulty('Easy', 1).get_level
    expected_result = [1, 1, 1, 2, 2, 2, 2, 10, 10, 10] 
    assert result == expected_result


def test_get_level_difficulty_medium():
    #Testing the function for the Medium level
    result = get_level_difficulty('Medium', 1).get_level
    expected_result = [2, 2, 2, 3, 3, 4, 4, 5, 5, 5]
    assert result == expected_result


def test_get_level_difficulty_hard():
    # Testing the function for the Hard level
    result = get_level_difficulty('Hard', 1).get_level
    expected_result = [2, 2, 3, 3, 4, 5, 6, 7, 8, 9]
    assert result == expected_result


def test_generate_hint_multiple_numbers():
    first_number = 5
    secund_number = 3
    result = generate_hint(first_number, secund_number)
    expected_hint = f"Hint : {first_number} + {first_number} + {first_number} = "
    assert result == expected_hint


def test_generate_hint_single_number():
    first_number = 5
    secund_number = 1
    result = generate_hint(first_number, secund_number)
    expected_hint = f"Hint : {first_number}"
    assert result == expected_hint


def test_get_numbers():
    questions = {0: [8, 5], 1: [5, 5], 2: [2, 4], 3: [3, 5], 4: [6, 3]}
    question_counter = 0
    result = get_numbers(questions,question_counter)
    except_result = [8, 5]
    assert result == except_result


def test_get_number_multi_pair():
    questions = {0: [8, 5], 1: [5, 5], 2: [2, 4], 3: [3, 5], 4: [6, 3]}
    assert get_numbers(questions,2) == [2, 4]
    assert get_numbers(questions,3) == [3, 5]


if __name__ == '__main__':
    test_get_level_difficulty_easy()
    test_get_level_difficulty_medium()
    test_get_level_difficulty_hard()
    test_generate_hint_multiple_numbers()
    test_generate_hint_single_number()
    test_get_numbers()
    test_get_number_multi_pair()
