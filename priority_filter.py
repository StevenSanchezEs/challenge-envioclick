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


def sort_list(items, key, descending=True):
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if descending:
                if items[j][key] < items[j + 1][key]:
                    # Intercambio manual
                    temp = items[j]
                    items[j] = items[j + 1]
                    items[j + 1] = temp
                    swapped = True
            else:
                if items[j][key] > items[j + 1][key]:
                    # Intercambio manual
                    temp = items[j]
                    items[j] = items[j + 1]
                    items[j + 1] = temp
                    swapped = True
        if not swapped:
            break
    return items


def filter_by_criteria(criteria, entry):
    valid = []
    invalid = []
    for item in entry:
        is_valid = True
        # Recorremos cada criterio y evaluamos:
        for attribute, operator, value in criteria:
            if not check_operator(item.get(attribute), operator, value):
                is_valid = False
                break
        if is_valid:
            valid.append(item)
        else:
            invalid.append(item)
    sorted_valid = sort_list(valid, "priority", descending=True)
    return sorted_valid + invalid
