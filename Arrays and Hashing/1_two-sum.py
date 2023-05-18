nums = [3, 3]
target = 6


def solution():
    hashMap = {}
    for i in range(len(nums)):
        # if difference in hashmap, return the two indexes and the indexes are different
        if (target - nums[i]) in hashMap:
            if hashMap[target - nums[i]] != i:
                return [hashMap[target - nums[i]], i]
                # value : key in hashmap
        hashMap[nums[i]] = i

print(solution())
