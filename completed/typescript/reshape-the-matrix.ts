function matrixReshape(matrix: number[][], r: number, c: number): number[][] {
  const result: number[][] = [];
  
  const m = matrix.length; // number of rows
  const n = matrix[0].length; // number of columns

  const numberOfEntries = m * n;
  if (numberOfEntries !== r * c) {
    return matrix;
  }

  let x = 0;
  let y = 0;
  for (let y2 = 0; y2 < r; y2++) {
    const row: number[] = [];
    for (let x2 = 0; x2 < c; x2++) {
      row.push(matrix[y][x]);
      x++;
      // we don't need to worry about y going out of bounds because we return if m * n != r * c
      if (x === n) {
        y++; 
        x = 0;
      }
    }
    result.push(row);
  }  
  
  return result;
};


// test 1
console.log(matrixReshape([[1,2],[3,4]], 1, 4));

// test 2
console.log(matrixReshape([[1,2],[3,4]], 2, 4));

// completed in 9 minutes 10 seconds
export {};