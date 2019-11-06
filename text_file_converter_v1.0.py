# Programmer: Bhumik Patel
# Program: Text File Converter
# Version: 1.0

# Purpose:
# This program will be used by the main quiz program to convert from text file to
# the needed  list. It is also able to do it the other way around and can write to
# the list in the correct format to the text file.

def convertFromList(Categories):
    """This function is used to convert the list of categories into the text file"""
    # I am creating a list so that it can be iterated through afterwards
    writeToFileList = []
    # Going through each Category in the Categories List
    for Category in Categories:
        # Going through each of the questions in the current Category
        for num1, questions in enumerate(Category):
            # The first item in the list is the Category Name so it is seperated
            if num1 == 0:
                categoryName = questions
                writeToFileList.append("Category: {}\n".format(categoryName))
            # Otherwise, going through each question in the questions list
            else:
                for num2, question in enumerate(questions):
                    # The first item in the list is the Question so it is seperated
                    if num2 == 0:
                        writeToFileList.append("Question {}: {}\n".format(num1, question))
                    # Otherwise, going through the answers in the questions list
                    else:
                        for num3, answers in enumerate(question):
                            # The first item in the list is the correct answer so it is seperated
                            if num3 == 0:
                                correctAnswer = answers
                                writeToFileList.append("Correct Answer: {}\n".format(answers))
                            # Otherwise, going through the incorrect answers in the question
                            else:
                                incorrectAnswers = answers
                                # The incrrect answers are in a list so they are seperated
                                for num4, incorrectAnswer in enumerate(incorrectAnswers):
                                    writeToFileList.append("Incorrect Answer {}: {}\n".format((num4+1), incorrectAnswer))
    # List is returned to be used for a file
    return writeToFileList


def correctCategoryFormat(ctgList):
    """This function is used to convert a list of data for categories into the correct format"""
    # Creating an empty list to be used to store information about the ctgData
    # Format is [Index of Start of Category, Number of Questions in Category] multiple per list
    ctgData = []
    # This loop will generate the data for the ctgData list which will be used later
    for ctgListIndex, ctgListItem in enumerate(ctgList):
        # Finding all the start locations(indexes) of each Category and appending as new list within ctgData list
        if ctgListItem[0:(ctgListItem.index(": ") + 2)] == "Category: ":
            ctgData.append([ctgListIndex])
    # This loop will find the number of questions in each category and append it to the list
    for ctgDataIndex, data in enumerate(ctgData):
        # Checking if the item is the last item in the list
        if ctgData[ctgDataIndex] != ctgData[-1]:
            # If it is not, the number of questions in the Category is calculated and appended
            ctgData[ctgDataIndex].append((int((ctgData[ctgDataIndex+1][0])-int(ctgData[ctgDataIndex][0])-1) / 5))
        else:
            # If it is, the number of questions in the Category is calculated and appended
            ctgData[ctgDataIndex].append(int((ctgList.index(ctgList[-1])-(ctgData[ctgDataIndex][0])) / 5))
    # Creating an empty list which will be filled with data in the correct format to be used for the quiz
    formattedList = []
    # Looping through each item of the ctgData list and also providing the index of the item
    for ctgIndex, ctg in enumerate(ctgData):
        # Generating a temporary varaible and saving it as the category name
        tempName = ctgList[ctg[0]]
        # Appending the category name but removing everything before ": "
        formattedList.append([tempName[(tempName.index(": ") + 2):]])
        # Looping through for the number of questions in the category
        for question in range(int(ctg[1])):
            # This will gather the string for the question from the data from the text file
            tempQuestion = ctgList[(ctg[0] + 1) + (5 * question)]
            # Everything before ": " is removed and it is added to the final list in the correct position
            formattedList[ctgIndex].append([tempQuestion[(tempQuestion.index(": ") + 2):]])
            # An empty list is created to accomodate for the answers
            answerList = []
            # The number of answers is 4 so we loop 4 times for each answer
            for answers in range(4):
                # Gathering the full answer (unformatted)
                answer = ctgList[(ctg[0]+ 2 + answers + (5 * question))]
                # If it is the first answer (correct answer) we add it to the list
                if answers == 0:
                    # Removing everything before ": " and appending to the list
                    answerList.append(answer[(answer.index(": ") + 2):])
                # If it is the second answer (first occuring incorrect answer) then we create an empty list with the answer within
                elif answers == 1:
                    answerList.append([answer[(answer.index(": ") + 2):]])
                # If it is the third or fourth answer (other 2 incorrect answers) then it is added to the list we created
                else:
                    answerList[1].append(answer[(answer.index(": ") + 2):])
            # The entire list with all the answers is then inserted into the final list in the correct position
            formattedList[ctgIndex][question + 1].append(answerList)
    # The fully formatted list is then returned
    return formattedList


def readTextFile(fileLocation, type):
    """This function will read a text file with values on each line and return them as a list"""
    # Opening the text file in read mode
    textFile = open(fileLocation, "r")
    # Saving each line of the file as an item in a list
    textList = textFile.readlines()
    # Closing the text file
    textFile.close()
    # Creating a temporary list
    tempList = []
    # Each item in the list has \n at the end
    for text in textList:
        # We must remove the \n and append it to the temporary list
        tempList.append(text.strip())
    # This statement is checking the type of text file we are using. Currently only one type exists.
    if type == "Category":
        # Converting the text file data into the correct format
        tempList = correctCategoryFormat(tempList)
    # Returning the list
    return tempList


def writeTextFile(fileLocation, type, dataList):
    """This function will write to the text file and erase all other data"""
    # Opening the text file in write mode
    textFile = open(fileLocation, "w")
    # Overwriting the text file with the new data
    textFile.writelines(convertFromList(dataList))
    # Closing the text file
    textFile.close()
