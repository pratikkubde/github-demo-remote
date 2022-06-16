#add
def add (x,y)
    return (x+y)
#sub
def subtract(x,y)
    return (x-y)
#mul
def multiply(x,y)
    return (x*y)
#div
def divide(x,y)
    if(y==0)                    # On master branch
        return DIVIDE_BY_0_ERROR
    else
        return x/y
#Square Implementation
def square(x)
    return x*x