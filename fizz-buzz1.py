
# fizzbuzz() will accept 
# The function Fizz Buzz accepts a stop number, a custom fizz number and a custom buzz number. However if the user inputs no values there are pre-set defaults.
def fizzbuzz(stop=100,fizz=3,buzz=5):
    print(f"For Fizz as {fizz} and Buzz as {buzz} until {stop}, the sequence is:")
    for i in range(stop):
        if (i+1) % fizz == 0 and (i+1) % buzz == 0:
            print("FizzBuzz")
        elif(i+1) % fizz == 0:
            print("Fizz")
        elif(i+1) % buzz == 0:
            print("Buzz")
        else: print(i + 1)

#set to colour of tile for graphical representation - can be merged with Conways Game of life to create an animation

def conwaymatrix():
    #will evaluate the raneg put in to create a table or map to be displayed on the GUI
    #special pattern/event for prime numbers
    #for numbers with no division under 10 the final row will be trucated 
        #in advanced versions a random cell will be taken out



def main():
    fizzbuzz(20,4,3)

main()