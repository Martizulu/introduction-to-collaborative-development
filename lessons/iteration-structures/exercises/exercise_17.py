data = list(range(1, 101))  # Do not modify this line... I will know if you do!
log = []
for i in data:
    if (i% 5== 0 and i%3 == 0):
        log.append("FizzBuzz")
    elif i%3 == 0:
        log.append("Fizz")
    elif i%5 == 0:
        log.append("Buzz")
    else:
        log.append("idk")
