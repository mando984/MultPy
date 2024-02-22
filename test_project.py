from project import get_level_difficulty, generate_hint, get_numbers, validation_answer, apps, start_level
import unittest
from unittest.mock import MagicMock
from gui.application import Application

class TestValidationAnswer(unittest.TestCase):

    def setUp(self):
        # Stvaranje instance vaše aplikacije
        self.apps = Application(start_level)
        # Čekanje da se stvori 'frame3' objekt
        self.apps.show_frame3()

        # Postavljanje mock objekata nakon što se stvori 'frame3'
        self.apps.frame3 = MagicMock()
        self.apps.frame3.answer_var = MagicMock()

        # Postavljanje apps objekta u vašem modulu na instancu vaše aplikacije
        validation_answer.apps = self.apps
    
    def test_validation_answer_correct(self):
        # Postavljanje vrijednosti 'answer_var' atributa
        self.apps.frame3.answer_var.get.return_value = 30

        result = validation_answer(self.apps, 5, 6)
        self.assertTrue(result)

    def test_validation_answer_wrong(self):
        # Postavljanje vrijednosti 'answer_var' atributa
        self.apps.frame3.answer_var.get.return_value = 28

        result = validation_answer(self.apps, 5, 6)
        self.assertFalse(result)

    def test_validation_answr_exeption(self):
        # Postavljanje vrijednosti 'answer_var' atributa
        self.apps.frame3.answer_var.get.return_value = "No"

        result = validation_answer(self.apps, 5, 6)
        self.assertFalse(result)   



def test_get_level_difficulty_easy():
    # Testiranje funkcije za nivo Easy
    result = get_level_difficulty('Easy', 1).get_level
    expected_result = [1, 1, 1, 2, 2, 2, 2, 10, 10, 10]  # Pretpostavljamo da klasa Easy ima listu brojeva od 1 do 5 za prvi nivo
    assert result == expected_result

def test_get_level_difficulty_medium():
    # Testiranje funkcije za nivo Medium
    result = get_level_difficulty('Medium', 1).get_level
    expected_result = [2, 2, 2, 3, 3, 4, 4, 5, 5, 5]  # Pretpostavljamo da klasa Medium ima listu brojeva od 6 do 10 za prvi nivo
    assert result == expected_result

def test_get_level_difficulty_hard():
    # Testiranje funkcije za nivo Hard
    result = get_level_difficulty('Hard', 1).get_level
    expected_result = [2, 2, 3, 3, 4, 5, 6, 7, 8, 9] # Pretpostavljamo da klasa Hard ima listu brojeva od 11 do 15 za prvi nivo
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



# Pokretanje testova
if __name__ == '__main__':
    test_get_level_difficulty_easy()
    test_get_level_difficulty_medium()
    test_get_level_difficulty_hard()
    test_generate_hint_multiple_numbers()
    test_generate_hint_single_number()
    test_get_numbers()
    test_get_number_multi_pair()
    print("Svi testovi su uspješno izvršeni.")
