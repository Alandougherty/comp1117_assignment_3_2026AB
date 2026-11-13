# A3 Recursive Patterns Assignment

Before starting, read [AI-use.md](AI-use.md) for the required AI workflow, conversation exports and academic integrity rules.

## Overview

Write a program that draws one of two recursive patterns on a square grid, then prints one summary line:

- **Pattern 1, Sierpinski carpet:** a square with holes in it, where every part looks like a smaller copy of the whole.
- **Pattern 2, L-tromino tiling:** a square board with one missing cell, covered completely by numbered L-shaped tiles.

Here is what two short runs look like. The value after each prompt is what the user types.

```
Pattern (1 carpet, 2 tromino): 1
Level: 1
  #  #  #
  #  .  #
  #  #  #
Filled: 8
```

```
Pattern (1 carpet, 2 tromino): 2
Level: 1
Hole row: 1
Hole column: 1
  1  1
  1  X
Tiles: 1
```

Both drawings come from short recursive functions. Each recursive call works on a smaller square somewhere inside the big grid. To get them right you must be able to follow the program call by call: which square each call is working on, where that square's upper-left corner is, and, for the tiling, which cell in it is already covered. That is what this assignment teaches and what it checks.

## Rows, columns and regions

A grid is a list of rows, and each row is a list of cells. `grid[r][c]` is the cell in row `r`, column `c`. Row 0 is the top row and column 0 is the left column.

```
          col 0  col 1  col 2  col 3
row 0      (0,0)  (0,1)  (0,2)  (0,3)
row 1      (1,0)  (1,1)  (1,2)  (1,3)
row 2      (2,0)  (2,1)  (2,2)  (2,3)
row 3      (3,0)  (3,1)  (3,2)  (3,3)
```

A **square region** is given by its upper-left corner `(top, left)` and its side length `size`. It contains rows `top` to `top + size - 1` and columns `left` to `left + size - 1`. For example, the region with `top = 2`, `left = 2`, `size = 2` is the four cells (2,2), (2,3), (3,2), (3,3) in the bottom-right corner above.

---

## Pattern 1: Sierpinski carpet

### What it looks like

Filled cells are `#` and empty cells are `.`.

```
Level 0 (side 1)     Level 1 (side 3)     Level 2 (side 9)
  #                    #  #  #              #  #  #  #  #  #  #  #  #
                       #  .  #              #  .  #  #  .  #  #  .  #
                       #  #  #              #  #  #  #  #  #  #  #  #
                                            #  #  #  .  .  .  #  #  #
                                            #  .  #  .  .  .  #  .  #
                                            #  #  #  .  .  .  #  #  #
                                            #  #  #  #  #  #  #  #  #
                                            #  .  #  #  .  #  #  .  #
                                            #  #  #  #  #  #  #  #  #
```

### The rule

- A carpet of side 1 is a single filled cell.
- A bigger carpet is split into a 3 by 3 arrangement of squares, each of side `size // 3`. The **middle** square is left empty. Each of the other eight squares is a smaller carpet.

The **level** is how many times the square is split. A level-k carpet has side 3 to the power k: 1, 3, 9, 27.

The summary line is `Filled: ` followed by the number of `#` cells.

### Example 1: carpet, level 2

```
Pattern (1 carpet, 2 tromino): 1
Level: 2
  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #
  #  #  #  .  .  .  #  #  #
  #  .  #  .  .  .  #  .  #
  #  #  #  .  .  .  #  #  #
  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #
Filled: 64
```

The 9 by 9 square is split into nine 3 by 3 squares. The middle one, rows 3 to 5 and columns 3 to 5, is skipped, so it stays `.`. Each of the other eight is a level-1 carpet, which leaves its own middle cell empty: for example (1, 1), (1, 4) and (7, 7). Of the 81 cells, 9 are in the big middle square and 8 are small middles, so 64 are filled.

### Example 2: carpet, level 3 (the largest input)

```
Pattern (1 carpet, 2 tromino): 1
Level: 3
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #
  #  .  #  .  .  .  #  .  #  #  .  #  .  .  .  #  .  #  #  .  #  .  .  .  #  .  #
  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #  .  .  .  .  .  .  .  .  .  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #
  #  #  #  .  .  .  #  #  #  .  .  .  .  .  .  .  .  .  #  #  #  .  .  .  #  #  #
  #  .  #  .  .  .  #  .  #  .  .  .  .  .  .  .  .  .  #  .  #  .  .  .  #  .  #
  #  #  #  .  .  .  #  #  #  .  .  .  .  .  .  .  .  .  #  #  #  .  .  .  #  #  #
  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #  .  .  .  .  .  .  .  .  .  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #
  #  .  #  .  .  .  #  .  #  #  .  #  .  .  .  #  .  #  #  .  #  .  .  .  #  .  #
  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #  #  #  #  .  .  .  #  #  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #  #  .  #
  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
Filled: 512
```

The 27 by 27 square is nine copies of Example 1, except that the middle copy (rows 9 to 17, columns 9 to 17) is empty. So 8 × 64 = 512 cells are filled.

---

## Pattern 2: L-tromino tiling

### What it looks like

A **tromino** is an L-shaped tile that covers three cells of a 2 by 2 square. The board has side 2 to the power n, where n is the level: 1, 2, 4, 8 or 16. One cell of the board is the **hole**, printed as `X`. Every other cell is covered by exactly one tromino. Tiles are numbered from 1, and the three cells with the same number form one tromino.

```
Level 1, hole (1, 1)     Level 2, hole (0, 0)
  1  1                     X  2  3  3
  1  X                     2  2  1  3
                           4  1  1  5
                           4  4  5  5
```

### The rule

Every region the program works on has exactly one **blocked cell**, which is a cell that is already covered. For the whole board, the blocked cell is the hole. To tile a region whose blocked cell is `(hole_row, hole_col)`, numbering tiles from `tile`:

1. **Base case.** If `size` is 1, the only cell is the blocked cell. Nothing is placed, and the next unused number is still `tile`.
2. **Split into quadrants.** Split the region into four quadrants of side `size // 2`, numbered like this:

   ```
     0 | 1
    ---+---
     2 | 3
   ```

   A cell is in the bottom half if its row is `top + size // 2` or more. It is in the right half if its column is `left + size // 2` or more.
3. **Place the center tromino.** The four **center cells** are the four cells that touch the middle of the region, one in each quadrant. One quadrant contains the blocked cell. Place tromino number `tile` on the other three center cells.
4. **Recurse.** Each quadrant now has exactly one blocked cell: either the original blocked cell, or the center cell just covered. Tile quadrants 0, 1, 2 and 3 **in that order**. Quadrant 0 starts numbering from `tile + 1`. Each later quadrant starts from the next unused number returned by the quadrant before it.

The summary line is `Tiles: ` followed by the number of trominoes placed.

### Example 3: tromino, level 2, hole in a corner

```
Pattern (1 carpet, 2 tromino): 2
Level: 2
Hole row: 0
Hole column: 0
  X  2  3  3
  2  2  1  3
  4  1  1  5
  4  4  5  5
Tiles: 5
```

Step by step:

- The center cells are (1, 1), (1, 2), (2, 1) and (2, 2). The hole (0, 0) is in quadrant 0, so tromino 1 goes on (1, 2), (2, 1) and (2, 2).
- Quadrant 0 (rows 0–1, columns 0–1) has the hole as its blocked cell. It is tiled starting from 2 and places tile 2, so it returns 3.
- Quadrant 1 has (1, 2) as its blocked cell and places tile 3. Quadrant 2 places tile 4 and quadrant 3 places tile 5.
- The top-level call returns 6, so 6 − 1 = 5 tiles were placed.

### Example 4: tromino, level 2, hole on a center cell

```
Pattern (1 carpet, 2 tromino): 2
Level: 2
Hole row: 1
Hole column: 2
  2  2  3  3
  2  1  X  3
  4  1  1  5
  4  4  5  5
Tiles: 5
```

Work through this one yourself before you start your specification. Which quadrant contains the hole? Why does tromino 1 cover (1, 1), (2, 1) and (2, 2), and not (1, 2)? What is the blocked cell of each quadrant when it is tiled?

### Example 5: tromino, level 4 (the largest input)

```
Pattern (1 carpet, 2 tromino): 2
Level: 4
Hole row: 5
Hole column: 10
  4  4  5  5  9  9 10 10 25 25 26 26 30 30 31 31
  4  3  3  5  9  8  8 10 25 24 24 26 30 29 29 31
  6  3  7  7 11 11  8 12 27 24 28 28 32 32 29 33
  6  6  7  2  2 11 12 12 27 27 28 23 23 32 33 33
 14 14 15  2 19 19 20 20 35 35 36 36 23 40 41 41
 14 13 15 15 19 18 18 20 35 34  X 36 40 40 39 41
 16 13 13 17 21 18 22 22 37 34 34 38 42 39 39 43
 16 16 17 17 21 21 22  1 37 37 38 38 42 42 43 43
 46 46 47 47 51 51 52  1  1 67 68 68 72 72 73 73
 46 45 45 47 51 50 52 52 67 67 66 68 72 71 71 73
 48 45 49 49 53 50 50 54 69 66 66 70 74 74 71 75
 48 48 49 44 53 53 54 54 69 69 70 70 65 74 75 75
 56 56 57 44 44 61 62 62 77 77 78 65 65 82 83 83
 56 55 57 57 61 61 60 62 77 76 78 78 82 82 81 83
 58 55 55 59 63 60 60 64 79 76 76 80 84 81 81 85
 58 58 59 59 63 63 64 64 79 79 80 80 84 84 85 85
Tiles: 85
```

How to read it:

- The hole (5, 10) is in quadrant 1, the top-right 8 by 8, so tromino 1 sits on the center cells of the other three quadrants: (7, 7), (8, 7) and (8, 8).
- Each 8 by 8 quadrant uses 21 tiles. Quadrant 0 uses 2 to 22, quadrant 1 uses 23 to 43, quadrant 2 uses 44 to 64 and quadrant 3 uses 65 to 85.
- Inside quadrant 1 (rows 0–7, columns 8–15), the hole is in its bottom-left 4 by 4, so tromino 23 goes on (3, 11), (3, 12) and (4, 12).
- Inside quadrant 2 (rows 8–15, columns 0–7), the blocked cell is (8, 7), which tromino 1 covered. It is in that quadrant's top-right 4 by 4, so tromino 44 goes on (11, 3), (12, 3) and (12, 4).
- A number wider than one digit takes the same three characters as any other cell, so the columns line up.

---

## Input and output format

Your program is tested automatically, so it must follow this format exactly.

| Value | Prompt |
|---|---|
| Pattern | `Pattern (1 carpet, 2 tromino): ` |
| Level | `Level: ` |
| Hole row (tromino only) | `Hole row: ` |
| Hole column (tromino only) | `Hole column: ` |

Input is one whole number per line. The pattern is 1 or 2. For a carpet, the level is 0 to 3. For a tromino, the level is 0 to 4, and the hole row and hole column are each from 0 to the board side minus 1.

After input ends, print **one line for every row of the grid**, top to bottom, then **exactly one summary line** (`Filled: <int>` or `Tiles: <int>`), and nothing else.

Each grid line is the row's cells, left to right, each printed with `"{:>3}".format(cell)` and joined with nothing in between. Every cell therefore takes exactly three characters, e.g.,
```
  #
  .
  X
  7
 21
```

## How the program is organised

`Pattern.py` already contains the outline of the program in six parts, one for each function. Each `def` line, with its name and parameters, is given, together with a comment saying what the function returns, and you write the body. For `main()`, the template gives the `def` line and some comments suggesting what `main()` needs to do. They are suggestions, not steps to copy.

**Do not rename the functions or change their parameters. Use only the six functions supplied in `Pattern.py`. Do not define additional functions, including helper functions or functions inside another function.** Parts 1, 2 and 4 **must be recursive**: each must call itself. `test.py` checks this.

| Part | Function | What it does | Used by |
|---|---|---|---|
| 1 | `count_filled(level)` | Returns the number of filled cells in a carpet of the given level. Does not use a grid. Recursive. | `main()`, for the carpet's summary line |
| 2 | `fill_carpet(grid, top, left, size)` | Draws a carpet of side `size` into the square region of `grid` with upper-left corner `(top, left)`, by setting its filled cells to `"#"`. It does not change empty cells or any cell outside the region. Returns nothing. Recursive. | `main()` |
| 3 | `find_quadrant(top, left, size, row, col)` | Returns 0, 1, 2 or 3: the quadrant of the region with upper-left corner `(top, left)` and side `size` that contains cell `(row, col)`. Not recursive. | `fill_tromino` |
| 4 | `fill_tromino(grid, top, left, size, hole_row, hole_col, tile)` | Tiles the region whose blocked cell is `(hole_row, hole_col)`, following the rule in Pattern 2, writing tile numbers (ints) into `grid` starting from `tile`. It does not change the blocked cell or any cell outside the region. Returns the next unused tile number. Recursive. | `main()` |
| 5 | `print_grid(grid)` | Prints one line for each row of the grid, in the format above. Returns nothing and does not change the grid. | `main()` |
| 6 | `main()` | Reads the input, builds the starting grid, calls part 2 or part 4 once on the whole grid, calls part 5, then prints the summary line. | (the program) |

Keep the three jobs separate:

- **Returning a value.** `count_filled`, `find_quadrant` and `fill_tromino` return a value to their caller. They do not print it.
- **Changing the grid.** `fill_carpet` and `fill_tromino` change the grid they are given. `main()` sees those changes, because the grid it passed in is the same list.
- **Printing.** Only `print_grid` and `main()` print. All input happens in `main()`.

**The starting grid.** For a carpet, `main()` starts with a grid in which every cell is `"."`. For a tiling, it starts with a grid in which every cell is the int `0`, then sets the hole to `"X"`. In a correct tiling, no `0` is left.

**The summary line comes from the recursion.** For a carpet, `main()` prints the value of `count_filled`. For a tiling, the call on the whole board numbers tiles from 1, and the number of tiles placed is one less than the value that call returns. Do not count cells in the grid to make the summary line. Your drawing and your count should still agree, and checking that they do is a good test. If they disagree, one of them is wrong.

Leave the last line, `main()  # Don't change this`, where it is.

## Constraints

Use only what we have covered in lectures 1 to 8:

- the basic types int, float, str and bool; `input()` and `print()`; `int()`, `float()` and `str()`;
- operators, including `//`, `%` and `**`;
- conditionals `if`, `elif` and `else`; `while` and `for` loops, `range`, `break` and `continue`;
- lists, tuples, sets and dictionaries as taught in lecture 4 (for lists: indexing, `append`, `len`, `in` and looping over a list), and lists of lists, indexed and assigned as `grid[r][c]`;
- the six supplied functions with parameters and `return`, and recursion; no additional function definitions;
- basic f-strings such as `f"{x}"`, without format codes.

Do not use string methods (including `join`), slicing, list methods other than `append`, list comprehensions, `sum`, `round`, `sorted`, `try` and `except`, `import`, or anything else not yet covered.

The `"{:>3}".format(...)` shown in Tips is supplied. Use it exactly as shown.

All code must use only the features above. You must be able to read, trace and explain every line of your program.

## Tips

### Printing a row

Each cell must take exactly three characters, whether it is `"#"`, `"X"`, `7` or `21`. This handles both strings and ints:

```python
"{:>3}".format(cell)
```

Build each row's line by adding these pieces to a string, one cell at a time, then print the line.

### Keep the offsets

A region is not always at the top-left of the grid. Inside a recursive call, the cells of the region are counted from `(top, left)`, not from `(0, 0)`.

For example, in Example 5, quadrant 3 of the whole board is the region with `top = 8`, `left = 8`, `size = 8`. Its center cells are (11, 11), (11, 12), (12, 11) and (12, 12), not (3, 3) to (4, 4). Its blocked cell is (8, 8), which tromino 1 covered, so tromino 65 goes on (11, 12), (12, 11) and (12, 12). Check this against the output.

### Trace before you code

Before writing `fill_tromino`, write out every call for Example 3 as a list. For each call, note its region, its blocked cell, the tile number it starts from and the number it returns. Then do the same for Example 4. If your list matches the output, you understand the rule well enough to write the code.

### Recursion depth

Each recursive call works on a square a third or a half the size of its caller's, so the deepest chain of calls is only as long as the level. You will not reach Python's recursion limit.

## Testing your program

**The target: every decision in the program is tested at least once in each direction, and every boundary is tested from both sides.** A boundary is tested from both sides when you have one case exactly on it and one case just past it. For example, a cell in the last row of the top half of a region, and a cell in the first row of the bottom half.

There are two kinds of test, and both go in `tests.txt`.

**Function checks** test one part on its own. Each is one line: a call to `count_filled` or `find_quadrant`, then `==`, then the value you expect. For example:

```
count_filled(2) == 64
find_quadrant(2, 4, 4, 3, 6) == 1
```

Write up to 12. Your checks should include the base case of `count_filled`, both sides of the row boundary and of the column boundary in `find_quadrant`, and at least one region that does not start at (0, 0).

**Program cases** test the whole program: the input, one value per line, then the expected output. Separate cases with a blank line. Write up to 8. Keep the spaces at the start of each grid line. `fill_carpet`, `fill_tromino` and `print_grid` change or print the grid instead of returning one value, so they are tested through program cases. Your cases should cover:

- both patterns, and level 0 of each;
- a carpet of level 2 or more;
- a hole in each of the four quadrants of the board;
- a hole on one of the four center cells;
- a hole on the edge of the board that is not a corner.

One case can cover more than one of these.

Put the function checks first, under a line `# Function checks`, then the program cases under a line `# Program cases`. `tests.txt` in the template shows the layout.

**Predict before you run.** For each test, work out the expected value from the rules first, then run it. A test only proves something if you predicted the result. An expected value copied from your program's output does not catch bugs.

`python test.py` checks that the recursive parts are recursive, checks `fill_carpet`, `fill_tromino` and `print_grid` directly on small grids, runs all five worked examples and the level-0 cases, and runs all of your own tests.

You may assume all input is valid, as described above. You do not need to test invalid input.
