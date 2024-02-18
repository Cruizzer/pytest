def add_strings(str1, str2):
    return str1 + str2


def combine_functions(func1, func2):
    def combined_function(str1, str2):
        result1 = func1(str1)

        result2 = func2(str2)

        return add_strings(result1, result2)
    return combined_function

# Example usage


def uppercase_string(string):
    return string.upper()


def lowercase_string(string):
    return string.lower()


combined = combine_functions(uppercase_string, lowercase_string)
result = combined("Hello", "World")

print(result)  # Output: HELLOworld
