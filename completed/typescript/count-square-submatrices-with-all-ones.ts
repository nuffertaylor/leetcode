function countSquares(matrix: number[][]): number {
  let result = 0;
  const numRows = matrix.length;
  const numCols = matrix[0].length;
  // largest possible square matrix is the smaller of these
  const largestPossible = Math.min(numCols, numRows);

  // iterate through each square size
  for (let squareSize = 1; squareSize <= largestPossible; squareSize++) {
    let debugCounter = 0;
    for (let y = 0; y <= numRows - squareSize; y++) {
      for (let x = 0; x <= numCols - squareSize; x++) {
        if (squareHasAllOnes(matrix, x, y, squareSize)) {
          result++;
          debugCounter++;
        }
      }
    }
    console.log({squareSize, debugCounter});
  }

  return result;
};

function squareHasAllOnes(matrix: number[][], x: number, y: number, squareSize: number): boolean {
  for (let row = y; row < y + squareSize; row++) {
    for (let col = x; col < x + squareSize; col++) {
      if (matrix[row][col] === 0) {
        return false;
      }
    }
  }
  return true;
}

// test 1 - expect 15
console.log(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]));

// test 2 - expect 7
console.log(countSquares([[1,0,1],[1,1,0],[1,1,0]]));

// test 3 - expect 20
console.log(countSquares([[1,1,0,0,1],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,0,1],[0,0,1,0,1]]));

export {};