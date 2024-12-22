def count_pairs(gloves):
    color_count = {}
    pairs = 0

    # Count the occurrences of each color
    for color in gloves:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # Calculate the number of pairs for each color
    for count in color_count.values():
        pairs += count // 2

    return pairs


# Using list comprehension
lst = [int(x) for x in input("Enter the numbers separated by space: ").split()]
print(lst)
print(count_pairs(lst))
