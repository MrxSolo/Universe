def to_uppercase(obj):
    if isinstance(obj, dict):
        # If the object is a dictionary, recurse through its keys and values
        return {to_uppercase(k): to_uppercase(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # If the object is a list, recurse through its elements
        return [to_uppercase(item) for item in obj]
    elif isinstance(obj, str):
        # If the object is a string, convert it to uppercase
        return obj.upper()
    else:
        # If the object is of any other type, return it as is
        return obj

# Example object with nested structures
example_obj = {
    'name': 'john doe',
    'age': 30,
    'address': {
        'city': 'new york',
        'country': 'usa'
    },
    'hobbies': ['reading', 'travelling'],
    'details': [
        {'info': 'some info'},
        {'info': 'more info'}
    ]
}

# Convert all keys and strings to uppercase
uppercase_obj = to_uppercase(example_obj)
print(uppercase_obj)
