# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')

def Namaste(name):
    print(f'Namaste {name}')
    
def getSum(num1 , num2):
    return num1 + num2
x= getSum(1,2)
print(x) 

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

sayNamaste= lambda name: print(f'hello salam namaster {name}')
sayNamaste("chal Shoriya")
print(getSum(10, 3))
