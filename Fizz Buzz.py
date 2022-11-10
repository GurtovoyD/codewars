# Return an array containing the numbers from 1 to N, where N is the parametered value.
#
# Replace certain values however if any of the following conditions are met:
#
# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.
#
# Method calling example:
#
# fizzbuzz(3) -->  [1, 2, "Fizz"]

def fizzbuzz(n):
    c = []
    for i in range(1, n + 1):
        if not i % 3 and not i % 5:
            c.append("FizzBuzz")
        elif not i % 3:
            c.append("Fizz")
        elif not i % 5:
            c.append("Buzz")
        else:
            c.append(i)
    return c