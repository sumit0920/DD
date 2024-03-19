print("Sumit\nSharma") # To change the line, added a \n between them.

phrases = "This is "
print (phrases+  "Sumit")   #This is called catination


#Function
phrase= "This is first function"
print(phrase.lower()) #Function to convert the entirely string to lower case
print(phrase.upper()) #Function to convert the entirely string to upper case

#Use two functions one after another for the same function

phrase= "This is second function"
print(phrase.lower().islower()) #Function to check the entire string to lower case
print(phrase.upper().isupper()) #Function to check the entire string to upper case

#To Know the length of the string
phrase= "This is third  function"   
print(len(phrase)) #Function to check the length of the string

#To print specific characters

print(phrase[9]) #It starting with zero like 0,1,2,3..., so have to mention that particular number which equal to string to print specific characters


#Index Functions:- tell us where is the specific character in the string.
print (phrase.index("f")) #This is called passing the perimeter 

#Replace Functions:- This function replace the string with  a new string.
print(phrase.replace("third", "foruth"))



#To be continued...