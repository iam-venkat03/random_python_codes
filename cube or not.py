#Guess and Ceck
#FInding cube roat
cube=int(input("ENTER"))
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
            print(cube,"Not a perfect cube")
else:
     if cube < 0 :
          guess = -guess
     print("Cube root of "+str(cube)+" is "+str(guess))
