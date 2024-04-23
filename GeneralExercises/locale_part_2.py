
def extract_region(locale):
    return locale.split('_')[1][:2] # [1] is the second element of the list, [:2] is the first two characters of the string

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR    