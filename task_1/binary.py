def generate_range(start, end):
    if start > end:
        print("Start should be less than or equal to end.")
        return

    while start <= end:
        print(start)
        start += 2

# Input
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

generate_range(start, end)