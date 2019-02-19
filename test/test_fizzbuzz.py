#fizzbuzz program
#utlity function
def checkfizzbuzz(value,expected):
    actual=fizzbuzz.fizzbuzz(value)
    assert actual==expected
#Test case
def test_canIcallfizzbuzz():
    fizzbuzz(1)
def test_return1with1():
    checkfizzbuzz(1,"1")
def test_return2with2():
    checkfizzbuzz(2,"2")
def test_returnFizzwith3():
    checkfizzbuzz(3,"Fizz")
def test_returnBuzzwith5():
    checkfizzbuzz(5,"Buzz")
def test_returnFizzwith6():
    checkfizzbuzz(6,"Fizz")
def test_returnBuzzwith10():
    checkfizzbuzz(10,"Buzz")
def test_returnFizzBuzzwith15():
    checkfizzbuzz(15,"FizzBuzz")

#code 1
def fizzbuzz(value):
    if(value%3==0):
        if(value%5==0):
            return "FizzBuzz"
        return "Fizz"
    if(value%5==0):
        return "Buzz"
    return str(value)

#code 2
#def ismultiple(value,mod):
    #return value%mod==0
#def fizzbuzz(value):
    #if ismultiple(value,3):
        #if ismultiple(value,5):
            #return "fizzbuzz"
        #return "fizz"
    #if ismultiple(value,5):
        #return "buzz"
    #return str(value)

