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
