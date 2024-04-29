def blah(*args):
    nums = [*args]
    start = 0
    for num in nums:
        start = start + int(num)
    return start


print(blah(1, 2, 3, 4, 5, 6))

# def blah(*args):
#     print([*args])


# blah(1, 2, 3, 4, 5)
