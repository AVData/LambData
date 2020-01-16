'''
lambdata - a  collection of data science helper funcitons
'''


def mean(x):
    return (sum(x)/len(x))
    print(mean(x))

def median(x):
    sortedx = sorted(x)
    xlen = len(x)
    index = (xlen - 1) // 2

    if (xlen % 2):
        return sortedx[index]
    else:
        return (sortedx[index] + sortedx[index + 1])/2.0

def mode(x):
    most = max(list(map(x.count, x)))
    return list(set(filter(lambda y: x.count(y) == most, x)))

def meanMedianMode(numbers):
    return print('Mean', mean(numbers), '\n',
    'Median', median(numbers), '\n',
    'Mode', mode(numbers))


# writing a fucntino for thursday
