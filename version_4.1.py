# Programmer: Bhumik Patel
# Program: Multi-Choice Quiz
# Version: 4.1

# Purpose:
# This is a Multi-Choice Quiz which will reflect to society and is made for all
# ... people who would like to challenge themselves. It will have multiple
# ... Categories so that it can relate to a wider range of people.


# In this version I will be adding the ability to add profiles. The only input for
# ... this will be the username and it must have no spaces. Everything else will
# ... be generated on its own.
# I will also be adding high scores when the quiz is being displayed. I will take
# ... the data of each player and sort the high scores of that quiz from highest
# ... to lowest displaying the username and the corresponding high score.
# Another change will be updating text files each time a quiz finishes or when
# ... the user decides to exit. The new profiles.txt file will update using the
# ... new data so that it will be saved for the next time the user starts the game


# Importing Modules
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from text_file_converter import *
import tkinter.messagebox
import random
import time
import operator

# Creating Colour Scheme Constants
BACKGROUND_COLOR1 = "#27697F"
BACKGROUND_COLOR2 = "#32A4C6"
BORDER_COLOR = "#274257"
TEXT_COLOR = "#F2F2F2"

# Setting Constants
DELAY = 0.5
FULL_POINTS = 10
MOST_POINTS = 7
SOME_POINTS = 3
NO_POINTS = 0
ORIGINAL_WIDTH = 1400
ORIGINAL_HEIGHT = 940


# Creating the Category Class
class Category:
    """The Class is used to store all the different Categories for the quiz"""
    # Setting global class variables
    num_of_questions = 0
    num_of_categories = 0
    categoryNames = []

    def __init__(self, categoryName, questionList):
        """This function is run when an instance of the Category class is created
        :param categoryName: Name of the Category
        :param questionList: A list of questions, their answers and incorrect answers
        """
        # Defining the category name parameter as an attribute of the class
        self.categoryName = categoryName
        # Defining the parameter providing list of questions as an attribute of the class
        self.questionList = questionList
        # Creating an empty list to store the instances of the questions
        self.questions = []
        # This will loop through every item in the questionList attribute
        for question in self.questionList:
            # This will append and instance of the question to the questions attribute
            self.questions.append(Questions.from_list(question))
        # This will add 1 to specify the number of categories stored in the class
        Category.num_of_categories += 1
        # This will add the number of items in the questionList to specify the number of question in the class
        Category.num_of_questions += int(len(self.questionList))
        # Adding the category name to a list of categories
        Category.categoryNames.append(categoryName)

    def createQuizWindow(self, quizMaster, username):
        """In this method a GUI window will be created for the Quiz
        :param quizMaster: This is the Tk() window
        """
        # This attribute is used to allow the quiz to start so is set to False by default
        self.endQuiz = False
        # Here the quizMaster and the username is being saved as an attribute so it can be
        # ... accessed by methods using the self parameter throughout the class
        self.quizMaster = quizMaster
        self.username = username
        # Here I am using the information I have to make it easy to define the instances for the category and profile
        userInstance = Profiles[Profile.profileNames.index(username)]
        categoryInstance = Category.categoryNames.index(self.categoryName)
        # Here I am opening the image using the Image library
        self.background = Image.open("images/background.png")
        # I am then resizing the image to the correct height and width and enabling ANTIALIASING
        self.background = self.background.resize((width, height), Image.ANTIALIAS)
        # Creating a PhotoImage variable using the resized background image
        self.backgroundImageVar = ImageTk.PhotoImage(self.background)
        # Creating a label with the background image
        self.backgroundImage = ttk.Label(self.quizMaster, image=self.backgroundImageVar)
        # Placing the background image at 0,0
        self.backgroundImage.place(x=0, y=0)
        # Creating a Frame for the category title which will be used as the border
        self.categoryFrame = Frame(self.quizMaster, bg=BORDER_COLOR)
        """Placing the frame at 50,50 with a width of 1300 and a height of 150
        From here everything which is placed must have its width and height along
        with the coordinate it is placed at. This is done by the original
        width/height by the new width/height and then by the window size"""
        self.categoryFrame.place(x=(width * 50) / ORIGINAL_WIDTH, y=(height * 50) / ORIGINAL_HEIGHT,
                                 width=(width * 1300) / ORIGINAL_WIDTH, height=(height * 150) / ORIGINAL_HEIGHT)
        # Creating a String Variable for the category text
        self.categoryTextVar = StringVar()
        # This will set the string variable to the category name
        self.categoryTextVar.set(self.categoryName)
        # A Label is created using the previously created StringVar and is also formatted
        self.categoryTextLabel = Label(self.categoryFrame, textvariable=self.categoryTextVar, bg=BACKGROUND_COLOR1,
                                       fg=TEXT_COLOR, font=("Arial", int((height * 80) / ORIGINAL_HEIGHT)),
                                       padx=(width * 14) / ORIGINAL_WIDTH, anchor="n")
        # The Label is then placed in the recently created frame at 6,6
        # With a width and height slightly less to show the border so that the frame acts as a border
        self.categoryTextLabel.place(x=(width * 6) / ORIGINAL_WIDTH, y=(height * 6) / ORIGINAL_HEIGHT,
                                     width=(width * 1288) / ORIGINAL_WIDTH, height=(height * 138) / ORIGINAL_HEIGHT)
        # Here a frame is created to display information
        # This will not be used at this stage and is for future use
        self.infoFrame = Frame(self.quizMaster, bg=TEXT_COLOR)
        # This frame is then placed in the appropriate position with the correct height and width
        self.infoFrame.place(x=(width * 950) / ORIGINAL_WIDTH, y=(height * 250) / ORIGINAL_HEIGHT,
                             width=(width * 400) / ORIGINAL_WIDTH, height=(height * 640) / ORIGINAL_HEIGHT)
        # Here a frame for the username is created
        self.userNameFrame = Frame(self.infoFrame, bg=BORDER_COLOR)
        # It is then placed correctly so that it can act as a border
        self.userNameFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 18) / ORIGINAL_HEIGHT,
                                 width=(width * 364) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT, )
        # A string var is created to store the username
        self.userNameVar = StringVar()
        # It is set to a default of 2 spaces so that it is aligned with the other labels
        self.userNameVar.set(username)
        # I create an entry box for the username
        self.userNameLabel = Label(self.userNameFrame, textvariable=self.userNameVar, bg=BACKGROUND_COLOR1,
                                   fg=TEXT_COLOR, font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                   justify='left', anchor="w", padx=(width * 10) / ORIGINAL_WIDTH,
                                   pady=(height * 10) / ORIGINAL_HEIGHT)
        # This is then placed in the corect position so that the user is able to enter their username
        self.userNameLabel.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                 width=(width * 356) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        # This is setting the starting score of the user
        self.totalScore = 0
        # I am then creating a frame which is used for the user score
        self.userScoreFrame = Frame(self.infoFrame, bg=BORDER_COLOR)
        # This frame is placed below the username section
        self.userScoreFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 98) / ORIGINAL_HEIGHT,
                                  width=(width * 364) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        # A stringvar is created which will store the users score
        self.userScoreVar = StringVar()
        # By default this is set to show that the user has a score of 0
        self.userScoreVar.set("Score: {}".format(0))
        # A label is created to display the users score
        self.userScoreLabel = Label(self.userScoreFrame, textvariable=self.userScoreVar, bg=BACKGROUND_COLOR1,
                                    fg=TEXT_COLOR, font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                    padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                    anchor="w")
        # This is then placed within the user score frame
        self.userScoreLabel.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                  width=(width * 356) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)

        # Here I am creating a frame which will be used for the highscores border and then placing it
        self.highScoresOuterFrame = Frame(self.infoFrame, bg=BORDER_COLOR)
        self.highScoresOuterFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 178) / ORIGINAL_HEIGHT,
                                        width=(width * 364) / ORIGINAL_WIDTH, height=(height * 364) / ORIGINAL_HEIGHT)
        # Here I am creating a frame which will be used for the users highscores and placing it
        self.highScoresInnerFrame = Frame(self.highScoresOuterFrame, bg=BACKGROUND_COLOR2)
        self.highScoresInnerFrame.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                        width=(width * 356) / ORIGINAL_WIDTH, height=(height * 356) / ORIGINAL_HEIGHT)
        # Creating a label for the category title and placing it
        self.highScoreTitleLabel = Label(self.highScoresInnerFrame, text="High Scores", bg=BACKGROUND_COLOR2,
                                         fg=BORDER_COLOR,
                                         font=("Arial", int((width * 18) / ORIGINAL_WIDTH), "bold", "underline"),
                                         padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                         anchor="center")
        self.highScoreTitleLabel.place(x=(width * 8) / ORIGINAL_WIDTH, y=(height * 8) / ORIGINAL_HEIGHT,
                                       width=(width * 336) / ORIGINAL_WIDTH, height=(height * 32) / ORIGINAL_HEIGHT)

        # Creating a label for the highscore title and placing it
        self.highscoreTitleLabel = Label(self.highScoresInnerFrame, text="1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.",
                                         bg=BACKGROUND_COLOR2, fg=TEXT_COLOR,
                                         font=("Arial", int((height * 18) / ORIGINAL_HEIGHT), "bold"),
                                         padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                         anchor="center")
        self.highscoreTitleLabel.place(x=(width * 8) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                                       width=(width * 40) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
        # Creating a frames to be used to help the user differentiate between the different labels
        self.dividerFrameLeft = Frame(self.highScoresInnerFrame, bg=BORDER_COLOR)
        self.dividerFrameLeft.place(x=(width * 63) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                                    width=(width * 4) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
        self.dividerFrameRight = Frame(self.highScoresInnerFrame, bg=BORDER_COLOR)
        self.dividerFrameRight.place(x=(width * 293) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                                     width=(width * 4) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
        # Creating string vars for the users username and their corresponding high score
        self.userNamesLabelVar = StringVar()
        self.userScoresLabelVar = StringVar()
        # This function will be used to set these String Var so that they can be used with their corresponding labels
        self.set_high_score_data()
        # Creating a label for the categories placing it
        self.userNamesLabel = Label(self.highScoresInnerFrame, textvariable=self.userNamesLabelVar,
                                    bg=BACKGROUND_COLOR2, fg=TEXT_COLOR,
                                    font=("Arial", int((height * 18) / ORIGINAL_HEIGHT), "bold"),
                                    padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                    anchor="center")
        self.userNamesLabel.place(x=(width * 73) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                                  width=(width * 210) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
        self.userScoresLabel = Label(self.highScoresInnerFrame, textvariable=self.userScoresLabelVar,
                                     bg=BACKGROUND_COLOR2, fg=TEXT_COLOR,
                                     font=("Arial", int((height * 18) / ORIGINAL_HEIGHT), "bold"),
                                     padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                     anchor="center")
        self.userScoresLabel.place(x=(width * 303) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                                   width=(width * 45) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
        # Creating a frame for the return button and placing the frame
        self.returnFrame = Frame(self.infoFrame, bg=BORDER_COLOR)
        self.returnFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                               width=(width * 174) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        # Creting a button within the returnFrame used to return to the main menu
        self.returnButton = Button(self.returnFrame, text="Go Back", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                                   font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                   padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                   relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                                   command=self.go_back)
        # Placing the button in the correct position
        self.returnButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                width=(width * 166) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        # A Frame is created for the border of the exit button which will exit the game
        self.exitWindowFrame = Frame(self.infoFrame, bg=BORDER_COLOR)
        # This Frame is then placed in the bottom right of the info frame
        self.exitWindowFrame.place(x=(width * 208) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                                   width=(width * 174) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        # I am then creating a button which is used to exit the game
        self.exitWindowButton = Button(self.exitWindowFrame, text="Exit Quiz", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                                       font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                       padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                       relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                                       command=self.quit)
        # It is then placed within the exitWindowFrame
        self.exitWindowButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                    width=(width * 166) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        # I am shuffling the list of questions so that the order is different each time the game is played
        random.shuffle(self.questions)
        # This will loop through the questions list and will also provide the index of that item
        for num, question in enumerate(self.questions):
            # If  endQuiz attribute is False
            if not self.endQuiz:
                # This will display the question and return a score out of 10
                qScore = question.create_questions(self.quizMaster, (num + 1))
                # The score the user receives for the question answered above is added to their total score
                self.totalScore += qScore
                # It will then add the score for this question and display it in the score label
                self.userScoreVar.set("Score: {}".format(self.totalScore))
                self.quizMaster.update_idletasks()
                time.sleep(DELAY * 3)
            else:
                pass
        if self.totalScore > int(userInstance.saveData[categoryInstance][1]):
            userInstance.update_score(self.totalScore, categoryInstance)
            time.sleep(DELAY * 6)
            self.quizMaster.quit()
            # Writing the quiz data
            writeTextFile("profiles.txt", "Profile", generate_new_profile_data())
            create_main_menu_window(quizMaster, username)
        else:
            userInstance.update_score(int(userInstance.saveData[categoryInstance][1]), categoryInstance)
            time.sleep(DELAY * 6)
            self.quizMaster.quit()
            # Writing the quiz data
            writeTextFile("profiles.txt", "Profile", generate_new_profile_data())
            create_main_menu_window(quizMaster, username)
        # This is the mainloop line and is needed for the window to exist
        self.quizMaster.mainloop()
        return

    def go_back(self):
        """This method is used to restart the quiz which is needed for the combobox which will change the category"""
        # Writing the quiz data first as it is important to save the profile data
        writeTextFile("profiles.txt", "Profile", generate_new_profile_data())
        # This sets the endQuiz function to True so when returned the code know that the current quiz is over
        self.endQuiz = True
        # This quits out of the current window so that a new category can be loaded
        self.quizMaster.quit()
        # It starts a new quiz by getting the value within the combobox
        # using the combobox value it indexes it and then creates the new categories quiz
        create_main_menu_window(self.quizMaster, self.username)

    def quit(self):
        """This method is used to exit the Tkinter window and will also end the program"""
        # There is a short delay
        time.sleep(DELAY * 2)
        # This sets the endQuiz function to True so when returned the code know that the current quiz is over
        self.endQuiz = True
        # Then the quiz window is destroyed and therefore cannot be used anymore
        self.quizMaster.destroy()
        # We then end the program
        exit()

    def set_high_score_data(self):
        """This method is used to set the users data in the high score panel"""
        mainList = []
        for profile in Profiles:
            if int(profile.saveData[Category.categoryNames.index(self.categoryName)][1]) != 0:
                mainList.append([profile.username,
                                 int(profile.saveData[Category.categoryNames.index(self.categoryName)][1])])
        if len(mainList) > 0:
            mainList.sort(key=operator.itemgetter(1))
        if len(mainList) < 10:
            for add in range(10 - len(mainList)):
                mainList.append(["---", "000"])
        userNames = ""
        userScores = ""
        for scoreData in mainList[0:10]:
            userNames += "{}\n".format(str(scoreData[0]))
            userScores += "{}\n".format(str(scoreData[1]))
        self.userNamesLabelVar.set(userNames[0:-1])
        self.userScoresLabelVar.set(userScores[0:-1])

    # This decorator is used to flag that this is a class method
    # It will take the cls parameter instead of self
    @classmethod
    def from_list(cls, categoryList):
        """This method is used to format the data given as a list so that it can be called as an instance
        :param categoryList: This is the list of each questions data from the text file
        :return: This returns an instance of the class for each category
        """
        # This will take the name of the category from the list
        category = categoryList[0]
        # This will take the entire list and save it as a new variable
        questions = categoryList
        # This will remove the category name from the list leaving the questions
        questions.pop(0)
        # This will return a string in the format Category(Category Name, Question List)
        return cls(category, questions)

    def __repr__(self):
        """This method is used for developers when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Category('{}','{}')".format(self.categoryName, self.questionList)

    def __str__(self):
        """This method is used for users when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Category Name: {}\nQuestions: {}".format(self.categoryName, self.questionList)


# Creating the Questions Class
class Questions:
    """This class is used to store each individual question"""

    def __init__(self, question, correctAnswer, incorrectAnswers):
        """This function is run when an instance of the Category class is created"""
        # Defining the question as an attribute of the class
        self.question = question
        # Defining the correct answer as an attribute of the class
        self.correctAnswer = correctAnswer
        # Defining a list of incorrect answers as an attribute of the class
        self.incorrectAnswers = incorrectAnswers

    def create_questions(self, quizMaster, qNumber):
        """This method will create the questions in the GUI window
        :param quizMaster: This is the Tk() window
        :param qNumber: Question Number
        :return: This will returns the score the user got for that question
        """
        # Here the quizMaster is being defined locally
        self.quizMaster = quizMaster
        # This is used to check if they have gotten the answer correct or ran out
        # ... of tries and is used to go the next question/return.
        self.answerConfirmed = False
        # This creates a variable representing the number of tries they have used
        self.tries = 0
        # Creating a frame where the questions and answers  will be displayed and the background color is set
        self.questionFrame = Frame(self.quizMaster, bg=TEXT_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.questionFrame.place(x=(width * 50) / ORIGINAL_WIDTH, y=(height * 250) / ORIGINAL_HEIGHT,
                                 width=(width * 850) / ORIGINAL_WIDTH, height=(height * 640) / ORIGINAL_HEIGHT)
        # Another frame is created to display only the question and the background color is set
        self.questionSubFrame = Frame(self.questionFrame, bg=BORDER_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.questionSubFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 18) / ORIGINAL_HEIGHT,
                                    width=(width * 814) / ORIGINAL_WIDTH, height=(height * 144) / ORIGINAL_HEIGHT)
        # Creating a string variable to store the question data
        self.questionLabelVar = StringVar()
        # I then set the StringVar as the question along with the question number before it
        self.questionLabelVar.set("Q{}. {}".format(qNumber, self.question))
        # Creating a label with the Question Var and with the correct formatting
        self.questionLabel = Label(self.questionSubFrame, textvariable=self.questionLabelVar, bg=BACKGROUND_COLOR1,
                                   fg=TEXT_COLOR, font=("Arial", int((width * 20) / ORIGINAL_WIDTH), "bold"),
                                   padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT, anchor="nw",
                                   wraplength=(width * 780) / ORIGINAL_WIDTH, justify='left')
        # The Label is then placed in the correct position with the correct dimensions
        self.questionLabel.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                 width=(width * 806) / ORIGINAL_WIDTH, height=(height * 136) / ORIGINAL_HEIGHT)
        # Creating a Frame which will be used to display the answers
        self.answersSubFrame = Frame(self.questionFrame, bg=BORDER_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.answersSubFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 178) / ORIGINAL_HEIGHT,
                                   width=(width * 814) / ORIGINAL_WIDTH, height=(height * 364) / ORIGINAL_HEIGHT)
        # Creating a Frame which will be used to display any outputs
        self.outputFrame = Frame(self.questionFrame, bg=BORDER_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.outputFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                               height=(height * 64) / ORIGINAL_HEIGHT, width=(width * 574) / ORIGINAL_WIDTH)
        # This creates a string variable for the information output
        self.outputLabelVar = StringVar()
        # The string var is then set to the default string telling the user to pick an answer
        # This will change accordingly while the user interacts with the question
        self.outputLabelVar.set("Please select an answer.")
        # A label using the String Var for the output is then created
        self.outputLabel = Label(self.outputFrame, textvariable=self.outputLabelVar, bg=BACKGROUND_COLOR1,
                                 fg=TEXT_COLOR, font=("Arial", int((width * 14) / ORIGINAL_WIDTH), "bold"),
                                 padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT, anchor="w",
                                 justify='left')
        # This Label is then placed in the correct position with the correct dimensions
        self.outputLabel.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                               width=(width * 566) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        # This will create a list of randomized answers using a the randomizedAnswers method
        randomizedAnswers = self.randomize_answers()
        # I create a variable to check if which button has been selected and is set to None by default
        self.SelectedButton = None
        """In the next 16 lines all 4 possible answers are displayed as buttons and
        these can be pressed to change the selected answer then must be confirmed
        Each has its own frame, StringVar and Label and are all placed in border
        and each button has its own command and the background colour will update
        when selected to show the user the selected answer"""
        self.Answer1Var = StringVar()
        self.Answer1Var.set(randomizedAnswers[0])
        self.Answer1Button = Button(self.answersSubFrame, textvariable=self.Answer1Var, bg=BACKGROUND_COLOR2,
                                    fg=TEXT_COLOR, font=("Arial", int((width * 18) / ORIGINAL_WIDTH)),
                                    padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                    anchor="w", relief="flat", activebackground=BACKGROUND_COLOR1,
                                    activeforeground=TEXT_COLOR, command=self.answer_1_select)
        self.Answer1Button.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                 width=(width * 806) / ORIGINAL_WIDTH, height=(height * 86) / ORIGINAL_HEIGHT)
        self.Answer2Var = StringVar()
        self.Answer2Var.set(randomizedAnswers[1])
        self.Answer2Button = Button(self.answersSubFrame, textvariable=self.Answer2Var, bg=BACKGROUND_COLOR2,
                                    fg=TEXT_COLOR, font=("Arial", int((width * 18) / ORIGINAL_WIDTH)),
                                    padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                    anchor="w", relief="flat", activebackground=BACKGROUND_COLOR1,
                                    activeforeground=TEXT_COLOR, command=self.answer_2_select)
        self.Answer2Button.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 94) / ORIGINAL_HEIGHT,
                                 width=(width * 806) / ORIGINAL_WIDTH, height=(height * 86) / ORIGINAL_HEIGHT)
        self.Answer3Var = StringVar()
        self.Answer3Var.set(randomizedAnswers[2])
        self.Answer3Button = Button(self.answersSubFrame, textvariable=self.Answer3Var, bg=BACKGROUND_COLOR2,
                                    fg=TEXT_COLOR, font=("Arial", int((width * 18) / ORIGINAL_WIDTH)),
                                    padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                    anchor="w", relief="flat", activebackground=BACKGROUND_COLOR1,
                                    activeforeground=TEXT_COLOR, command=self.answer_3_select)
        self.Answer3Button.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 184) / ORIGINAL_HEIGHT,
                                 width=(width * 806) / ORIGINAL_WIDTH, height=(height * 86) / ORIGINAL_HEIGHT)
        self.Answer4Var = StringVar()
        self.Answer4Var.set(randomizedAnswers[3])
        self.Answer4Button = Button(self.answersSubFrame, textvariable=self.Answer4Var, bg=BACKGROUND_COLOR2,
                                    fg=TEXT_COLOR, font=("Arial", int((width * 18) / ORIGINAL_WIDTH)),
                                    padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                    anchor="w", relief="flat", activebackground=BACKGROUND_COLOR1,
                                    activeforeground=TEXT_COLOR, command=self.answer_4_select)
        self.Answer4Button.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 274) / ORIGINAL_HEIGHT,
                                 width=(width * 806) / ORIGINAL_WIDTH, height=(height * 86) / ORIGINAL_HEIGHT)
        # Here a frame is being created for the confirmation button
        # This frames only purpose is to act as the border for the button
        self.confirmFrame = Frame(self.questionFrame, bg=BORDER_COLOR)
        # Placing the frame in the correct position
        self.confirmFrame.place(x=(width * 618) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                                width=(width * 214) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        # Creating a confirmation button within the frame
        # This button will be confirm the selection and an output will be shown
        self.confirmButton = Button(self.confirmFrame, text="Confirm Answer", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                                    font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                    padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                    relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                                    command=self.check_answer)
        # Placing the button so that the border is correct
        self.confirmButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                 width=(width * 206) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        # Mainloop is used again so that the window will show
        self.quizMaster.mainloop()
        # It will then return the score the user gets either 0, 3, 7 or 10
        return self.score

    def answer_1_select(self):
        """This method will be run if the first button is pressed"""
        # if no button is selected...
        if self.SelectedButton is None:
            # it will change the colour of the background of the first button
            self.Answer1Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the first button then return to the previous method
            self.SelectedButton = self.Answer1Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the first button will be set to the 'selected' colour and the others will be set to the 'unselected'
            # colour
            self.Answer4Button.config(bg=BACKGROUND_COLOR2)
            self.Answer3Button.config(bg=BACKGROUND_COLOR2)
            self.Answer2Button.config(bg=BACKGROUND_COLOR2)
            self.Answer1Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the first button then return to the previous method
            self.SelectedButton = self.Answer1Var
            return

    def answer_2_select(self):
        """This method will be run if the second button is pressed"""
        # if no button is selected...
        if self.SelectedButton is None:
            # it will change the colour of the background of the second button
            self.Answer2Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the second button then return to the previous method
            self.SelectedButton = self.Answer2Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the second button will be set to the 'selected' colour and the others will be set to the 'unselected'
            # colour
            self.Answer1Button.config(bg=BACKGROUND_COLOR2)
            self.Answer4Button.config(bg=BACKGROUND_COLOR2)
            self.Answer3Button.config(bg=BACKGROUND_COLOR2)
            self.Answer2Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the second button then return to the previous method
            self.SelectedButton = self.Answer2Var
            return

    def answer_3_select(self):
        """This method will be run if the third button is pressed"""
        # if no button is selected...
        if self.SelectedButton is None:
            # it will change the colour of the background of the third button
            self.Answer3Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the third button then return to the previous method
            self.SelectedButton = self.Answer3Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the third button will be set to the 'selected' colour and the others will be set to the 'unselected'
            # colour
            self.Answer2Button.config(bg=BACKGROUND_COLOR2)
            self.Answer1Button.config(bg=BACKGROUND_COLOR2)
            self.Answer4Button.config(bg=BACKGROUND_COLOR2)
            self.Answer3Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the third button then return to the previous method
            self.SelectedButton = self.Answer3Var
            return

    def answer_4_select(self):
        """This method will be run if the fourth button is pressed"""
        # if no button is selected...
        if self.SelectedButton is None:
            # it will change the colour of the background of the fourth button
            self.Answer4Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the fourth button then return to the previous method
            self.SelectedButton = self.Answer4Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the fourth button will be set to the 'selected' colour and the others will be set to the 'unselected'
            # colour
            self.Answer3Button.config(bg=BACKGROUND_COLOR2)
            self.Answer2Button.config(bg=BACKGROUND_COLOR2)
            self.Answer1Button.config(bg=BACKGROUND_COLOR2)
            self.Answer4Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the fourth button then return to the previous method
            self.SelectedButton = self.Answer4Var
            return

    def check_answer(self):
        """This method will check the answer the user has selected and will run when the confirm answer button is
        pressed
        :return: This returns a score out of 10 depending on how many tries the user has had"""
        # Here I am setting different outputs that could occur.
        # These are constant and do not change and are shown in the output box at the bottom of the window.
        unselectedAnswer = "You have not selected an answer."
        answerCorrect = ["Awesome you got that correct!", "Great Work, you got that correct!",
                         "Correct Answer, Amazing Work!", "Correct!", "Correct, that is INSANE!"]
        answerIncorrect = "You got that incorrect."
        # If the user has not selected a button there will be a short pause
        # and the output string var will then be set to show the user that they must select a button
        if self.SelectedButton is None:
            time.sleep(DELAY)
            self.outputLabelVar.set(unselectedAnswer)
            # It will then return to the mainloop to check for another confirmation
            return
        # otherwise if the text in the selected button is the same as the correct answer
        elif (self.SelectedButton.get()) == self.correctAnswer:
            # It then sets the answerConfirmed as True so that the code will advance to the next question
            self.answerConfirmed = True
            # if they have used 0 tries, first try answer they get full points
            if self.tries == 0:
                self.score = FULL_POINTS
            # if they have used 1 tries, second try answer they get full points
            elif self.tries == 1:
                self.score = MOST_POINTS
            # if they have used 2 tries, third try answer they get full points
            elif self.tries == 2:
                self.score = SOME_POINTS
            # if they get the answer on their last try they get no points
            else:
                self.score = NO_POINTS
            # This randomly selects an item for the output from the answerCorrect list
            self.outputLabelVar.set(random.choice(answerCorrect))
            # This is used to update all the idle tasks and is an alternative to mainloop
            self.quizMaster.update_idletasks()
            # This is disabling the button so that it cannot be spam clicked which crashes the quiz
            self.confirmButton.config(state="disabled")
            # it then quits the quiz master so that a new one can be made and returns to the mainloop
            self.quizMaster.quit()
            return
        # If they have used up all their tries
        else:
            if self.tries > 2:
                # Then the output label will tell the user they are out of tries
                self.outputLabelVar.set("You got that incorrect and are out of tries.")
                # This is used to update all the idle tasks and is an alternative to mainloop
                self.quizMaster.update_idletasks()
                # This is disabling the button so that it cannot be spam clicked which crashes the quiz
                self.confirmButton.config(state="disabled")
                # It then sets the answerConfirmed as True so that the code will advance to the next question
                self.answerConfirmed = True
                # it will then set their score to 0 points
                self.score = NO_POINTS
                # it then quits the quiz master so that a new one can be made and returns to the mainloop
                self.quizMaster.quit()
                return
            # else there will  be a short pause and it will set the output label to show how many tries they have
            # remaining
            else:
                # It shows the number of tries they have remaining
                self.outputLabelVar.set("{} Try Again - Tries Remaining: {}".format(answerIncorrect, (3 - self.tries)))
                # They have 1 try added to the number of tries they have used and returns to the mainloop
                self.tries += 1
                return

    def randomize_answers(self):
        """This method is used to return a list of randomized answers for this instance
        :return: This will return a randomized list of the correct answer mixed in with the incorrect answers
        """
        # First a list is created using the incorrect answers attribute
        answers = self.incorrectAnswers
        # Here an if statement is being used to check wether the correct answer is in the list
        if self.correctAnswer not in answers:
            # If so the correct answer is appended to this list
            answers.append(self.correctAnswer)
        # Lastly this list is shuffled and returned
        random.shuffle(answers)
        return answers

    # This decorator is used to flag that this is a class method
    # It will take the cls parameter instead of self
    @classmethod
    def from_list(cls, questionList):
        """This method is used to format the data given as a list so that it can be called as an instance
        :param questionList: This is the list of each questions data from the text file
        :return:This returns an instance of the class for each question
        """
        # This takes the first item in the list which is the question
        question = questionList[0]
        # Here the correct answer is taken which is the first item in the second item of the main list
        correctAnswer = questionList[1][0]
        # Taking a list of incorrect answers are taken which is the second tem in the second item of the main list
        incorrectAnswers = questionList[1][1]
        # This will return a string in the format Category(Question, Correct Answer, Incorrect Answers)
        return cls(question, correctAnswer, incorrectAnswers)

    def __repr__(self):
        """This method is used for developers when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Questions('{}','{}',{})".format(self.question, self.correctAnswer, self.incorrectAnswers)

    def __str__(self):
        """This method is used for users when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Question: {}\nCorrect Answer: {}\nIncorrect Answers: {}".format(self.question, self.correctAnswer,
                                                                                self.incorrectAnswers)


class Profile:
    """This class is used to store all the Profile Data"""
    # Setting global class variables
    profileNames = []

    def __init__(self, userID, username, saveData):
        """This function is run each time an instance of the class is created
        :param userID: This is the users ID (Used to sort the profiles in combobox)c
        :param username: Users username and is used by them as their profile
        :param saveData: List used to store each Category with the users highest score, total score and number attempts
        """
        # Here each of the parameters that are required are saved as attributes
        self.userID = userID
        self.username = username
        self.saveData = saveData
        Profile.profileNames.append(self.username)

    def get_category_scores_string(self):
        """This will retrieve a string with all the users scores"""
        categoryScoresString = ""
        for data in self.saveData:
            if int(data[1]) == 0:
                categoryScoresString += "000\n"
            else:
                categoryScoresString += "{}\n".format(data[1])
        if len(self.saveData) < 10:
            categoryScoresString += ("000\n" * (9 - len(self.saveData)) + "000")
        return categoryScoresString

    def update_score(self, newScore, categoryInst):
        """This function is used to update the score of the user after they complete the quiz :param newScore: This
        is the users new score. If they did not surpass the old score the old score should be returned and therefore
        it will remain the same. :param categoryInst: This is the index value of the category for which the user got
        this score
        """
        self.saveData[categoryInst][1] = newScore
        self.saveData[categoryInst][2] = int(self.saveData[categoryInst][2]) + newScore
        self.saveData[categoryInst][3] = int(self.saveData[categoryInst][3]) + 1
        return

    # This decorator is used to flag that this is a class method
    # It will take the cls parameter instead of self
    @classmethod
    def from_list(cls, profileList):
        """This method is used to format the data given as a list so that it can be called as an instance
        :param profileList: This is the list of each users profile data from the text file
        :return: This returns an instance of the class for each user
        """
        # This takes the first item in the list which is the profile ID
        ID = profileList[0]
        # This takes the first item in the list which is the username
        username = profileList[1]
        # This will take the 4th and last item in the list which is a list of all the users scores
        saveData = profileList[2]
        # This will return a string in the format Profiles(userID, username, savedQuizzes, saveData)
        return cls(ID, username, saveData)

    def __repr__(self):
        """This method is used for developers when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Profile('{}','{}','{}')".format(self.userID, self.username, self.saveData)

    def __str__(self):
        """This method is used for users when the instance is printed it is formatted"""
        # This returns the formatted string
        return "User ID: {}\nUsername: {}\nScores: {}".format(self.userID, self.username, self.saveData)


def create_main_menu_window(masterWindow, loggedUser):
    """This function is used to create the main menu window where the user
    :param masterWindow: This is used to transfer the Tk() window.
    """

    def add_profile():
        """This function is used to add a new profile. A form is created and validation occurs so they can add a
        profile """

        def callback(event):
            """This function is used when the user clicks on the entry box"""
            userNameEntryBox.focus_set()
            userNameEntryBoxVar.set("  ")
            return

        def validate_username():
            """This function is used to make sure the username the user enters meets the requirements"""
            userName = userNameEntryBoxVar.get().strip()
            if userName == "":
                tkinter.messagebox.showerror("Error", "Please don't leave it blank.")
                userNameEntryBoxVar.set("  Enter a Username")
            elif len(userName) < 3 or len(userName) > 20:
                tkinter.messagebox.showerror("Error", "Please choose a Username which is between 3 and 20 characters "
                                                      "long.")
                userNameEntryBoxVar.set("  Enter a Username")
            elif userName in Profile.profileNames:
                tkinter.messagebox.showerror("Error", "Sorry, that username is already taken.")
                userNameEntryBoxVar.set("  Enter a Username")
            elif userName == "Enter a Username":
                tkinter.messagebox.showerror("Error", "Please enter a valid username")
            else:
                add_username()
                tkinter.messagebox.showinfo("Information", "Username Created")

        def add_username():
            """This function is used to add the username (once it is validated) to the Profiles"""
            saveData = []
            for category in Category.categoryNames:
                saveData.append([category, 0, 0, 0])
            Profiles.append(Profile.from_list([Profiles[-1].userID + 1, userNameEntryBoxVar.get().strip(), saveData]))
            profileBox['values'] = Profile.profileNames
            writeTextFile("profiles.txt", "Profile", generate_new_profile_data())
            profileCreateFrame.destroy()
            return

        def go_back():
            """This function is used to exit out of the add profile scene"""
            profileCreateFrame.destroy()

        userNameValid = False
        profileCreateFrame = Frame(userInteractFrame, bg=TEXT_COLOR)
        profileCreateFrame.place(x=(width * 0) / ORIGINAL_WIDTH, y=(height * 0) / ORIGINAL_HEIGHT,
                                 width=(width * 400) / ORIGINAL_WIDTH, height=(height * 640) / ORIGINAL_HEIGHT)
        userNameFrame = Frame(profileCreateFrame, bg=BORDER_COLOR)
        userNameFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 18) / ORIGINAL_HEIGHT,
                            width=(width * 364) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        userNameEntryBoxVar = StringVar()
        userNameEntryBoxVar.set("  Enter a Username")
        userNameEntryBox = Entry(userNameFrame, textvariable=userNameEntryBoxVar, bg=BACKGROUND_COLOR1,
                                 fg=TEXT_COLOR, font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                 justify='left')
        userNameEntryBox.bind("<Button-1>", callback)
        # This is then placed in the corect position so that the user is able to enter their username
        userNameEntryBox.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                               width=(width * 356) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        returnFrame = Frame(profileCreateFrame, bg=BORDER_COLOR)
        returnFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                          width=(width * 174) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        returnButton = Button(returnFrame, text="Go Back", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                              font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                              padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                              relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                              command=go_back)
        returnButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                           width=(width * 166) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
        userNameConfirmFrame = Frame(profileCreateFrame, bg=BORDER_COLOR)
        userNameConfirmFrame.place(x=(width * 208) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                                   width=(width * 174) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
        userNameConfirmButton = Button(userNameConfirmFrame, text="Confirm", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                                       font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                                       padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                                       relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                                       command=validate_username)
        userNameConfirmButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                                    width=(width * 166) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)

    def change_category_scores(*args):
        """This function is used to change the users scores for each category if the combobox value is changed"""
        if profileBox.get() == "Select Profile":
            categoriesScoresLabelVar.set(("000\n" * 9) + "000")
        else:
            profileIndex = Profile.profileNames.index(profileBox.get())
            categoriesScoresLabelVar.set(Profiles[profileIndex].get_category_scores_string())
        return

    def play_quiz():
        if profileVar.get() == "Select Profile" or chosenCategory.get() == "Select a Category":
            tkinter.messagebox.showerror("Error", "Please select a Category and your Profile")
        else:
            menuWindow.quit()
            Categories[Category.categoryNames.index(chosenCategory.get())].createQuizWindow(menuWindow,
                                                                                            profileVar.get())

    background = Image.open("images/background.png")
    # I am then resizing the image to the correct height and width and enabling ANTIALIASING
    background = background.resize((width, height), Image.ANTIALIAS)
    # Creating a PhotoImage variable using the resized background image
    backgroundImageVar = ImageTk.PhotoImage(background)
    # Creating a label with the background image
    menuWindow = ttk.Label(masterWindow, image=backgroundImageVar)
    # Placing the background image at 0,0
    menuWindow.place(x=0, y=0)
    # Creating a Frame for the title label which will be used as the border
    greetingFrame = Frame(menuWindow, bg=BORDER_COLOR)
    """Placing the frame at 50,50 with a width of 1300 and a height of 150
    From here everything which is placed must have its width and height along
    with the coordinate it is placed at. This is done by the original
    width/height by the new width/height and then by the window size"""
    greetingFrame.place(x=(width * 50) / ORIGINAL_WIDTH, y=(height * 50) / ORIGINAL_HEIGHT,
                        width=(width * 1300) / ORIGINAL_WIDTH, height=(height * 150) / ORIGINAL_HEIGHT)
    # Creating a String Variable for the greeting text
    greetingTextVar = StringVar()
    # This will set the string variable to the greeting name
    greetingTextVar.set("Welcome to the Multi-Choice Quiz")
    # A Label is created using the previously created StringVar and is also formatted
    greetingTextLabel = Label(greetingFrame, textvariable=greetingTextVar, bg=BACKGROUND_COLOR1,
                              fg=TEXT_COLOR, font=("Arial", int((width * 60) / ORIGINAL_WIDTH)),
                              padx=(width * 14) / ORIGINAL_WIDTH, anchor="center")
    # The Label is then placed in the recently created frame at 6,6
    # With a width and height slightly less to show the border so that the frame acts as a border
    greetingTextLabel.place(x=(width * 6) / ORIGINAL_WIDTH, y=(height * 6) / ORIGINAL_HEIGHT,
                            width=(width * 1288) / ORIGINAL_WIDTH, height=(height * 138) / ORIGINAL_HEIGHT)
    # Creating a frame where the information will be displayed for the user
    infoFrame = Frame(menuWindow, bg=TEXT_COLOR)
    # This frame is placed in the correct position with the correct dimensions
    infoFrame.place(x=(width * 50) / ORIGINAL_WIDTH, y=(height * 250) / ORIGINAL_HEIGHT,
                    width=(width * 850) / ORIGINAL_WIDTH, height=(height * 640) / ORIGINAL_HEIGHT)
    # Another frame is created to display the title of the frame
    infoSubFrame = Frame(infoFrame, bg=BORDER_COLOR)
    # This frame is placed in the correct position with the correct dimensions
    infoSubFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 18) / ORIGINAL_HEIGHT,
                       width=(width * 814) / ORIGINAL_WIDTH, height=(height * 74) / ORIGINAL_HEIGHT)
    # Creating a string variable to store the question data
    infoLabelVar = StringVar()
    # I then set the StringVar which is set to "Information" which will be displayed using a label
    infoLabelVar.set("Information")
    # Creating a label with the String Var and specifying its settings
    infoLabel = Label(infoSubFrame, textvariable=infoLabelVar, bg=BACKGROUND_COLOR1,
                      fg=TEXT_COLOR, font=("Arial", int((width * 28) / ORIGINAL_WIDTH), "bold"),
                      padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT
                      , justify='center', anchor="center")
    # The Label is then placed in the correct position with the correct dimensions
    infoLabel.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                    width=(width * 806) / ORIGINAL_WIDTH, height=(height * 66) / ORIGINAL_HEIGHT)
    # Creating a Frame which will be used to display the answers
    scriptFrame = Frame(infoFrame, bg=BORDER_COLOR)
    # This frame is placed in the correct position with the correct dimensions
    scriptFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 108) / ORIGINAL_HEIGHT,
                      width=(width * 814) / ORIGINAL_WIDTH, height=(height * 514) / ORIGINAL_HEIGHT)
    # Creating a string var and setting it as the constant text which will be displayed
    scriptLabelVar = StringVar()
    scriptLabelVar.set("1. If you are a returning user please select your profile from the menu on the right\n2. If "
                       "you are new you can create a new profile from the menu on the right by clicking the “+”\n3. "
                       "Select which Category you would like to be tested on.\n4. Then click “Play Quiz”. Which will "
                       "begin the quiz.\n5. Your highest scores will be saved for each quiz and can also be seen on "
                       "the right.\n\nGood Luck!")
    # Creating a label which will display the string var set previously
    scriptLabel = Label(scriptFrame, textvariable=scriptLabelVar, bg=BACKGROUND_COLOR2,
                        fg=TEXT_COLOR, font=("Arial", int((height * 25) / ORIGINAL_HEIGHT), "bold"),
                        padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT, anchor="nw",
                        justify='left', wraplength=(width * 790) / ORIGINAL_WIDTH)
    # Placing the label
    scriptLabel.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                      width=(width * 806) / ORIGINAL_WIDTH, height=(height * 506) / ORIGINAL_HEIGHT)
    # Here a frame is created to store everything the user interacts with
    userInteractFrame = Frame(menuWindow, bg=TEXT_COLOR)
    # This frame is then placed in the appropriate position with the correct height and width
    userInteractFrame.place(x=(width * 950) / ORIGINAL_WIDTH, y=(height * 250) / ORIGINAL_HEIGHT,
                            width=(width * 400) / ORIGINAL_WIDTH, height=(height * 640) / ORIGINAL_HEIGHT)
    # Here a frame for the profile is created
    profileFrame = Frame(userInteractFrame, bg=BORDER_COLOR)
    # It is then placed correctly so that it can act as a border
    profileFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 18) / ORIGINAL_HEIGHT,
                       width=(width * 284) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
    # A string var is created to store the profile
    profileVar = StringVar()
    # Here the default text for the combo box is being set
    profileVar.set(loggedUser)
    # I am using a previously created theme for the combobox
    ComboStyle.theme_use('combostyle')
    # Creating a combobox to select the profile
    profileBox = ttk.Combobox(profileFrame, textvariable=profileVar, state="readonly",
                              font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"))
    # On the next line I am defining the values which will appear in the combobox
    profileBox['values'] = Profile.profileNames
    # This is then placed in the corect position so that the user is able to enter their profile
    profileBox.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                     width=(width * 276) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
    # Creating a frame for the add profile button and placing it
    add_profileFrame = Frame(userInteractFrame, bg=BORDER_COLOR)
    add_profileFrame.place(x=(width * 318) / ORIGINAL_WIDTH, y=(height * 18) / ORIGINAL_HEIGHT,
                           width=(width * 64) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
    # Creating a button within the add_profileFrame used to add a profile
    add_profileButton = Button(add_profileFrame, text="+", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                               font=("Arial", int((width * 35) / ORIGINAL_WIDTH), "bold"),
                               padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                               relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                               command=add_profile)
    # Placing the button in the correct position
    add_profileButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                            width=(width * 56) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
    # A Frame is created for the category combobox and it is then placed in the correct postion
    categoryBoxFrame = Frame(userInteractFrame, bg=BORDER_COLOR)
    categoryBoxFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 98) / ORIGINAL_HEIGHT,
                           width=(width * 364) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
    # I am creating a string variable for the combo box
    chosenCategory = StringVar()
    # Setting the chosenCategory to the current categoryName
    chosenCategory.set("Select a Category")
    # I am using a previously created theme for the combobox
    ComboStyle.theme_use('combostyle')
    # Creating a combobox to select the category
    categoryBox = ttk.Combobox(categoryBoxFrame, textvariable=chosenCategory, state="readonly",
                               font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"))
    # On the next line I am defining the values which will appear in the combobox
    categoryBox['values'] = Category.categoryNames
    # Placing the combobox in the correct position
    categoryBox.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                      width=(width * 356) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
    # Here I am creating a frame which will be used for the users highscores border and placing it
    userScoresOuterFrame = Frame(userInteractFrame, bg=BORDER_COLOR)
    userScoresOuterFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 178) / ORIGINAL_HEIGHT,
                               width=(width * 364) / ORIGINAL_WIDTH, height=(height * 364) / ORIGINAL_HEIGHT)
    # Here I am creating a frame which will be used for the users highscores and placing it
    userScoresInnerFrame = Frame(userScoresOuterFrame, bg=BACKGROUND_COLOR2)
    userScoresInnerFrame.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                               width=(width * 356) / ORIGINAL_WIDTH, height=(height * 356) / ORIGINAL_HEIGHT)
    # Creating a label for the category title and placing it
    highScoreTitleLabel = Label(userScoresInnerFrame, text="Category", bg=BACKGROUND_COLOR2,
                                fg=BORDER_COLOR, font=("Arial", int((width * 18) / ORIGINAL_WIDTH), "bold",
                                                       "underline"),
                                padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                anchor="center")
    highScoreTitleLabel.place(x=(width * 8) / ORIGINAL_WIDTH, y=(height * 8) / ORIGINAL_HEIGHT,
                              width=(width * 205) / ORIGINAL_WIDTH, height=(height * 32) / ORIGINAL_HEIGHT)
    # Creating a label for the highscore title and placing it
    highscoreTitleLabel = Label(userScoresInnerFrame, text="Highscore", bg=BACKGROUND_COLOR2,
                                fg=BORDER_COLOR,
                                font=("Arial", int((width * 18) / ORIGINAL_WIDTH), "bold", "underline"),
                                padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                anchor="center")
    highscoreTitleLabel.place(x=(width * 233) / ORIGINAL_WIDTH, y=(height * 8) / ORIGINAL_HEIGHT,
                              width=(width * 115) / ORIGINAL_WIDTH, height=(height * 32) / ORIGINAL_HEIGHT)
    # Creating a frame to be used to divide the category names and the highscores and placing it
    dividerFrame = Frame(userScoresInnerFrame, bg=BORDER_COLOR)
    dividerFrame.place(x=(width * 223) / ORIGINAL_WIDTH, y=(height * 8) / ORIGINAL_HEIGHT,
                       width=(width * 4) / ORIGINAL_WIDTH, height=(height * 340) / ORIGINAL_HEIGHT)
    # Creating a string var for the categories and using a local function to collect the string to set it as
    categoriesLabelVar = StringVar()
    categoriesLabelVar.set(get_category_string())
    # Creating a label for the categories placing it
    categoriesLabel = Label(userScoresInnerFrame, textvariable=categoriesLabelVar, bg=BACKGROUND_COLOR2,
                            fg=TEXT_COLOR, font=("Arial", int((height * 18) / ORIGINAL_HEIGHT), "bold"),
                            padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                            anchor="center")
    categoriesLabel.place(x=(width * 8) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                          width=(width * 205) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
    # Creating a string variable which will be used to store each label
    categoriesScoresLabelVar = StringVar()
    if loggedUser == "Select Profile":
        # When there is no selected profile in the combobox it sets the default value for the scores to "000"
        categoriesScoresLabelVar.set(("000\n" * 9) + "000")
    else:
        change_category_scores(menuWindow)
    # When the value in the combo box is updated the scores are changed to what the user has scored for those quizzes
    profileBox.bind("<<ComboboxSelected>>", change_category_scores)
    # creating a label for the scores of each category for the selected user to be displayed.
    categoriesScoresLabel = Label(userScoresInnerFrame, textvariable=categoriesScoresLabelVar, bg=BACKGROUND_COLOR2,
                                  fg=TEXT_COLOR, font=("Arial", int((height * 18) / ORIGINAL_HEIGHT), "bold"),
                                  padx=(width * 5) / ORIGINAL_WIDTH, pady=(height * 5) / ORIGINAL_HEIGHT,
                                  anchor="center")
    categoriesScoresLabel.place(x=(width * 233) / ORIGINAL_WIDTH, y=(height * 48) / ORIGINAL_HEIGHT,
                                width=(width * 115) / ORIGINAL_WIDTH, height=(height * 290) / ORIGINAL_HEIGHT)
    # A Frame is created for the border of the exit button which will exit the game
    exitWindowFrame = Frame(userInteractFrame, bg=BORDER_COLOR)
    # This Frame is then placed in the bottom right of the info frame
    exitWindowFrame.place(x=(width * 18) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                          width=(width * 174) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
    # I am then creating a button which is used to exit the game
    exitWindowButton = Button(exitWindowFrame, text="Exit Quiz", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                              font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                              padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                              relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                              command=quit)
    # It is then placed within the exitWindowFrame
    exitWindowButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                           width=(width * 166) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
    # A Frame is created for the border of the button which is used to start the quiz
    playQuizFrame = Frame(userInteractFrame, bg=BORDER_COLOR)
    # This Frame is then placed in the bottom right of the info frame
    playQuizFrame.place(x=(width * 208) / ORIGINAL_WIDTH, y=(height * 558) / ORIGINAL_HEIGHT,
                        width=(width * 174) / ORIGINAL_WIDTH, height=(height * 64) / ORIGINAL_HEIGHT)
    # I am then creating a button which is used to start the quiz using the play_quiz function when pressed
    playQuizButton = Button(playQuizFrame, text="Play Quiz", bg=BACKGROUND_COLOR1, fg=TEXT_COLOR,
                            font=("Arial", int((width * 17) / ORIGINAL_WIDTH), "bold"),
                            padx=(width * 10) / ORIGINAL_WIDTH, pady=(height * 10) / ORIGINAL_HEIGHT,
                            relief="flat", activebackground=BACKGROUND_COLOR2, activeforeground=TEXT_COLOR,
                            command=play_quiz)
    # It is then placed within the playQuizFrame
    playQuizButton.place(x=(width * 4) / ORIGINAL_WIDTH, y=(height * 4) / ORIGINAL_HEIGHT,
                         width=(width * 166) / ORIGINAL_WIDTH, height=(height * 56) / ORIGINAL_HEIGHT)
    masterWindow.mainloop()


def get_category_string():
    """This function is used to create a string with each category in it on seperate lines"""
    # Creating a blank string
    categoryString = ""
    # Looping through every instance of the categories
    for ctg in Categories:
        # Adding every category name to the string on a different line
        categoryString += (ctg.categoryName + "\n")
    # If the number of categories is less than 10 we add "---" on separate lines making the string 10 lines long
    if Category.num_of_categories < 10:
        categoryString += ("---\n" * (9 - Category.num_of_categories)) + "---"
    return categoryString


def generate_new_profile_data():
    """This function will generate a list correctly formatted so it can be written to the profiles file"""
    mainList = []
    for profile in Profiles:
        userID = profile.userID
        userName = profile.username
        userData = profile.saveData
        mainList.append([userID, userName, userData])
    return mainList


# The next two lines are used to collect lists of both the categories and profiles
# ... from their own text files. This is done using the textFileConverter module
CategoryList = readTextFile("categories.txt", "Category")
ProfileList = readTextFile("profiles.txt", "Profile")
# Here an empty list is created which will be used to store each instance of the categories
Categories = []
# Here an empty list is created which will be used to store each instance of the profiles
Profiles = []

# This will loop through every category in the main category list
for ctg in CategoryList:
    # This will append an instance of each category using the class method in the Category class
    Categories.append(Category.from_list(ctg))
# This will loop through every profile in the main profile list
for prf in ProfileList:
    # This will append an instance of each profile using the class method in the Profile class
    Profiles.append(Profile.from_list(prf))

# Creating the Quiz
quizWindow = Tk()
# On this line I am collecting information about the users screen resolution I can
# ... then use this data to change the sizing of my window and all the widgets
width, height = quizWindow.winfo_screenwidth(), quizWindow.winfo_screenheight()
# I am setting the resolution of the window to the same size as their screen
quizWindow.geometry("{}x{}+0+0".format(width, height))
# Making the window a fullscreen window
quizWindow.attributes('-fullscreen', True)
# This will set the title of the quiz window as the "Multi-Choice Quiz"
quizWindow.title("Multi-Choice Quiz")
# I am creating a ttk style which will be used as for a combobox
ComboStyle = ttk.Style()
# Creating a theme for this style
ComboStyle.theme_create("combostyle", parent='alt', settings={'TCombobox': {
    'configure': {'selectbackground': BACKGROUND_COLOR1, 'fieldbackground': BACKGROUND_COLOR1,
                  'background': BACKGROUND_COLOR1, 'selectforeground': TEXT_COLOR, 'foreground': TEXT_COLOR,
                  'padding': ((width * 10) / ORIGINAL_WIDTH)}}})
create_main_menu_window(quizWindow, "Select Profile")
quizWindow.mainloop()
