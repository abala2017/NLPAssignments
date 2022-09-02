import sys
import re
import pickle

#3
class Person:

    def __init__(self, last, first, midIn, ID, officeNum): ## the initializer
        ## assigning the inputs as the variables in the person object
        self.last = last 
        self.first = first
        self.midIn = midIn
        self.ID = ID
        self.officeNum = officeNum
        
    def display(self): ## display function
        ## printing out the person details
        print("Employee id: " + self.ID)
        print("\t" + self.first + " " + self.midIn + " " + self.last)
        print("\t" + self.officeNum)



#4
def processInput(filename):

    people = {} ## creating the dictionary
    f = open(filename,'r') ## opening the file from the user input
    line = f.readline() ## skipping the first line with the columns
    line = f.readline() ## getting the next line of text
    while line: ## making sure we haven't reached the end of the file
        
        #4a
        data = line.split(",") ## splitting the line by commas
        
        #4b
        last = data[0].lower().capitalize() ## lowercasing the entire the last name and capitalizing the first letter
        first = data[1].lower().capitalize() ## lowercasing the entire the first name and capitalizing the first letter
        
        #4c
        midIn = data[2].upper() ## getting and upper casing the middle initial
        hasInitial = (len(data[2]) == 1) ## checking if there is a middle initial
        if(hasInitial == False): ## if there is no middle initial give an X
            midIn = 'X' ## setting the X
        
        #4d
        ID = data[3].upper() ## upper casing the beginning of the ID
        if not (re.match('[A-Z][A-Z][0-9][0-9][0-9][0-9]', ID)): ## making sure the ID matches the regex format
            print("ID invalid: " + str(ID)) ## printing the invalid ID if it doesn't match the format
            print("ID is two letters followed by 4 digits") ## Printing rules
            ID = input("Please enter a valid id: ").upper() ## prompting for the user to enter in the ID again
        
        #4e
        officeNum = re.sub('\D', '',data[4]) ## removing all the non digits to from the office number from the arguements
        officeNum = officeNum[:3] + '-' + officeNum[3:6] + '-' + officeNum[6:] ## add the dashes
        
        #4f
        p = Person(last,first,midIn,ID,officeNum) ## creating the person object using the extracted data
        if(ID in people): ## iterating through the IDs
            print("Dulicate ID found : " + ID) ## making aware of duplicate IDs
        people[ID] = p ## putting the new person in the dictionary
        
        line = f.readline() ## going to the next line
        
    f.close() ## close the file
    
    #4g
    return people ## return the dictionary



if __name__ == '__main__':

    people = processInput(sys.argv[1]) ## We pass the filename to the function to process the files and save the function return to the people variable
    pickle.dump(people, open("people.p","wb")) ## Here we dump the people dictionary to a pickle file
    peoplePickle = pickle.load(open("people.p", "rb")) ## Here we load the dictionary back from the pickle file
    print("\n\nEmployee list: ") ## We start printing the people objects
    for person in peoplePickle.values(): ## iterating through the dictionary
        print("\n")
        person.display() ## displaying the people object




