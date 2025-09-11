function transpose(matrix: number[][]): number[][] {
  let result: number[][] = [];
  let numCols = matrix.length;
  let numRows = matrix[0].length;
  // create an empty matrix where the original numRows is now the numCols
  for (let y = 0; y < numRows; y++) {
    let row: number[] = [];
    for (let x = 0; x < numCols; x++) {
      row.push(0);
    }
    result.push(row)
  }

  // iterate through the original matrix and place the values in the new
  for (let y = 0; y < numCols; y++) {
    for (let x = 0; x < numRows; x++) {
      result[x][y] = matrix[y][x]
    }
  }

  return result;
    
};


/*
0,0 -> 0,0
1,0 -> 0,1
2,0 -> 0
...
*/

// test 1
console.log(transpose([[1,2,3],[4,5,6],[7,8,9]]));

// test2
console.log(transpose([[1,2,3],[4,5,6]]));

// time: 6:38

export {};
