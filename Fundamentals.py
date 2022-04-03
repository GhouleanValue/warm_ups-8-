#1 | Flow logic

 value = True

   if value:
     print("my value is true")
   else:
    print('my value is not true')

#2 | Extended flow logic block of code

       location = 'School'

       if location == 'Down Town':
         #print('Main st.')
       elif location == 'School':
          print('computer class')
       elif location == 'store':
          print('Grocery Store')
       else:
          print('Location not known')


#3 | A list of methods to remember

# To make this a better exercise for any beginners, lets use the help function.

# I will leave a list of methods below. Use the help function if you are not familiar with them.

# Create a simple list

lst = [1,2,3,4,5] # a basic list

lst.append(77) # each method requires this .method syntax after the variable name which in our case is lst.
# if you are wondering what the () is, that is the space for an argument and in our case we placed 77 for our argument.

print(lst)

# Try this list of methods

 #append
 #count
 #extend
 #insert
 #pop
 #remove
 #reverse
 #sort
