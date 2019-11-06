# Multi-Choice Quiz Version 4.2

This program is a Multi-Choice Quiz which can be played by many different age groups. There are multiple Categories all ready added. These include Geography, Science, War, Movies and a Miscallaneous Category. As a user, you also have the ability to add your own Categories. There are also Profiles which can be created for each user. Each user has their own set of Highscores for each quiz. The quiz relies on two text files for its data. These are **profiles.txt** and **categories.txt** which store the information for the categories and the users profile data. A second python script named **text_file_converter.py** When the Program is exited, a new profile or quiz is added, or a quiz is ended the data currently stored by the program is written to these text files. A backup of this data is provided in the backup_data files which can be used to replace the data in the data in the two files. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine so that you can play this game.

### Prerequisites

What things you need to run the program and how to install them:

```
Python
PIP
Pillow
```

### Installing

A step by step series of examples that tell you how to get the program running.

First you must have Python installed. You can do this by visiting the [Python Website](https://www.python.org/downloads/). Then the latest version of python can be installed. When downloading this you can also select to install PIP.

Once Python and PIP are installed we will need to install the different packages which are needed for this program. To do this will be using the command shown below in the command prompt which will allow us to install all the different packages we will need.

```
pip install [Package Name]
```

To install Pillow the command below can be entered into the command prompt.

```
pip install PIL
```

Once all these packages are installed you are able to run the program using the batch file (.bat).

```
run_v4.2.bat
```

## Using the Program

Using this program is very simple. These instructions are also displayed in the quiz.

1. If you are a returning user select your profile from the menu on the right
2. If you are a new user you can create a new profile from the menu on the right by clicking the corresponding “+”
3. Select which Category you would like to be tested on. You can create your own Category using the corresponding “+”.
4. Then click “Play Quiz”. Which will begin the quiz.
5. Your high scores will be saved for each quiz you play and can also be seen on the right.
______
When adding a quiz you can enter the Category Name and then enter all the questions you wish to include in the quiz. Then by clicking confirm a pop-up will appear stating that the Category was added. Reason for failure will either be invalid entries such as fields being left blank or the default text being used.````````````
``
## Using the Text Files

The two text files are quite easy to understand and therefore edit if you wish to. There are a few things which must be kept in mind when doing this. **There must be  a ": " infront of every piece of data.** As this is what is the string which is used by the program to identify the difference between the data and the subscript.

For example:

```
Category: Geography
Question 1: What is the capital of Mongolia?
Correct Answer: Ulaanbaatar
Incorrect Answer 1: Dharkhan
Incorrect Answer 2: Erdene
Incorrect Answer 3: Bayankhongor
```

Would be interpreted by the program as:

```
Geography
What is the capital of Mongolia?
Ulaanbaatar
Dharkhan
Erdene
Bayankhongor
```

It will read this text file and convert it into a list which will be used by the main program to run the quiz. When the program writes data from the quiz it is also in the same format to what is read.

## Versions

All the different versions are provided. And can be run using _**py version_name.py**_ in the command prompt. It is recommended that the newest version is used as some of these versions may be unstable.

##### Version 1.0

* This is the very first functional quiz without GUI where the user enters a letter to answer the question they are asked. It has basic functionality and includes every single question and only uses classes as a complex technique. In the next version I intend to implement some sort of GUI. Which will allow the user to select the category they would like to access and will have buttons to answer the question instead of inputting a letter.

##### Version 2.0

* This is the first version of the GUI quiz. In this version I will add the very first GUI based quiz. The user will be able to access a set category of the quiz and will receive a score for that category at the end.
* Using Tkinter to create a GUI
* I have removed the method in the Questions class which was used to ask each questions

##### Version 2.1

* This is the second version of the GUI implementation of this quiz.
* This version will track the users score in the GUI window instead of outputting at the end
* The category the user uses is still hardcoding but this will be change to a combobox in the upcoming versions
* Added a temporary Entry box in the place as the users name label so that they can enter their own name.
* Implemented an exit button which can be used to exit out of the quiz and the code

##### Version 2.2

* This is because on some lower resoltion screens the window would not fit
* It is based on the original design and all the widgets, frames, etc. Are resized based on these dimensions but with an aspect ratio relevant to the users screen. For example if they have a 1920x1080 screen the 1400x940 original will resize everything to fit this screen
* It will also do this for all the font to make sure that this also fits within the widgets.
* Added Image and ImageTK so that the image I am using for the background is resized.
* NOTE: The Image and ImageTk must be installed using PIP so that the background image can be resized

##### Version 2.3

* In this version I have added a restart quiz button which will let the user restart the quiz.
* I have also implemented a combo box used to select the category of the quiz. When the restart button is pressed the quiz will restart and the new category will be loaded

##### Version 3.0

* In this version I have added the use of the text_file_converter module which I developed this will mean that a large list does not need to be stored and instead a text file can be used to store all the data.
* By doing this the user does not have to access the python file to edit the questions
* It is also laid out in a much more user friendly format instead of one large list which most people would not understand.

##### Version 3.1

* In this version I made a major bug fix. In the previous versions since I am  shuffling a list and adding the correct answer to it meaning a total of 4  possible answers. When the quiz is restarted the correct answer gets added  to this list again each time meaning the correct answer shows up again and  therefore the chance of the correct answer showing up increases.
* This makes it significantly easier to get 100 points in the quiz as all you  have to do is restart it multiple times.
* I also found that the quiz would completely skipped through the user getting the  answer correct and go to the next question. It also did this when they ran  out of tries and instead of showing an output it would skip forward. This  was because mainloop was not set in place so it could not update.
* I also removed delay on some things to make the quiz seem more responsive.

##### Version 4.0

* In this version I am adding the use of Profiles. These will eventually be saved  in a text file so that the values can be saved when the user exits the quiz.
* As this quiz is very casual and not competitive it should not matter if they find  a method to alter their scores. However, later I may choose to use a less  common file type for the profiles such as JSON as it is not as easy to edit
* In this version all I am doing is creating the Profile Class and creating a window  which will show up before the actual quiz. In this version the quiz has become  unplayable but this is done to test the profiles update.
* In this version I have switched to a newer version of the Text File Converter  module which has the ability to transfer the profile text file to a list
* Currently, users are unable to create new profiles but this will be implemented soon  and must be done through the text file
* Fixed a bug which would let the user crash the quiz. If the confirm answer button was  pressed when the user ran out of tries or got the answer correct the quiz would  either output an error or crash the quiz. I fixed this by disabling the button before the time.sleep command which meant the button could not be pressed until  the next one was created.
* Currently, the high scores will update but they are not written to the text file so progress is not saved. (This will be resolved in future updates)

##### Version 4.1

* In this version I will be adding the ability to add profiles. The only input for this will be the username and it must have no spaces. Everything else will be generated on its own.
* I will also be adding high scores when the quiz is being displayed. I will take the data of each player and sort the high scores of that quiz from highest to lowest displaying the username and the corresponding high score.
* Another change will be updating text files each time a quiz finishes or when the user decides to exit. The new profiles.txt file will update using the new data so that it will be saved for the next time the user starts the game

##### Version 4.2

* In this version I will also be adding the ability for the user to add their own categories. This means that they will be able to create their own quizzes.
* Since new categories are added a new menu is needed so that they can interact and all the questions and answers for their new category.
* I will also need to add this category to each profile since it will need a location to actually save all this new data.



### Programmer: Bhumik Patel