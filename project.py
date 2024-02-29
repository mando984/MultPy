""" 1. Start Level Functionality:
        When the player clicks "Start level," the start_level() function is executed.
        The update_label_text() function is called to update the level label.
            If the current level is greater than 5:
                If the sum of all time is less than 75, run bonus_frame.
                Else, run frame_4.
            Else, increase the current level.
        The start_level() function then runs the play_one_round() function.

    2. Playing One Round:
        Inside play_one_round(), there's a counter to keep track of the question status.
        Loop 5 times:
            Call get_numbers() to generate a pair of numbers.
            Generate a question.
            Display the question.
            Wait for the user's answer.
            Upon receiving an answer, proceed to the process_answer() function.

    3. Processing the Answer:
        Inside process_answer():
            Call validation_answer() to compare the user's input and the correct result and display feedback.
            Update the combo and score through the Score class.
            Update UI elements such as score number label and combo number level.
            Clear the entry field for the next question.
            Repeat the round if the counter is less than 5.
            Restart widgets and prepare for the next level.
            Disable the "Press Enter" option and input from the keyboard.

    4. Waiting for the Next Level:
        Wait for the player to click "Start level" to play the next level.

    This flow seems to handle the gameplay loop, including level progression, question generation,
      answer processing, and UI updates. You might need to implement functions like get_numbers(),
      validation_answer(), and the Score class methods to complete the functionality.
    Additionally, consider implementing error handling and user
      feedback mechanisms for a smoother gaming experience.
   """



from gui.application import Application
from data.easy import Easy
from data.medium import Medium
from data.hard import Hard

from ttkbootstrap import Style
import tkinter as tk

import random
import time
import math


MAX_QUESTIONS = 5
DELAY_HIDE_MESSAGE = 700
DELAY_WRONG_MESSAGE = 1500
DEFAULT_TEXT_SIZE = 12


apps = None
current_level = 1
question_counter = 0
questions = {}
start_time = None
size_text = 12 # The variable tracks the size of the text of combo_number_label.
enter_pressed = None  # Variable that tracks whether the Enter key is pressed


def main():
    global apps
    apps = Application(start_level)
    apps.start_application()


def start_level():
    global questions
    global start_time
    questions = generate_quest(current_level)  # generat quest
    start_time = time.time()  # keep start time
    apps.frame3.level_label.config(text=update_label_text())
    apps.frame3.start_button.config(text="Play")
    apps.frame3.start_button['state'] = 'disabled'
    apps.frame3.answer_entry.configure(state=tk.NORMAL)
    apps.frame3.quest_frame.grid(row=3, column=0, columnspan=3, pady=10)

    play_one_round()


def play_one_round():
    global enter_pressed
    global question_counter
    global questions
    enter_pressed = tk.BooleanVar()

    for _ in range(MAX_QUESTIONS):
        numbers = get_numbers(questions, question_counter)
        first_number = numbers[0]
        second_number = numbers[1]
        question = f"{first_number} * {second_number} =" # generates a question view
        apps.frame3.quest_label.config(text=question)  # display question
        apps.frame3.answer_entry.grid(row=0, column=1, sticky="w", padx=10)
        hint = generate_hint(first_number, second_number)
        apps.frame3.help_label.config(text=hint)  # display hint
        apps.frame3.answer_entry.focus()
        # when user give answer, and press enter
        apps.frame3.answer_entry.bind('<Return>', process_answer)
        apps.frame3.wait_variable(enter_pressed)

    # When user finish the level, disable the 'Press Enter' option.
    apps.frame3.answer_entry.unbind("<Return>")
    # Disable input from the keyboard.
    apps.frame3.answer_entry.configure(state=tk.DISABLED)
    reset_widgets()


# Restart widgets and prepare to next level.
def reset_widgets():
    global start_time
    global current_level

    # stop time and subtract from start time
    elapsed_time = math.ceil(time.time() - start_time)
    apps.score.time = elapsed_time  # add time to instance class Score
    current_level += 1  # increasing the level
    apps.frame3.quest_frame.grid_forget()
    apps.frame3.level_label.config(text="")
    apps.frame3.start_button.config(text=f"Start level {current_level}")
    apps.frame3.start_button['state'] = 'enable'
    update_label_text()


# handle user answer
def process_answer(event):
    global apps
    global enter_pressed
    global question_counter
    global size_text
    global questions
    numbers = get_numbers(questions, question_counter)
    first_number = numbers[0]
    second_number = numbers[1]

    answer = validation_answer(
        apps,
        first_number,
        second_number)  # return True or False
    apps.score.answer(answer)  # Forward the check to the Score class.

    if answer:
        apps.frame3.combo_number_label.config(
            text=apps.score.combo, font=(
                "Helvetica", combo_text_resize()))
        apps.frame3.feedback_result_label.config(
            text="Correct Answer", foreground="#CA9A07")
        # After a delay, hide the message for 700 ms.
        apps.frame3.feedback_result_label.after(
            DELAY_HIDE_MESSAGE, hide_mesage)
    elif answer == False:
        size_text = DEFAULT_TEXT_SIZE
        apps.frame3.combo_number_label.config(
            text=apps.score.combo, font=(
                "Helvetica", DEFAULT_TEXT_SIZE))
        apps.frame3.feedback_result_label.config(
            text=f"Wrong!  {first_number}  *  {second_number} = {first_number * second_number} ",
            foreground="red")
        apps.frame3.feedback_result_label.after(
            DELAY_WRONG_MESSAGE, hide_mesage)

    apps.frame3.score_number_label.config(text=apps.score.score)
    # Clear the entry field for the next question
    apps.frame3.answer_var.set("")
    question_counter += 1
    enter_pressed.set(True)  # Change the variable when the user presses Enter.


# Check the user's answer and return true or false."
def validation_answer(apps, first_number, second_nubmer):

    try:
        user_answer = int(apps.frame3.answer_var.get())  # get users answer
        result = first_number * second_nubmer
        if result == user_answer:
            return True
        else:
            return False
    except ValueError:
        return False


def hide_mesage():
    global question_counter
    apps.frame3.feedback_result_label.config(text="")


# change size of combo text
def combo_text_resize():
    global size_text
    size_text += 1
    return size_text


def get_numbers(questions, question_counter):
    numbers = questions.get(question_counter)  # one pair of numbers
    return numbers


def generate_quest(current_level):
    """
    Generates two lists of 5 numbers for a given level.
    Parameters:
    - current_level, difficulty
    Returns:
    A dictionary containing five pairs of two numbers.
    """
    first_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_numbers = shuffle(first_numbers)
    first_numbers = first_numbers[:5]
    second_numbers = get_level_difficulty(
        apps.difficulty, current_level).get_level
    second_numbers = shuffle(second_numbers)
    second_numbers = second_numbers[:5]
    pairs = {}  # create dictionary for store all pair numbers
    for i in range(5):
        pair = [first_numbers[i], second_numbers[i]]
        pairs[i] = pair
    return pairs


# returns string to help_label
def generate_hint(first_number, second_number):

    if second_number == 1:  # when multiply with 1, then have single number
        return f"Hint : {first_number}"
    else:
        # when print hint reduce hint becous one "+" is too much
        reduct_secund_nubmer = second_number - 1

    help = f"{first_number} + " * reduct_secund_nubmer  # multipy hint
    # add one more number to complite hint
    help = f"Hint : {help}{first_number} = "
    return help


def shuffle(mylist):
    random.shuffle(mylist)
    return mylist


def get_level_difficulty(difficulty, level):
    """
    Returns a list of numbers from the selected class. Each class stores 5 lists
    Class Easy,Medium and Hard placed in dir data.
    """
    match difficulty:
        case 'Easy':
            return Easy(level)
        case 'Medium':
            return Medium(level)
        case 'Hard':
            return Hard(level)


def reset_frame2():
    # Resetovanje vrednosti na prazan string
    apps.frame2.difficulty_var.set("")
    apps.frame2.next_button.config(state='disabled')


def update_label_text():
    global size_text
    global current_level
    global questions
    global apps
    global question_counter
    question_counter = 0  # reset counter

    # Tracks when the game will finish.
    if current_level > 5:
        if current_level > 6:  # If the player finishes the bonus level.
            reset_frame2()
            apps.show_frame4()
            size_text = DEFAULT_TEXT_SIZE
            current_level = 1
        else:
            if apps.score.time <= 75:
                size_text = DEFAULT_TEXT_SIZE
                apps.style = Style(theme="united")  # Changing theme
                apps.frame3.header_label.config(text="MultiPy Bonus")
                apps.score.answer(False)  # Reset combo in Score class.
                apps.frame3.combo_number_label.config(text="1", font=(
                    "Helvetica", DEFAULT_TEXT_SIZE))  # Reset combo on display
                apps.frame3.start_button.config(
                    text=f"Start Bonus level", command=start_level)
                apps.frame3.start_button['state'] = 'enable'
                return (f"Level Bonus")

        reset_frame2()
        current_level = 1
        # provide instance score to page 4
        apps.frame4.init_score_instance(score_instance=apps.score)
        size_text = DEFAULT_TEXT_SIZE
        apps.show_frame4()
    else:
        return (f"Level {current_level}")


if __name__ == "__main__":
    main()
