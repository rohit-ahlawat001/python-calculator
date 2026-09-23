# cresting the program for the exctption handlingDivisible by Zero

def checkDivisionError(a, b):
    c = None
    try:
        c = a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("Kindly enter the vlaid values")
    finally:
        print(c)
        return c
    
checkDivisionError(10, 2)

def throwError(valOne, valTwo):
    valThree = None
try:
    valThree = valOne / valTwo
except ZeroDivisionError:
    raise ZeroDivisionError("Kindly add the valid number")