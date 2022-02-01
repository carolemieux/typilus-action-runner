class NumWrapper:
    def __init__(self, value):
        self.value = value

    def pretty_print(self):
        return f"I am the number with value {self.value}"

    def get_value(self):
        return self.value

def get_wrapped_value(value):
    return NumWrapper(value)

def add(val1, val2):
    assert isinstance(val1, NumWrapper) and isinstance(val2, NumWrapper)
    int_val1 = val1.get_value()
    int_val2 = val2.get_value()
    return get_wrapped_value(int_val1 + int_val2)

def multiply(val1, val2):
    int_val1 = val1.get_value()
    int_val2 = val2.get_value()
    return get_wrapped_value(int_val1 * int_val2)

def is_pretty_print_string(intval, string):
    if intval.pretty_print() == string:
        return True
    else:
        return False


