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
    min_heap, max_heap = [], []

    for num in nums:
        hq.heappush(min_heap, num)
        if len(min_heap) > len(max_heap) + 1:
            smallest_max_heap = hq.heappop(min_heap)
            hq.heappush(max_heap, -smallest_max_heap)
        if len(min_heap) == len(max_heap):
            median = (min_heap[0]-max_heap[0])/2  # average but max_heap has -ve
        else:
            median = min_heap[0]  # since min heap is always equal or larger.
        medians.append(median)

    return medians


assert not cont_median(None)
assert not cont_median([])
assert cont_median([2, 5]) == [2, 3.5]
assert cont_median([3, 3, 3, 3]) == [3, 3, 3, 3]
assert cont_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
