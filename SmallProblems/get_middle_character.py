


def center_of(string):
    if len(string) % 2 == 0:
        return string[len(string) // 2 - 1] + string[len(string) // 2]
    else:
        return string[len(string) // 2]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True