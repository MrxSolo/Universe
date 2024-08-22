def to_uppercase(obj):
    if isinstance(obj, dict):
        # Recursively convert both keys and specific string values to uppercase
        return {k.upper(): to_uppercase(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # Recursively apply the conversion to each item in the list
        return [to_uppercase(item) for item in obj]
    elif isinstance(obj, str):
        # Convert strings to uppercase
        return obj.upper()
    else:
        # Return non-string types as is
        return obj

# Apply the function to your nested structure
uppercase_obj = to_uppercase(example_obj)
print(uppercase_obj)
