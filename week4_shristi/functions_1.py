import ctypes

# Load the shared library
lib = ctypes.CDLL('./libfunctions.so')

# Define argument and return types
lib.square.argtypes = [ctypes.c_int]
lib.square.restype = ctypes.c_int

lib.concat_strings.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.concat_strings.restype = None

lib.is_prime.argtypes = [ctypes.c_int]
lib.is_prime.restype = ctypes.c_int

# Call the square function
result_square = lib.square(5)
print(f"Square of 5: {result_square}")

# Call the concat_strings function
str1 = b"Hello, "
str2 = b"World!"
result_str = ctypes.create_string_buffer(50)  # Buffer for the result
lib.concat_strings(str1, str2, result_str)
print(f"Concatenated string: {result_str.value.decode()}")

# Call the is_prime function
number = 17
result_prime = lib.is_prime(number)
print(f"Is {number} a prime number? {'Yes' if result_prime else 'No'}")
