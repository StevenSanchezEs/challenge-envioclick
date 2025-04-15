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
