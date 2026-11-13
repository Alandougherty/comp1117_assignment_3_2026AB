def count_filled(level):
    # Returns the number of filled cells in a carpet of the given level. Does not use a grid.
    pass  # your code here


def fill_carpet(grid, top, left, size):
    # Draws a carpet of side size into grid, in the square region with upper-left
    # corner (top, left), by setting its filled cells to "#". Returns nothing.
    pass  # your code here


def find_quadrant(top, left, size, row, col):
    # Returns 0, 1, 2 or 3: the quadrant of the square region with upper-left
    # corner (top, left) and side size that contains cell (row, col).
    pass  # your code here


def fill_tromino(grid, top, left, size, hole_row, hole_col, tile):
    # Tiles the square region with upper-left corner (top, left) and side size,
    # whose blocked cell is (hole_row, hole_col), numbering trominoes from tile.
    # Returns the next unused tile number.
    pass  # your code here


def print_grid(grid):
    # Prints one line for each row of the grid. Returns nothing.
    pass  # your code here


def main():
    # main() is yours to write, by working it out with the AI assistant.
    # Some things it will need to do:
    #   - read the pattern and the level, and for a tromino the hole position
    #   - build a starting grid of the right size, filled with the right starting value
    #   - call fill_carpet or fill_tromino once, on the whole grid
    #   - print the grid with print_grid
    #   - print the summary line: for a carpet use count_filled, for a tiling
    #     use the value fill_tromino returns
    pass


main()  # Don't change this
