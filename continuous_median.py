import heapq as hq


def cont_median(nums):
    """
    Given an array of numbers, for i, 0 through len(nums), print the median
    thus far, i.e from 0 to i.
    Use 2 buckets, one to store the lower half of numbers and one to store upper
    half. The former is a maxheap and the latter is a minheap.
    """
    if not nums:
        return None
    medians = []
    lower, upper = [], []

    for num in nums:
        hq.heappush(lower, num)
        if len(lower) > len(upper) + 1:
            smallest_upper = hq.heappop(lower)
            hq.heappush(upper, -smallest_upper)
        if len(lower) == len(upper):
            median = (lower[0]-upper[0])/2
        else:
            median = lower[0]
        medians.append(median)

    return medians


assert not cont_median(None)
assert not cont_median([])
assert cont_median([2, 5]) == [2, 3.5]
assert cont_median([3, 3, 3, 3]) == [3, 3, 3, 3]
assert cont_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
