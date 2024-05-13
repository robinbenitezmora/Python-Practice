

def friday_the_13ths(year):
    import datetime
    count = 0
    for month in range(1, 13):
        if datetime.datetime(year, month, 13).weekday() == 4:
            count += 1
    return count

print(friday_the_13ths(1986))      # 1
print(friday_the_13ths(2015))      # 3
print(friday_the_13ths(2017))      # 2
print(friday_the_13ths(2018))      # 1
print(friday_the_13ths(2019))      # 2
print(friday_the_13ths(2020))      # 2
print(friday_the_13ths(2021))      # 1
print(friday_the_13ths(2022))      # 2
print(friday_the_13ths(2023))      # 1
print(friday_the_13ths(2024))      # 2
