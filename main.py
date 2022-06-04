# -------------------------
# PART 1: Ask user for two numbers
# -------------------------

# validateInput(num) function: checks if the user inputted a number over -1
def validateInput(num):
  validatedNum = num; # Set a local variable equal to the inputted value
  
  while (not validatedNum.isnumeric() and validatedNum != '-1') or (int(validatedNum) < -1 or int(validatedNum) % 1 != 0): # While the current input is a string, a number less than -1 or a decimal
    validatedNum = input("Invalid response. Please input a positive integer (-1 if you want to quit the program): "); # Ask the user for a number, set it to that variable
  return validatedNum; # Return validated number once it is valid

# Check if the user wants to exit the program
def checkToQuit(input):
  if input == '-1': # If the input is -1
    return True; # Return true, otherwise return false
  return False;

# -------------------------
# PART 2: Find the GCF of the numbers
# -------------------------

# Get the factors of a number. Input must be a number value
def getFactors(num):
  numInt = int(num) # Turn data type to integer
  factors = []; # Create an empty list
  for i in range(numInt + 1): # Loop through all integers between 0 and the inputted number
    if i != 0 and numInt % i == 0: # If the looped number is not 0 and the number divided by the looped number is 0
      factors.append(i); # Add the looped number into the list
  return factors; # Return the list

# Get the factors between two numbers. Inputs must be two lists containing the factors of the number (use getFactors(num) to get these lists)
def getCommonFactors(p, q):
  commonFactors = []; # Create new empty list

  # Loop through all the elements of both factor lists
  for pInd in p:
    for qInd in q:
      if pInd == qInd: # If a factor of p is equal to a factor of q
        commonFactors.append(pInd); # Put the common factor into the list
  return commonFactors; # Return the list

# Get the greatest common factor of a list of factors. Input must be a list of common factors (use getCommonFactors(p, q) to get this list)
def getGCF(commonFactors):
  gcf = 1; # Create a new variable, set it to 1 (math theory: all integers have a common factor of 1)
  for fact in commonFactors: # Loop through the list of factors
    if fact > gcf: # If the factor is greater than the gcf
      gcf = fact; # Set the gcf to this new number
  return gcf; # Return the gcf

# -------------------------
# PART  3: Find the LCM of the numbers
# -------------------------

# Get the lcm of two numbers, Inputs must be two numbers
def getLCM(p, q):
  product = int(p) * int(q); # Convert p and q to integers and multiply them
  return int(product / getGCF(getCommonFactors(getFactors(p), getFactors(q)))); # Return this product divided by the gcf

# -------------------------
# PART 4: Find the common factors of the numbers
# -------------------------

# Get all the prime factors 
def printPrimeFactors(num):
  currNum = int(num); # Convert input to integer. This number will be modified
  currNumFactors = getFactors(currNum); # Get all the factors of the current number

  # *** Simple code - prints out the prime factors, not including the amount of times they show up
  #
  # for factor in currNumFactors:
  #   if isPrimeNumber(factor):
  #     print('- ' + str(factor));
  #

  # *** More complex code - this will print all the prime factors with the number of times they show up
  continueLoop = True; # Create a variable that should determine if the below 'while' loop should continue looping
  while continueLoop:
    if num == '1': # If the starting number is 1
      continueLoop = False; # Break the loop
      print('- None') # 1 has no prime factors, so print "None" to the chat
    elif currNum == 1: # If the current number is 1
      continueLoop = False; # Break the loop
    for factor in currNumFactors: # For each factor in the current number's factors
      if isPrimeNumber(int(factor)): # If the factor is a prime number
        print('- ' + str(factor)) # Print it to the console
        currNum = currNum / factor; # Set the current number equal to the quotient of the current number and the prime factor
        currNumFactors = getFactors(currNum); # Update the list of the current number's factors to match the new current number
        if isPrimeNumber(currNum): # If the new current number is prime
          print('- ' +  str(int(currNum))); # Print it to the console
          continueLoop = False; # Break the 'while' loop
        break; # Break the 'for' loop

# Checks if a numebr is prime. Input must be an integer
def isPrimeNumber(num):
  if len(getFactors(num)) == 2: # If the list of factors has 2 numbers (which would be 1 and itself)
    return True; # Return true, otherwise return false
  return False;

# -------------------------
# Basic list of steps to do
# -------------------------

# Set of steps for the computer to take
def run():
  # PART 1: Get user inputted numbers
  x = validateInput(input("Please input a positive integer (-1 if you want to quit the program): ")); # Ask the user for a number
  shouldQuit = checkToQuit(x); # Check if the user wants to quit the program
  if not shouldQuit: # If the user says not to, ask for a second number
    y = validateInput(input("Please input another positive integer (-1 if you want to quit the program): "));
    shouldQuit = checkToQuit(y); # Check if the user wants to quit the program

  # If the user wants to quit the program
  if shouldQuit:
    print("Goodbye"); # Say bye. The run() function will not run again
  else: # If the user does not want to quit the program
    # PART 2: Find the GCF
    xFact = getFactors(x); # Create lists that will hold the factors of the numbers
    yFact = getFactors(y);
    gcf = getGCF(getCommonFactors(xFact, yFact)); # Get the GCF
    print('GCF=' + str(gcf)); # Concatenate strings and print the GCF
  
    # PART 3: Find the LCM
    print("LCM=" + str(getLCM(x, y))); # Use the two numbers to get the LCM then print it
  
    # PART 4: Find the prime factors
    print("Prime factors of " + x + ":") # Print a starting statement
    printPrimeFactors(x); # Print all the prime factors of x
    print("Prime factors of " + y + ":") # Print a starting statement
    printPrimeFactors(y); # Print all the prime factors of y
    run(); # Run the program again

run(); # Run the program the first time