<p align="center" dir="auto">
  <a>
    <img src="/resources/MultiPy.png" alt="MultiPy logo" width="200" height="200"  style="max-width: 100%;">
  </a>
</p>
<h1 align="center" tabindex="-1" dir="auto"><a class="anchor" aria-hidden="true"></a>MultiPy</h1>


<p align="center" dir="auto">
  Simple, intuitive, and educational mathematic game intended for kids.
  <br>
  <br>
  <a href="">Youtube video</a>
  ·
  <a href="requirements.txt">Request feature</a>
  ·
  <a href="https://github.com/mando984/MultiPy.git" rel="nofollow">Git hub</a>
  ·
  <a href="/resources/uml_diagram_MultiPy.pdf" rel="nofollow">Uml diagram</a>
</p>


### Table of content
* [Description](#description)
* [Prerequisites](#prerequest)
* [Installantion](#installation)
* [Running Apps](#running-apps)
* [Gameplay](#gameplay)
* [Code Structure](#code-structure)
* [Code Architecture](#code-architecture)


### Description 
***
*MultiPy* is an interactive game designed for learning multiplication up to 10. The game consists of five levels, each with five questions, and offers three difficulty levels. It generates random questions, tracks player scores, and ranks them on a leaderboard at the end of the game. 
It's implemented in Python, using Tkinter and ttkbootstrap for the graphical user interface.
The main challenge was implementing Tkinter using an object-oriented approach, following the MVC concept. 
The next upgrade will include adding sound effects, expanding the game to include division operations, and possibly addition and subtraction as well.

### Prerequisites
***
Python 3.x installed on your system.

Tkinter library installed (install using pip).

Ttkbootstrap library installed (install using pip).

### Installation
***
Install the Tkinter module and the ttkbootstrap module.
Clone or download this repository to your local machine.
Navigate to the project directory in your terminal or command prompt.
The root file is `project.py`.

### Gameplay
***
When the game starts, the `Main page` is displayed . The main page shows a rank table featuring the best players, as well as buttons for `Start Game` and `Quit Game`.

Main page:
![Main Page](resources/main_page_screenshot.png)



Upon starting the game, move to the `Second Page` and select the desired difficulty level (easy, medium, hard) and press `Next` button.

Second Page:
![Second Page](resources/second_page_screenshot.png)


On the `Third Page`, the status of the current level is displayed at the top of the screen. In the middle of the screen, the question, answer, and hint frame are displayed. On the bottom left, the combo is shown. To start the level, click the `Start Level` button. Answer the multiplication questions by entering the correct value and pressing the `Enter` key on the keyboard. Each time the player's answer is correct, the combo (the number of consecutive correct answers given by the player) increases by 5 and is added to the score. The score is displayed in the bottom right corner. During gameplay, a timer counts down as the level progresses. If the level finishes, the timer stops.

Third Page:
![Third Page](resources/third_page_screenshot.png)

When the player presses 'Enter' to submit their answer, feedback is displayed below the hint frame. There are two types of feedback: `Correct Answer` and `Wrong! a * b = c`.
If the answer is wrong, the combo resets to 1.

Third Page 2:
![Wrong Answer](resources/wrong_answer.png)


If the player's time is less than 75 seconds, they receive a `Bonus Level`.

Bonus Level:
![Bonus Level](resources/bonus_page_screenshot.png)

When the game finishes, players are directed to the `Fourth Page` where their score and time are displayed. On this page, players enter their name in an entry field. Upon submitting their name, the application places the player in a table and ranks them. Finally, players are returned to the main page.

Fourth Page:
![Fourth Page](resources/fourth_page_screenshot.png)


### Code Structure
***

<details>
<summary>Click to expand</summary>
<pre>
project/
|-- __init__.py
|-- project.py
|-- test_project.py
|-- requirements.txt
|-- README.md
|
|-- gui/
|   |-- __init__.py
|   |-- application.py
|   |-- main_page.py
|   |-- second_page.py
|   |-- third_page.py
|   |-- fourth_page.py
|
|-- data/
|   |-- __init__.py
|   |-- table.py
|   |-- rankList.csv
|   |-- easy.py
|   |-- medium.py
|   |-- hard.py
|   |-- score.py
|
|-- resources/
</pre>
</details>


1. **project**/

    **init. py**: Marks the directory as a Python package.

    **project. py**: Main file of the project containing core code and functions to run the project.

    **test_project.py**: Contains tests to verify the correctness of the project's code.

    **requirements.txt**: Lists Python packages and their versions required to execute the project.

    **README. md**: Contains project description, installation instructions, usage guidelines, and other important information.

2. **gui**/

    **init. py**: Marks the directory as a Python package.

    **application. py**: Initializes the application and manages its display.

    **main_page. py**, **second_page. py**, **third_page. py**, **fourth_page. py**: Contains code related to the main screens or pages of the application.

3. **data**/

    **init. py**: Marks the directory as a Python package.

    **table. py**: Contains code for processing or manipulating data tables.

    **rankList. csv**, **easy. py**, **medium. py**, **hard. py**, **score. py**: Contains various data or scripts used in the project, such as ranking data, score calculation scripts, etc.

4. **resources**/

    Contains various project resources such as images, icons, sounds, etc.

### Code Architecture
***



