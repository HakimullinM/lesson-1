percent = range
numbs = {11,12,13,14}
for percent in range(100):
    i = percent + 1
    if i in numbs:
        print(percent, "процентов")
    elif percent % 10 == 1:
        print(percent, "процент")
    elif percent % 10 > 1 and i % 10 <5:
        print(percent, "процента")
    else:
        print(percent, "процентов")