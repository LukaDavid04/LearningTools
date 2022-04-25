def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 4
b = 6


print('LCM of', a, 'and', b, 'is', lcm(a, b))
