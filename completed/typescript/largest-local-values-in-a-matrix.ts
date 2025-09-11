function largestLocal(grid: number[][]): number[][] {
  const n = grid.length; // square grid. must be at least 3
  let maxLocal = emptyMatrix(n - 2);

  // maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
  for (let i = 0; i < n - 2; i++) {
    for (let j = 0; j < n - 2; j++) {
      maxLocal[i][j] = getLargestValueIn3x3(grid, i + 1, j + 1);
    }
  }


  return maxLocal;
};

function getLargestValueIn3x3(grid: number[][], i, j): number {
  let largest = grid[i][j];
  if (grid[i + 1][j] > largest) {
    largest = grid[i + 1][j]
  }
  if (grid[i - 1][j] > largest) {
    largest = grid[i - 1][j]
  }
  if (grid[i + 1][j + 1] > largest) {
    largest = grid[i + 1][j + 1]
  }
  if (grid[i - 1][j + 1] > largest) {
    largest = grid[i - 1][j + 1]
  }
  if (grid[i + 1][j - 1] > largest) {
    largest = grid[i + 1][j - 1]
  }
  if (grid[i - 1][j - 1] > largest) {
    largest = grid[i - 1][j - 1]
  }
  if (grid[i ][j + 1] > largest) {
    largest = grid[i][j + 1]
  }
  if (grid[i][j - 1] > largest) {
    largest = grid[i][j - 1]
  }
  return largest;
}

function emptyMatrix(n: number): number[][] {
  let emptyMatrix: number[][] = [];
  for (let i = 0; i < n; i++) {
    let row: number[] = [];
    for (let j = 0; j < n; j++) {
      row.push(0);
    }
    emptyMatrix.push(row);
  }
  return emptyMatrix;
}

// test 1
console.log(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]));

// test 2
console.log(largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]));

// finished in 13:37

export {};