def has_42(*args):
    for arg in args:
        if arg == 42:
            return True
    return False


print(has_42(41, 'f', 43, 44))
