function islandPerimeter(grid: number[][]): number {
  const numRows = grid.length;
  const numCols = grid[0].length;
  let perimeter = 0;

  for (let y = 0; y < numRows; y++) {
    for (let x = 0; x < numCols; x++) { 
      // if val === 0 it's water, continue
      if (grid[y][x] === 0) { continue; }

      // if we're here, we're on land.
      // check four perimeter tiles - if it's out of bounds or water, add 1 to perimeter
      // check left
      if (x - 1 < 0 || grid[y][x - 1] === 0) {
        perimeter++;
      }
      // check right
      if (x + 1 >= numCols || grid[y][x + 1] === 0) {
        perimeter++;
      }
      // check up
      if (y - 1 < 0 || grid[y - 1][x] === 0) {
        perimeter++;
      }
      // check down
      if (y + 1 >= numRows || grid[y + 1][x] === 0) {
        perimeter++;
      }

    }
  }

  return perimeter;
};

// time to complete: 5:55