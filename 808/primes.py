primes = []

primes_dict = {}

# This is a file that contains the first 2,000,000 primes separated by spaces.
f = open('primes_file.txt', 'r')

for line in f:
    data = line.strip().split()
    for prime in data:
        int_val = int(prime)
        primes.append(int_val)
        primes_dict[int_val] = None
