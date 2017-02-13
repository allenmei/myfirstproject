
def factorial(max):
    product = 1
    for i in range(1, max):
        product *= i
    return product

def main():
    output = 0.0

    for i in range(1, 50):
        output += 1/factorial(i)

    print( "%.50f" % (output))
    return 0

main()