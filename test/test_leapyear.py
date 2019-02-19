#Test case
def test_normal_leap_year():
    assert is_leap(1996)
def test_normal_common_year():
    assert not is_leap(2001)
def test_atypical_common_year():
    assert not is_leap(1900)
def test_atypical_leap_year():
    assert is_leap(2000)

#code 1

#def is_leap(year):
    #if year%100==0:
        #if year%400==0:
           # return True
        #return False
        
    #return year%4==0

#code 2
#def is_leap(year):
    
    #if year%100==0 and not year%400==0:
        #return False
    #return year%4==0

#code 3
def is_atypical_common_(year):
    return year%100==0 and not year%400==0
def is_leap(year):
    if(test_atypical_common_year(year)):
        return False
        
    



    
        

