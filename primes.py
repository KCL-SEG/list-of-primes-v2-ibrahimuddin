def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError
    list = []
    i = 0
    number = 2
    while i<number_of_primes:
        if(is_prime(number)):
            list.append(number)
            number+=1
            i+=1
        else:
            number+=1

    return list

def is_prime(number):
    if number==2 or number==3:
        return True
    if number%2==0:
        return False
    if number%2!=0:
        for i in range(3,number):
            if number%i==0:
                return False
    return True

print(primes(0))