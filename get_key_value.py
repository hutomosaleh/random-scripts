"""
   Returns the first key value of the searched key name of a dictionary.
"""

def get_key_value_by_name(dictionary, name):
    if type(dictionary) is dict:
        for key in dictionary.keys():
            if key == name:
                result = dictionary[key]
                return result
            else:
                if type(dictionary[key]) is dict:
                    result = get_struct_by_name(dictionary[key], name)
                    if result is not None:
                        return result
