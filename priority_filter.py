def check_operator(value, operator, reference):
    if operator == "=":
        return value == reference
    elif operator == ">=":
        return value >= reference
    elif operator == "<=":
        return value <= reference
    elif operator == ">":
        return value > reference
    elif operator == "<":
        return value < reference
    else:
        raise ValueError("Unsupported operator: " + operator)
