def directions_reduction(dirs: list) -> list:
    """
    Given a list of cardinal directions (North,South,East,West), return the
    directions but simplified as going north at one point and then going south
    right after would be redundant.
    For example:
    dirs = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    directions_reduction(dirs)
    >>> ["WEST"]
    This is because the first North and South cancel each other. Then the East
    and West cancel and then the South at the third index meets North at the
    second last index and cancel out leaving only west.
    See also:
    https://www.codewars.com/kata/550f22f4d758534c1100025a
    """
    DIR_LIST = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }
    if not dirs:
        return []
    final_dirs = [dirs[0]]  # this question can be easily solved with a stack.
    for dir in dirs[1:]:
        if final_dirs and dir == DIR_LIST[final_dirs[-1]]:
            final_dirs.pop()
        else:
            final_dirs.append(dir)
    return final_dirs


def main():
    dirs = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(directions_reduction(dirs))


if __name__ == '__main__':
    main()
