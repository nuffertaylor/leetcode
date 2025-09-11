function isToeplitzMatrix(matrix: number[][]): boolean {
  const numRows = matrix.length;
  const numCols = matrix[0].length;

  // we need to iterate over every x = 0 and y = 0
  for (let x = 0; x < numCols; x++) {
    if(!sameDiagonal(matrix, x, 0)) { return false; }
  }
  for (let y = 0; y < numRows; y++) {
    if(!sameDiagonal(matrix, 0, y)) { return false; }
  }

  return true;
};

function sameDiagonal(matrix: number[][], x: number, y: number): boolean {
  const numRows = matrix.length;
  const numCols = matrix[0].length;
  const value = matrix[y][x];
  while (x < numCols && y < numRows) {
    if (matrix[y][x] !== value) { return false; }
    x++;
    y++;
  }
  return true;
}


// test 1 - expect true
console.log(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]));


// test 2 - expect false
console.log(isToeplitzMatrix([[1,2],[2,2]]));

// completed in 7:33