
def creditcard():
    entry = input('Enter a credit card number with no spaces:')
    cc = list(map(int, list(entry)))
    print(cc)
    return

creditcard()