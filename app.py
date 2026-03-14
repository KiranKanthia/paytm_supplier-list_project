# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check Armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

# Function to check palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Lists to store results
primes = []
odds = []
evens = []
armstrongs = []
palindromes = []

# Loop through numbers 1 to 300
for num in range(1, 301):
    if is_prime(num):
        primes.append(num)
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
    if is_armstrong(num):
        armstrongs.append(num)
    if is_palindrome(num):
        palindromes.append(num)

# Print results
print("Prime numbers between 1 and 300:", primes)
print("Odd numbers between 1 and 300:", odds)
print("Even numbers between 1 and 300:", evens)
print("Armstrong numbers between 1 and 300:", armstrongs)
print("Palindrome numbers between 1 and 300:", palindromes)