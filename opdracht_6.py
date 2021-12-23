from keyword import iskeyword

def contains_keyword(*args):
    for arg in args:
        if iskeyword(arg):
            return True
    else:
        return False

print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chickens are evil", 42))
print(contains_keyword("four", "for", "if"))
print(contains_keyword("blabla", "doggo", "crab", "anchor"))
print(contains_keyword("grizzly", "ignore", "return", "False"))
