/**
 Do not return anything, modify matrix in-place instead.
 */
function rotateOld(matrix: number[][]): void {
  const n = matrix.length;
  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      /*
      x=0,y=0 -> x=2, y=0
      x=1,y=0 -> x=2, y=1
      x=2,y=0 -> x=2, y=2
      x=0,y=1 -> x=1, y=0
      x=1,y=1 -> x=1, y=1
      x=2,y=1 -> x=1, y=2
      */
      console.log({x, y, x2: n-1-y, y2: x});
      const x2 = n-1-y;
      const y2 = x;
      // x2 and y2 translate where the original piece needs to be moved
      // we need to do another calculate to determine what gets moved to the original spot
      // i think we can subtract an iteration if we do this? or two? cut it in half? not sure

      /*
      x=0,y=0 <- x=0, y=2
      x=1,y=0 <- x=0, y=1
      x=2,y=0 -> x=0, y=0
      */


      // or maybe we just calculate where what was in x2,y2 should end up
      // recursive? maybe we just iterate n*n times in a single for loop?
      let temp = matrix[y][x];
      console.log("swapping " + temp.toString() + " -> " + matrix[y2][x2].toString());
      matrix[y][x] = matrix[y2][x2];
      matrix[y2][x2] = temp;
    }
  }
}

function rotateOld2(matrix: number[][]): void {
  for (let y = 0; y < Math.floor(matrix.length / 2); y++) {
    const n = matrix.length - (2 * y);
    for (let x = y; x < n - 1; x++) {
      movePieces(matrix, n, x, y, matrix[y][x]);
    }
  }
  // movePieces(matrix, 0, 0, matrix[0][0]);
}

function movePieces(matrix: number[][], n: number, x: number, y: number, newValue: number, iteration = 1) {
  let x2: number;
  let y2: number;
  if (n === 2) {
    if (iteration === 1) {
      x2 = x + 1;
      y2 = y;
    } else if (iteration === 2) {
      x2 = x;
      y2 = y + 1;
    }
    else if (iteration === 3) {
      x2 = x -1;
      y2 = y;
    } else {
      x2 = x;
      y2 = y - 1;
    }
  } else {
    x2 = n-1-y;
    y2 = x;
  }
  console.log({n, x, y, x2, y2});
  const temp = matrix[y2][x2];
  matrix[y2][x2] = newValue;
  if (iteration >= 4) { return; }
  movePieces(matrix, n, x2, y2, temp, ++iteration);
}

function rotate(matrix: number[][]): void {
  const n = matrix.length;
  for (let layer = 0; layer < Math.floor(n / 2); layer++) {
    const first = layer;
    const last = n - 1 - layer;
    
    for (let i = first; i < last; i++) {
      const offset = i - first;
      
      // Save top element
      const top = matrix[first][i];
      
      // Top = Left
      matrix[first][i] = matrix[last - offset][first];
      
      // Left = Bottom
      matrix[last - offset][first] = matrix[last][last - offset];
      
      // Bottom = Right
      matrix[last][last - offset] = matrix[i][last];
      
      // Right = Top
      matrix[i][last] = top;
    }
  }
}




let testImage1 = [[1,2,3],[4,5,6],[7,8,9]];
rotate(testImage1);
console.log(testImage1);
let testImage2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]];
rotate(testImage2);
console.log(testImage2);

/*
x=1,y=1 -> x=2,y=1
x=2,y=1 -> x=2,y=2
x=2,y=2 -> x=1,y=2
x=1,y=2 -> x=1,y=1
*/