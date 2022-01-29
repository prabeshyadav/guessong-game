number= 67;

count=0;

while True:
    count +=1;

    guss=int(input("guess your number "))

    if guss>number:
        print("your guess is too high")

    elif guss<number:
        print("your guess is too small")
        

    elif guss==number:
        print("conguralation you did it")

        break

print("thankss for playing!");