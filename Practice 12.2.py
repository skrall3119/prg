def find_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + find_sum(nums[1:])


def main():
    nums = [2, 7, 43, 15, 76, 22]
    print(find_sum(nums))

main()
