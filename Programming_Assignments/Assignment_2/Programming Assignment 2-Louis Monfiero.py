#Louis Monfiero 016336266
#Katherine Seng
#Dustin Nguyen 016873907

#incomplete - final version done on Katherine's laptop

#def modulus_product(base, exponent, divisor):
    
   # return mod_product


def isPrime(L):

    return L

def main():
    temp[2, 5, 8, 10, 13]
    print(isPrime(temp))

n = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nL = []
test = False
if min(n) > 1:
    for i in n:
        for j in range(2, i):
            if (i % j) == 0:
                # print('False')
                test = True
                break
        if (test):
            nL.append(i)
            test = False

# for i in n:
#     for j in nL:
#         if i == j:
#             n.remove(i)
yeet = [i for i in n if i not in nL]
print(n)        
print(nL)
print(yeet)