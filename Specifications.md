# A3 Recursive Patterns: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words, with the AI
assistant's help.

## Input and output types

- **Inputs:** what values does the program read, in what order, when is each
  one read, and what type is each? Which inputs are read for a carpet, and
  which for a tiling?
- **Outputs:** what does the program print, how many lines, and how is each
  cell printed? How many lines does a level-k carpet print, and a level-n
  tiling?
- **The grid:** what can a cell hold, for each pattern, and what type is
  each value? What is in every cell before drawing starts?

## The rules for each function in my own words

State each rule in your own words, not the assignment's wording pasted back.
For every boundary, write **both sides**: what happens exactly on it, and
what happens just past it. For each recursive function, say what its base
case is and why every recursive call gets closer to it.

### count_filled(level)

- **What it receives and what it returns:**
- **Base case:** which level, and what is the count? Check it against the
  level-0 carpet.
- **Recursive case:** how is the count for a level made from the count for
  the level below? Why that number? Check your rule against Example 1 and
  Example 2.

### fill_carpet(grid, top, left, size)

- **What it receives, and what it changes in the grid:** which cells may it
  change, and which must it leave alone?
- **Base case:** which size, and what happens to the grid?
- **Recursive case:** the nine smaller squares. What is each one's side, and
  where is each one's upper-left corner, counted from (top, left)? Which
  square is skipped, and what is left in its cells?
- **Offsets:** for a region that does not start at (0, 0), give one example
  of the smaller squares' corners.

### find_quadrant(top, left, size, row, col)

- **What it receives and what it returns:**
- **Rows:** which rows of the region are in the top half and which are in
  the bottom half? Give the last row of the top half and the first row of
  the bottom half.
- **Columns:** the same for the left and right halves.
- **Offsets:** give one example with a region that does not start at (0, 0),
  on both sides of a boundary.

### fill_tromino(grid, top, left, size, hole_row, hole_col, tile)

- **What it receives, what it changes in the grid and what it returns:**
  which cells may it change, and which must it leave alone?
- **Base case:** which size, what is placed, and what is returned?
- **The center cells:** for a region starting at (top, left), which four
  cells are they? Which quadrant is each one in?
- **The center tromino:** which three center cells does it cover, and which
  number does it get?
- **Each quadrant's blocked cell:** for the quadrant that holds the region's
  blocked cell, and for the other three.
- **The numbering:** the order the quadrants are tiled in, which number each
  quadrant starts from, and what the whole call returns. Check your rule
  against your trace of Example 3.

### print_grid(grid)

- **What it receives, what it prints and what it returns:** how many lines,
  how many characters per cell, and what does it leave unchanged?

### main()

- **What it does, in order:** reading input, building the starting grid,
  drawing, printing.
- **The summary line:** what is counted for each pattern, and where does the
  number come from? Why is the number of tiles one less than the value the
  first call of `fill_tromino` returns?

## Edge cases

The inputs where something special happens, and what the program must do in
each. For example: level 0 of each pattern, a hole on one of the four center
cells, a hole on the edge of the board, or a region in a recursive call that
does not start at (0, 0).