import copy, sys

def clone(object):
    newObject = copy.deepcopy(object)
    return newObject

sys.modules[__name__] = clone

class example:
    x = "hello"
    y = 12345

test = example
print(test.x + str(test.y))
copied = clone(test)
print(copied.x + str(copied.y))