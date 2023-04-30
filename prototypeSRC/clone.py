import copy, sys

def clone(object):
    newObject = copy.deepcopy(object)
    return newObject

sys.modules[__name__] = clone