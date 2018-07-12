import os

os.system('clear')

#naughty strings

# If quotations are improperly used in a stream, the error will say, "Syntax Error: invalid syntax".
#For Example:

#ray= [''asherah's powers are growing.']
#print(ray)

#The code was not recognized because the apostrophe interrupted the code and confused the code. To fix this,
#you would need to include a back slash to began the quote inside the stream and use another backslash at the end
#to escape that quote. Another mistake is using double quotes instead of single quotes.
#Corrected Example:

ray= ['\'Asherah\'s powers are growing.']
print(ray)
#fruits and vegetables

x= ["apple", "banana", "carrot"]
print(x[0]+'s', x[1]+'s', "and", x[2]+'s')



