


def xor(comment1, comment2):
 if (comment1 and not comment2) or (comment2 and not comment1):
  return True
 return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
