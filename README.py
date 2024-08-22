def to_uppercase(obj):
    if isinstance(obj, dict):
        # Recursively convert both keys and values to uppercase
        return {to_uppercase(k): to_uppercase(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # Recursively apply the conversion to each item in the list
        return [to_uppercase(item) for item in obj]
    elif isinstance(obj, str):
        # Convert strings to uppercase
        return obj.upper()
    else:
        # Return non-string types as is
        return obj

# Example object with up to three levels of nesting
example_obj = {
    'level1': {
        'level2a': {
            'level3a': 'some value',
            'level3b': 'another value'
        },
        'level2b': {
            'level3c': 'more value',
            'level3d': 'yet another value'
        }
    },
    'simpleKey': 'simple value',
    'simpleList': ['item1', 'item2']
}

# Convert all keys and strings to uppercase
uppercase_obj = to_uppercase(example_obj)
print(uppercase_obj)
