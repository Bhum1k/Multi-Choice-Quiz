# Programmer: Bhumik Patel
# Program: Multi-Choice Quiz
# Version: 1.0

# Purpose:
# This is a Multi-Choice Quiz which will reflect to society and is made for all
# people who would like to challenge themselves. It will have multiple Categories
# so that it can relate to a wider range of people.

# This is the very first functional quiz without GUI where the user enters a letter
# to answer the question they are asked. It has basic functionality and includes
# every single question and only uses classes as a complex technique.
# In the next version I intend to implement some sort of GUI. Which will allow the
# user to select the category they would like to access and will have buttons to
# answer the question instead of inputting a letter.

# Importing Modules
import random

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
        # Defining a list of letters to choose from as an attribute of the class
        self.letters = ["a","b","c","d"]


    def askQuestions(self):
        """This method is used to ask the user the question"""
        # Here the question is printed
        print("\n{}".format(self.question))
        # This is temporarily creating a list using the incorrect answers so that the answers can be randomized
        answers = self.incorrectAnswers
        # The correct answer is added to the temporary list of answers
        answers.append(self.correctAnswer)
        # A new list is definined as an attribute so that it can be randomized
        self.randomizedAnswers = answers
        # On this next line the list is shuffled(randomized) so that it is not obvious
        random.shuffle(self.randomizedAnswers)
        # This for loop will loop through the length of the answers list
        for answer in range(len(answers)):
            # This will print the possible answers along with a letter before it+
            print("{}) {}".format(self.letters[answer],self.randomizedAnswers[answer]))
        # This will ask the user to enter an answer represented by a letter and brought to lower case
        while True:
            userAnswer = input("\nPlease enter the corresponding letter: ").strip().lower()
            if userAnswer not in self.letters:
                print("Please enter a valid letter.")
            else:
                break
        # This if statement will check if the answer the user inputs is correct
        if self.randomizedAnswers[(self.letters).index(userAnswer)] != self.correctAnswer:
            # If it is incorrect it will print incorrect and return False
            print("Incorrect")
            return False
        else:
            # If it is correct it will print correct and return True
            print("Correct")
            return True


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

# This will define a variable which will show the users score
correct = 0
# This will loop through each category in the Categories list
for Category in Categories:
    # This will print the name of the category
    print("\n{}".format(Category.categoryName))
    # This will loop each question in the question list stored in the category class
    for question in Category.questions:
        # Here the users score will increase if they answer the asked question correctly
        if (question.askQuestions()) == True:
            correct += 1

# The users score is printed
print("You got {} correct.".format(correct))
