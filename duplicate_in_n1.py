class FindDuplicate:
    """
    Given an array of n+1 numbers from 1 to n, find the number that is a
    duplicate.
    i.e FindDuplicate([1,2,3,4,2,5])
    >>> 2
    This is structured as a class to show the 2 approaches, one using linked
    lists and Floyd's algorithm and the other using a hash map.
    """

    def __init__(self, arr):
        self.arr = arr
        ans1 = self.floyd_llist()
        print(f"Floyd's Algorithm: {ans1}")
        ans2 = self.hash_solve()
        print(f"Hash map: {ans2}")

    def floyd_llist(self):
        """
        This approach uses 2 pointers, a fast one and a slow one to traverse the
        numbers. Each number in the array can be considered as the pointer to
        the next node and having a value of None.
        """
        nums = self.arr
        fast, slow = nums[0], nums[0]
        while True:
            fast, slow = nums[nums[fast]], nums[slow]
            if fast == slow:
                break
        p1, p2 = nums[0], fast
        while p1 != p2:
            p1, p2 = nums[p1], nums[p2]
        return p1

    def hash_solve(self):
        """
        Maintain a hash map of all the nums we have seen and then if we see
        a num twice then return it.
        """
        nums = self.arr
        seen = {}
        for num in nums:
            if num in seen:
                return num
            seen[num] = True


def main():
    obj = FindDuplicate([1, 2, 3, 4, 5, 2])


if __name__ == '__main__':
    main()
