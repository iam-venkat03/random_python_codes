cube=int(input("ENTER"))
epsilon=0.1
increment=0.01
count=0
guess=0.0
while abs(guess**3 - cube)>=epsilon and guess**3<=cube:
    guess+=increment
    count+=1;
print("number of guesses:",count)
print(guess,"is the closest cube root for",cube)
    
