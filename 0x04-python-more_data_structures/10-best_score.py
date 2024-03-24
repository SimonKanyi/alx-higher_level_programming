#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        str: The key with the biggest integer value, or None if no score found.

    """
    if a_dictionary:
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None

# Test the function
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
