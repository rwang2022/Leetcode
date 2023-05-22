def twoSum(numbers, target):
    hashMap = {}
    for index in range(len(numbers)):
        # the two numbers that add to target
        num = numbers[index]
        diff = target - num

        # if diff is found in hashMap, return it. else add the difference to hashmap and loop.
        if diff in hashMap:
            return [hashMap[diff]+1, index+1]
        hashMap[num] = index


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
