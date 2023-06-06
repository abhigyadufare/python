# Checks whether the number is even or odd
def check_odd_even(number):
  if number%2 == 0 :
    print(f"{number} is an even number")
  elif number == int(number) :
    print(f"{number} is an odd number")
  else :
    print(f"{number} is not a whole number")

# Calculates the total number of factors 
def get_factors(number) :
  factors = []
  int_type = int(number)
  if number != int_type :
    factors.append(1)
    print(f"{number} has no factors")
  elif number < 0 :
    iteration_index = number
    while iteration_index < 0 :
      if number%iteration_index == 0 :
        factors.append(iteration_index)
      iteration_index += 1
    iteration_index = 1
    max_positive_factor = number * -1
    while iteration_index <= max_positive_factor :
      if number%iteration_index == 0 :
        factors.append(iteration_index)
      iteration_index += 1
    print(f"The factors of {number} are: {factors}")
  else : 
    factors = []
    for iteration_index in range(number) :
      iteration_index += 1
      if number%iteration_index == 0 :
        factors.append(iteration_index)
    print(f"The factors of {number} are: {factors}")
  return factors

# Checks if it is an iteger or a float
def check_datatype(number) :
  convert_to_int = int(number)
  if number == convert_to_int :
    print(f"{number} is an interger")
  else :
    print(f"{number} is a float")

# Checks whether the number is positive or negative
def check_integer(number) :
  if number > 0 :
    print(f"{number} is a positive number")
  else :
    print(f"{number} is a negative number")

# Checks if the number is prime or not
def check_prime(number, factors) :
  if len(factors) == 2 :
    print(f"{number} is a prime number")
  else :
    print(f"{number} is not a prime number")


# Use this function to analyze with all the functions
def analyze_number(number) :
  check_integer(number)
  check_odd_even(number)
  factors = get_factors(number)
  check_prime(number, factors)
  check_datatype(number)

analyze_number(-64)
analyze_number(73)
analyze_number(56.7)


