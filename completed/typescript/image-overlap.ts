function largestOverlap(img1: number[][], img2: number[][]): number {
  const n = img1.length; // square matrixes, both have same n

  let bestScore = 0;

  // there are a finite number of translations we can perform
  // the most we can move in either x/y direction is (+/-) n-1
  for (let dy = -n-1; dy < n; dy++) {
    for (let dx = -n-1; dx < n; dx++) {
      let newScore = calculateScore(img1, img2, dy, dx);
      if (newScore > bestScore) {
        bestScore = newScore;
      }
    }
  }

  return bestScore;
};

function calculateScore(img1: number[][], img2: number[][], dy: number, dx: number): number {
  let points = 0;
  const n = img1.length; // square matrixes, both have same n
  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      if (y-dy >= n || x-dx >= n || y-dy < 0 || x-dx < 0) {
        continue;
      }

      if (img1[y][x] === 1 && img2[y-dy][x-dx] === 1) {
        points++;
      }
    }
  }
  return points;
}

// test 1
console.log(largestOverlap(
  [[1,1,0],[0,1,0],[0,1,0]],
  [[0,0,0],[0,1,1],[0,0,1]]
));

// test 2
console.log(largestOverlap(
  [[1]],
  [[1]]
));

console.log(largestOverlap(
  [[0]],
  [[0]]
));

// this took exactly 45 minutes.
// though the first 25 minutes were wasted on the shifting logic I implemented below

/*
dx = -2
matrix1[y][0] compared to martix2[y][0--2]
matrix1[y][1] compared to martix2[y][1--2] <-- if a given index is out of bounds, we know it's a zero

*/


















// all these shift functions modify in place
// these are worthless, ignore

function shiftMatrixRight(matrix: number[][]): number[][] {
  const lastIndex = matrix.length - 1;
  for (let y = lastIndex; y > -1; y--) {
    for (let x = lastIndex; x > -1; x--) {
      if (x === 0) {
        matrix[y][x] = 0;
      } else {
        matrix[y][x] = matrix[y][x-1];
      }
    }
  }
  return matrix;
}

// test shiftMatrixRight
// console.log(shiftMatrixRight([[1,1,0],[1,0,1],[0,1,0]]));

function shiftMatrixLeft(matrix: number[][]): number[][] {
  const lastIndex = matrix.length - 1;
  for (let y = 0; y <= lastIndex; y++) {
    for (let x = 0; x <= lastIndex; x++) {
      if (x === lastIndex) {
        matrix[y][x] = 0;
      } else {
        matrix[y][x] = matrix[y][x+1];
      }
    }
  }
  return matrix;
}

// test shiftMatrixLeft
// console.log(shiftMatrixLeft([[1,1,0],[1,0,1],[0,1,0]]));

function shiftMatrixDown(matrix: number[][]): number[][] {
  const lastIndex = matrix.length - 1;
  for (let x = lastIndex; x > -1; x--) {
    for (let y = lastIndex; y > -1; y--) {
      if (y === 0) {
        matrix[y][x] = 0;
      } else {
        matrix[y][x] = matrix[y-1][x];
      }
    }
  }
  return matrix;
}

// test shiftMatrixDown
// console.log(shiftMatrixDown([[1,1,0],[1,0,1],[0,1,0]]));

function shiftMatrixUp(matrix: number[][]): number[][] {
  const n = matrix.length;
  for (let y = 0; y < n - 1; y++) {
    for (let x = 0; x < n; x++) {
      matrix[y][x] = matrix[y + 1][x];
    }
  }
  // zero row
  for (let x = 0; x < n; x++) {
    matrix[n-1][x] = 5;
  }
  return matrix;
}

// test shiftMatrixUp
// console.log(shiftMatrixUp([[1,1,0],[1,0,1],[0,1,0]]));

