# if Quotient is 0, then that number is not prime number
class prime_number:
 def __init__(self,numberth):
    number=2
    a=0
    numberth_counter=1
    #numberth=int(input("what numberth do you want?"))
    while True:
     if numberth<1:
         print('Input is wrong')
         break
     if number<4:                          # all numbesr 0f under 4 is prime
        if numberth_counter==numberth:    # numberth=4
            print(number)
            a=len(input("quit?"))
            if a > 1:
                break
            number=2
            a=0
            numberth_counter=1
            numberth=input("what numberth do you want?")
            try:
                numberth=int(numberth)
                continue
            except:
                numberth=0
                continue
        numberth_counter+=1
        number+=1
        continue
     if number>3:
        for by in range(2,number-1):
            not_prime=0
            if number%by!=0:    # condition of prime number
                continue
            else:               # condition of non prime number. it will be marked
                not_prime=1     # mark of non prime number
                break           # you don't have to run more.
     if not_prime==0: # this is prime nuber so check the numberth_counter and numberth
        #print(number,'  ',numberth_counter) # For showing all prime nuber until i get the number i want
        if numberth_counter==numberth: # This is the number that i'm looking for!
            print(number,numberth_counter)
            a=len(input("quit?"))
            if a > 1:
                break
            number=2
            a=0
            numberth_counter=1
            numberth=input("what numberth do you want?")
            try:
                numberth=int(numberth)
                continue
            except:
                numberth=0
                continue
        else:
            numberth_counter+=1
            number+=1
        #print(number,"is prime number")
     else: # this is not prime so move it on to next number.
        number+=1
        #print(number,"is not prime number")
     if a > 1: # If you fine the prime number. then we have a=2 so be able to quit.
        break
