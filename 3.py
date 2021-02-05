
def logBase2 (number): 
    if number == 1: 
        return 0
    else:
        return 1 + logBase2(int(number/2))
print("result " + str(logBase2(16)))