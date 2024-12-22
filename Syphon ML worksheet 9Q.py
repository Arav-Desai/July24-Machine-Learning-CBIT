def are_consecutive(arr1, arr2):
    combined = arr1 + arr2
    min_val = min(combined)
    max_val = max(combined)

    # Check if the combined array forms a consecutive sequence
    return len(combined) == (max_val - min_val + 1) and len(set(combined)) == len(combined)


n = ''
arr1 = []
arr2 = []
a = 0
while n != "n" or n != "N":
    a = int(input("Enter the number for 1st list:"))
    arr1.append(a)
    n = input("Do you still want to continue ?")

while n != 'n' or n != 'N':
    a = int(input("Enter the number for 2st list:"))
    arr2.append(a)
    n = input("Do you still want to continue ?")

print(are_consecutive(arr1, arr2))  # Output: False