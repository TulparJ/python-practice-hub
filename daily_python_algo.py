# Daily Python Algorithm
# Topic: Two Pointers + List

def move_zeros(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


def sum_of_evens(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print("After moving zeros:", move_zeros(arr))

    nums = [1, 2, 3, 4, 5, 6]
    print("Sum of evens:", sum_of_evens(nums))
