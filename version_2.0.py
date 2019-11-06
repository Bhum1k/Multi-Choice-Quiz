# Programmer: Bhumik Patel
# Program: Multi-Choice Quiz
# Version: 2.0

# Purpose:
# This is a Multi-Choice Quiz which will reflect to society and is made for all
# age groups who would like to challenge themselves. It will have multiple
# Categories to choose from so that it can relate to an even wider range of people.

# This is the first version of the GUI quiz. In this version I will add the very
# ... first GUI based quiz. The user will be able to access a set category of the
# ... quiz and will receive a score for that category at the end.
# Using Tkinter to create a GUI
# I have removed the method in the Questions class which was used to ask each questions


# Importing Modules
from tkinter import *
from tkinter import ttk
import random
import time

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


# Creating the Category Class
class Category:
    """The Class is used to store all the different Categories for the quiz"""
    # Setting global class variables
    num_of_questions = 0
    num_of_categories = 0

    def __init__(self,categoryName,questionList):
        """This function is run when an instance of the Category class is created"""
        # Defining the category name parameter as an attribute of the class
        self.categoryName = categoryName
        # Defining the parameter providing list of questions as an attribute of the class
        self.questionList = questionList
        # Creating an empty list to store the instances of the questions
        self.questions = []
        # This will loop through every item in the questionList attribute
        for question in self.questionList:
            # This will append and instance of the question to the questions attribute
            (self.questions).append(Questions.from_list(question))
        # This will add 1 to specify the number of categories stored in the class
        Category.num_of_categories += 1
        # This will add the number of items in the questionList to specify the number of question in the class
        Category.num_of_questions += int(len(self.questionList))


    def createQuizWindow(self,quizMaster):
        """In this method a GUI window will be created for the Quiz"""
        # This will set the title of the quiz window as the "Category Name" Quiz
        quizMaster.title("{} Quiz".format(self.categoryName))
        # Setting the resolution of this window to 1400x940 pixels
        quizMaster.geometry("1400x940")
        # Disabling the ability to resize the quizWindow
        quizMaster.resizable(0,0)
        # Creating a PhotoImage variable and setting the file
        backgroundImageVar = PhotoImage(file="images/background.png")
        # Creating a label with the background image
        backgroundImage = ttk.Label(quizMaster,image=backgroundImageVar)
        # Placing the background image at 0,0
        backgroundImage.place(x=0,y=0)
        # Creating a Frame for the category title and will be used as the border
        categoryFrame = Frame(quizMaster,bg=BORDER_COLOR)
        # Placing the frame at 50,50 with a width of 1300 and a height of 150
        categoryFrame.place(x=50,y=50,width=1300,height=150)
        # Creating a String Variable for the category text
        categoryTextVar = StringVar()
        # This will set the string variable to the category name
        categoryTextVar.set(self.categoryName)
        # A Label is created using the previously created StringVar and is also formatted
        categoryTextLabel = Label(categoryFrame,textvariable=categoryTextVar,bg=BACKGROUND_COLOR1,fg=TEXT_COLOR,font=("Arial",80),padx=14,anchor="n")
        # The Label is then placed in the recently created frame at 6,6
        # With a width and height slightly less to show the border so that the frame acts as a border
        categoryTextLabel.place(x=6,y=6,width=1288,height=138)
        # Here a frame is created to display information
        # This will not be used at this stage and is for future use
        infoFrame = Frame(quizMaster,bg=TEXT_COLOR)
        # This frame is then placed in the appropriate position with the correct height and width
        infoFrame.place(x=950,y=250,width=400,height=640)
        # This is setting the starting score of the user
        totalScore = 0
        # This will loop through the questions list and will also provide the index of that item
        for num,question in enumerate(self.questions):
            # This will display the question and return a score out of 10
            qScore = question.createQuestions(quizMaster,(num + 1))
            # The score the user receives for the question answered above is added to their total score
            totalScore += qScore
        # It will then print their total score
        print("You scored {} points".format(totalScore))
        # This is the mainloop line and is needed for the window to exist
        quizMaster.mainloop()


    # This decorator is used to flag that this is a class method
    # It will take the cls parameter instead of self
    @classmethod
    def from_list(cls,categoryList):
        """This method is used to format the data given as a list so that it can be called as an instance"""
        # This will take the name of the category from the list
        category = categoryList[0]
        # This will take the entire list and save it as a new variable
        questions = categoryList
        # This will remove the category name from the list leaving the questions
        questions.pop(0)
        # This will return a string in the format Category(Category Name, Question List)
        return cls(category,questions)


    def __repr__(self):
        """This method is used for developers when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Category('{}','{}')".format(self.categoryName,self.questionList)


    def __str__(self):
        """This method is used for users when the instance is printed it is formatted"""
    # This returns the formatted string
        return "Category Name: {}\nQuestions: {}".format(self.categoryName,self.questionList)


# Creating the Questions Class
class Questions:
    """This class is used to store each individual question"""
    def __init__(self,question,correctAnswer,incorrectAnswers):
        """This function is run when an instance of the Category class is created"""
        # Defining the question as an attribute of the class
        self.question = question
        # Defining the correct answer as an attribute of the class
        self.correctAnswer = correctAnswer
        # Defining a list of incorrect answers as an attribute of the class
        self.incorrectAnswers = incorrectAnswers


    def createQuestions(self,quizMaster,qNumber):
        """This method will create the questions in the GUI window"""
        # Here the quizMaster is being defined locally
        self.quizMaster = quizMaster
        # This is used to check if they have gotten the answer correct or ran out
        # ... of tries and is used to go the next question/return.
        self.answerConfirmed = False
        # This creates a variable representing the number of tries they have used
        self.tries = 0
        # Creating a frame where the questions and answers  will be displayed and the background color is set
        self.questionFrame = Frame(self.quizMaster,bg=TEXT_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.questionFrame.place(x=50,y=250,width=850,height=640)
        # Another frame is created to display only the question and the background color is set
        self.questionSubFrame = Frame(self.questionFrame,bg=BORDER_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.questionSubFrame.place(x=18,y=18,width=814,height=144)
        # Creating a string variable to store the question data
        questionLabelVar = StringVar()
        # I then set the StringVar as the question along with the question number before it
        questionLabelVar.set("Q{}. {}".format(qNumber,self.question))
        # Creating a label with the Question Var and with the correct formatting
        questionLabel = Label(self.questionSubFrame,textvariable=questionLabelVar,bg=BACKGROUND_COLOR1,fg=TEXT_COLOR,font=("Arial",25,"bold"),padx=10,pady=5,anchor="nw",wraplength = 780)
        # The Label is then placed in the correct position with the correct dimensions
        questionLabel.place(x=4,y=4,width=806,height=136)
        # Creating a Frame which will be used to display the answers
        self.answersSubFrame = Frame(self.questionFrame,bg=BORDER_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.answersSubFrame.place(x=18,y=178,width=814,height=364)
        # Creating a Frame which will be used to display any outputs
        self.outputFrame = Frame(self.questionFrame,bg=BORDER_COLOR)
        # This frame is placed in the correct position with the correct dimensions
        self.outputFrame.place(x=18,y=558,height=64,width=574)
        # This creates a string variable for the information output
        self.outputLabelVar = StringVar()
        # The string var is then set to the default string telling the user to pick an answer
        # This will change accordingly while the user interacts with the question
        self.outputLabelVar.set("Please select an answer.")
        # A label using the String Var for the output is then created
        self.outputLabel = Label(self.outputFrame,textvariable=self.outputLabelVar,bg=BACKGROUND_COLOR1,fg=TEXT_COLOR,font=("Arial",14,"bold"),padx=10,pady=10,anchor="w")
        # This Label is then placed in the correct position with the correct dimensions
        self.outputLabel.place(x=4,y=4,width=566,height=56)
        # This will create a list of randomized answers using a the randomizedAnswers method
        randomizedAnswers = self.randomizeAnswers()
        # I create a variable to check if which button has been selected and is set to None by default
        self.SelectedButton = None
        """In the next 16 lines all 4 possible answers are displayed as buttons and
        these can be pressed to change the selected answer then must be confirmed
        Each has its own frame, StringVar and Label and are all placed in border
        and each button has its own command and the background colour will update
        when selected to show the user the selected answer"""
        self.Answer1Var = StringVar()
        self.Answer1Var.set(randomizedAnswers[0])
        self.Answer1Button = Button(self.answersSubFrame,textvariable=self.Answer1Var,bg=BACKGROUND_COLOR2,fg=TEXT_COLOR,font=("Arial",18,"bold"),padx=10,pady=10,anchor="w",relief="flat",activebackground=BACKGROUND_COLOR1,activeforeground=TEXT_COLOR,command=self.Answer1Select)
        self.Answer1Button.place(x=4,y=4,width=806,height=86)
        self.Answer2Var = StringVar()
        self.Answer2Var.set(randomizedAnswers[1])
        self.Answer2Button = Button(self.answersSubFrame,textvariable=self.Answer2Var,bg=BACKGROUND_COLOR2,fg=TEXT_COLOR,font=("Arial",18,"bold"),padx=10,pady=10,anchor="w",relief="flat",activebackground=BACKGROUND_COLOR1,activeforeground=TEXT_COLOR,command=self.Answer2Select)
        self.Answer2Button.place(x=4,y=94,width=806,height=86)
        self.Answer3Var = StringVar()
        self.Answer3Var.set(randomizedAnswers[2])
        self.Answer3Button = Button(self.answersSubFrame,textvariable=self.Answer3Var,bg=BACKGROUND_COLOR2,fg=TEXT_COLOR,font=("Arial",18,"bold"),padx=10,pady=10,anchor="w",relief="flat",activebackground=BACKGROUND_COLOR1,activeforeground=TEXT_COLOR,command=self.Answer3Select)
        self.Answer3Button.place(x=4,y=184,width=806,height=86)
        self.Answer4Var = StringVar()
        self.Answer4Var.set(randomizedAnswers[3])
        self.Answer4Button = Button(self.answersSubFrame,textvariable=self.Answer4Var,bg=BACKGROUND_COLOR2,fg=TEXT_COLOR,font=("Arial",18,"bold"),padx=10,pady=10,anchor="w",relief="flat",activebackground=BACKGROUND_COLOR1,activeforeground=TEXT_COLOR,command=self.Answer4Select)
        self.Answer4Button.place(x=4,y=274,width=806,height=86)
        # Here a frame is being created for the confirmation button
        # This frames only purpose is to act as the border for the button
        self.confirmFrame = Frame(self.questionFrame,bg=BORDER_COLOR)
        # Placing the frame in the correct position
        self.confirmFrame.place(x=618,y=558,width=214,height=64)
        # Creating a confirmation button within the frame
        # This button will be confirm the selection and an output will be shown
        self.confirmButton = Button(self.confirmFrame,text="Confirm Answer",bg=BACKGROUND_COLOR1,fg=TEXT_COLOR,font=("Arial",17,"bold"),padx=10,pady=10,relief="flat",activebackground=BACKGROUND_COLOR2,activeforeground=TEXT_COLOR,command=self.checkAnswer)
        # Placing the button so that the border is correct
        self.confirmButton.place(x=4,y=4,width=206,height=56)
        # Mainloop is used again so that the window will show
        self.quizMaster.mainloop()
        # It will then retuirn the score the user gets either 0, 3, 7 or 10
        return self.score

    def Answer1Select(self):
        """This method will be run if the first button is pressed"""
        # if no button is selected...
        if self.SelectedButton == None:
            # it will change the colour of the background of the first button
            self.Answer1Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the first button then return to the previous method
            self.SelectedButton = self.Answer1Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the first button will be set to the 'selected' colour and the others will be set to the 'unselected' colour
            self.Answer4Button.config(bg=BACKGROUND_COLOR2)
            self.Answer3Button.config(bg=BACKGROUND_COLOR2)
            self.Answer2Button.config(bg=BACKGROUND_COLOR2)
            self.Answer1Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the first button then return to the previous method
            self.SelectedButton = self.Answer1Var
            return


    def Answer2Select(self):
        """This method will be run if the second button is pressed"""
        # if no button is selected...
        if self.SelectedButton == None:
            # it will change the colour of the background of the second button
            self.Answer2Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the second button then return to the previous method
            self.SelectedButton = self.Answer2Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the second button will be set to the 'selected' colour and the others will be set to the 'unselected' colour
            self.Answer1Button.config(bg=BACKGROUND_COLOR2)
            self.Answer4Button.config(bg=BACKGROUND_COLOR2)
            self.Answer3Button.config(bg=BACKGROUND_COLOR2)
            self.Answer2Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the second button then return to the previous method
            self.SelectedButton = self.Answer2Var
            return


    def Answer3Select(self):
        """This method will be run if the third button is pressed"""
        # if no button is selected...
        if self.SelectedButton == None:
            # it will change the colour of the background of the third button
            self.Answer3Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the third button then return to the previous method
            self.SelectedButton = self.Answer3Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the third button will be set to the 'selected' colour and the others will be set to the 'unselected' colour
            self.Answer2Button.config(bg=BACKGROUND_COLOR2)
            self.Answer1Button.config(bg=BACKGROUND_COLOR2)
            self.Answer4Button.config(bg=BACKGROUND_COLOR2)
            self.Answer3Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the third button then return to the previous method
            self.SelectedButton = self.Answer3Var
            return


    def Answer4Select(self):
        """This method will be run if the fourth button is pressed"""
        # if no button is selected...
        if self.SelectedButton == None:
            # it will change the colour of the background of the fourth button
            self.Answer4Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the fourth button then return to the previous method
            self.SelectedButton = self.Answer4Var
            return
        # else it will change the colour of all the other buttons and select the correct button
        else:
            # the fourth button will be set to the 'selected' colour and the others will be set to the 'unselected' colour
            self.Answer3Button.config(bg=BACKGROUND_COLOR2)
            self.Answer2Button.config(bg=BACKGROUND_COLOR2)
            self.Answer1Button.config(bg=BACKGROUND_COLOR2)
            self.Answer4Button.config(bg=BACKGROUND_COLOR1)
            # it will set the selected button as the fourth button then return to the previous method
            self.SelectedButton = self.Answer4Var
            return


    def checkAnswer(self):
        """This method will check the answer the user has selected and will run when the confirm answer button is pressed"""
        # Here I am setting different outputs that could occur.
        # These are constant and do not change and are shown in the output box at the bottom of the window.
        unselectedAnswer = "You have not selected an answer."
        answerCorrect = ["Awesome you got that correct!","Great Work, you got that correct!","Correct Answer, Amazing Work!","Correct!","Correct, that is INSANE!"]
        answerIncorrect = "You got that incorrect."
        # If the user has not selected a button there will be a short pause
        # and the output string var will then be set to show the user that they must select a button
        if self.SelectedButton == None:
            time.sleep(DELAY)
            self.outputLabelVar.set(unselectedAnswer)
            # It will then return to the mainloop to check for another confirmation
            return
        # otherwise if the text in the selected button is the same as the correct answer
        elif (self.SelectedButton.get()) == self.correctAnswer:
            # there will be a short delay
            time.sleep(DELAY)
            # This randomly selects an item for the output from the answerCorrect list
            self.outputLabelVar.set(random.choice(answerCorrect))
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
            # If the user gets the question correct on their last try
            else:
                self.score = NO_POINTS
            # it then closes the questionFrame so that a new one can be made and return to the mainloop
            self.questionFrame.quit()
            return
        # If they have used up all their tries
        else:
            if self.tries > 2:
                # it will pause for a short time
                time.sleep(DELAY)
                # Then the output label will tell the user they are out of tries
                self.outputLabelVar.set("You got that incorrect and are out of tries.")
                # It then sets the answerConfirmed as True so that the code will advance to the next question
                self.answerConfirmed = True
                # it will then set their score to 0 points
                self.score = NO_POINTS
                # it then closes the questionFrame so that a new one can be made and return to the mainloop
                self.questionFrame.quit()
                return
            # else there will  be a short pause and it will set the output label to show how many tries they have remaining
            else:
                time.sleep(DELAY)
                # It shows the number of tries they have remaining
                self.outputLabelVar.set("{} Try Again - Tries Remaining: {}".format(answerIncorrect,(3-self.tries)))
                # They have 1 try added to the number of tries they have used and returns to the mainloop
                self.tries += 1
                return


    def randomizeAnswers(self):
        """This method is used to return a list of randomized answers for this instance"""
        # First a list is created using the incorrect answers attribute
        answers = self.incorrectAnswers
        # Then the correct answer is appended to this list
        answers.append(self.correctAnswer)
        # Lastly a this list is shuffled and returned
        random.shuffle(answers)
        return answers


    # This decorator is used to flag that this is a class method
    # It will take the cls parameter instead of self
    @classmethod
    def from_list(cls,questionList):
        """This method is used to format the data given as a list so that it can be called as an instance"""
        # This takes the first item in the list which is the question
        question = questionList[0]
        # Here the correct answer is taken which is the first item in the second item of the main list
        correctAnswer = questionList[1][0]
        # Taking a list of incorrect answers are taken which is the second tem in the second item of the main list
        incorrectAnswers = questionList[1][1]
        # This will return a string in the format Category(Question, Correct Answer, Incorrect Answers)
        return cls(question,correctAnswer,incorrectAnswers)


    def __repr__(self):
        """This method is used for developers when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Questions('{}','{}',{})".format(self.question,self.correctAnswer,self.incorrectAnswers)


    def __str__(self):
        """This method is used for users when the instance is printed it is formatted"""
        # This returns the formatted string
        return "Question: {}\nCorrect Answer: {}\nIncorrect Answers: {}".format(self.question,self.correctAnswer,self.incorrectAnswers)


# This next line is defining all the data used which includes all the categories along with each question
CategoryList = [['Geography',['What is the capital of Mongolia?',['Ulaanbaatar',['Dharkhan','Erdene','Bayankhongor']]],['How many countries border Russia?',['14',['12','17','11']]],['What is the world’s youngest country?',['South Sudan',['Serbia','Montenegro','Kosovo']]],['What is the capital of Tajikistan?',['Dushanbe',['Bishkek','Tashkent','Khujand']]],['What country borders Latvia and is to the North of Latvia?',['Estonia',['Lithuania','Belarus','Russia']]],['What is the largest continent on Earth?',['Asia',['Antarctica','Europe','North America']]],['What country has the most natural lakes?',['Canada',['India','United States','Australia']]],['Which African Country contains the most pyramids?',['Sudan',['Algeria','Egypt','Libya']]],['What is the driest place on Earth?',['McMurdo,Antarctica',['Sahara Desert','Atacama Desert','Kufra,Libya']]],['What percentage of the River Nile falls in Egypt?',['22%',['100%','43%','72%']]]],['Science',['When was the idea of the atom first introduced?',['450 B.C.',['1942','1791','1050']]],['In what type of matter are atoms most tightly packed?',['Solids',['Gases','Liquids','All are the same']]],['What is the negative particle in an atom called?',['Electron',['Positron','Neutron','Proton']]],['What planet has the most moons?',['Jupiter',['Saturn','Uranus','Mars']]],['Which method of heat transfer best describes a lava lamp?',['Convection',['Conduction','Radiation','Induction']]],['Hurricanes only form over ___?',['Warm Water',['Cold Water','Warm Land','Cold Land']]],['Where are the smallest bones in the human body?',['Middle Ear',['Eyes','Nose','Toes']]],['What is a humming bird’s heartrate?',['1260 Beats Per Minute',['60 Beats Per Minute','240 Beats Per Minute','300 Beats Per Minute']]],['What is the symbol for Silver?',['Ag',['Si','Pb','Au']]],['A light year is a unit of ___.',['Distance',['Speed','Time','Power']]]],['War',['What year did the Chinese Civil War begin?',['1927',['1947','1907','1898']]],['Which of the following was developed during World War I?',['All of These',['Plastic Surgery','Poison Gas','Blood Banks']]],['Who had a nephew that server in the U.S. Navy during World War II?',['Adolf Hitler',['Joseph Stalin','Hirohito','Benito Mussolini']]],['What percent of casualties in World War II were civilians?',['60 %',['20 %','40 %','80 %']]],['Which of the following was a claw-like weapon from India designed to fit over the knuckles?',['Bagh Naka',['Chakram','Vajra','Parashu']]],['What war lasted from June 25,1950 to July 27,1953?',['Korean War',['Vietnam War','World War II','Irish Civil War']]],['What weapon was being developed secretly at Harvard University in 1942?',['Napalm',['Bazooka','Machine Gun','Missile']]],['What percent of Russian males born in 1923 survived World War II?',['20 %',['40 %','60 %','80 %']]],['Who was the President of the Unites States during the Civil War?',['Abraham Lincoln',['Jefferson Davis','Andrew Johnson','Ulysses S. Grant']]],['Which of the following wars lasted the longest?',['French and Indian War',['World War II','Seven Years’ War','Mexican-American War']]]],['Movies',['Which one of these movies has a runtime of 85 hours?',['The Cure for Insomnia',['Dance with the Wolves','Hamlet','The Stand']]],['What is the first rule of Fight Club?',['You do not talk about Fight Club.',['There are no rules.','If this is your first night at Fight Club,you have to fight.','Only two guys a fight.']]],['What movie popularized the phrase: “May the Force be with you”?',['Star Wars',['Matrix','Star Trek','E.T.']]],['How long did it take to render each frame (1/24 of a second) of the CGI scenes in the movie Avatar (2009)?',['47 Hours',['47 Days','47 Seconds','47 Minutes']]],['What movie depicts a society in which population and the consumption of resources are maintained by killing everyone who reaches the age of 30?',['Logan’s Run',['Blade Runner','District 9','In Time']]],['In Back to the Future,where does Doc Brown get the plutonium to power his time machine?',['Libyan Terrorists',['Chinese “Businessmen” ','The Future','Russian Mob']]],['In The Martian where were the Mars exterior scenes shot?',['Jordan',['Australia','Namibia','Wyoming']]],['In Ant-Man (2015) what character disappears into a subatomic quantum realm while disabling a Soviet nuclear missile?',['Wasp',['Yellow Jacket','Ant-Man','Atom']]],['How many visible cuts are there in Birdman?',['16',['0','35','73']]],['In The Wolf of Wall Street,what did the actors snort in scenes that involved cocaine?',['B Vitamins',['Flour','Cocaine','Baby Powder']]]],['Miscellaneous Questions',['What is the only king in a deck of cards without a moustache?',['King of Hearts',['King of Diamonds','King of Spades','King of Clubs']]],['What is the largest number of children born to one woman?',['69',['23','49','32']]],['What video game features Lara Croft?',['Tomb Raider',['Street Fighter','Grand Theft Auto','Myst']]],['What is the little dot above a lower case “i” or “j” called?',['Tittle',['Whit','Jot','Dripple']]],['What is the unit of currency in Russia?',['Ruble',['Drachma','Lev','Lira']]],['Which poison do apple seeds contain?',['Cyanide',['Strychnine','Ricin','Arsenic']]],['When was diet coke invented?',['1982',['2002','1892','1962']]],['According to Japanese legend,a sick person will recover if they fold 1,000 of what type of origami?',['Crane',['Frog','Dragon','Fish']]],['What animal undertakes the world’s largest migration each year?',['Arctic Tern',['Storm Petrel','Gray Whale','Pacific Hearing']]],['What was the highest amount of money ever paid for a cow at auction?',['$ 1,300,000',['$ 130,000','$ 670,000','$ 67,000']]]]]


# Here an empty list is created which will be used to store each category in the correct format
Categories = []
# This will loop through each item in the main category list
for ctg in CategoryList:
    # This will append an instance of each category using the class method in the Category class
    Categories.append(Category.from_list(ctg))
# Here I am creating the quiz window using Tkinter
quizWindow = Tk()
# I am then using the method from the category class to do the rest of the work.
Categories[0].createQuizWindow(quizWindow)
# the mainloop function is run to show the window
quizWindow.mainloop()
