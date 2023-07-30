#Asking user for their name
name = input ("What's your name? ").strip().title()

#Remove Whitespaces from the String
# name = name.strip()
# name = name.capitalize() 
# name = name.title() 

#Combined
# name = name.strip().title()

# print("Hello, ",name,"!")
print("Hello,",name,"!") #Greet the user!
print("Hello, " + name,"!") #Greet the user!

# Printing options
# print ("Hello, ", end="")
# print (name)

# Printing options
# print ("Hello, ", sep=" ", end="") # Sep->separation
# print (name)

##Printing Double Quation (Escape char)
print (F"Hello, \" {name} \"")
