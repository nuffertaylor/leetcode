function findDiagonalOrder(matrix: number[][]): number[] {
  const result: number[] = [];
  const m = matrix.length;
  const n = matrix[0].length;
  console.log({m, n});
  let x = 0;
  let y = 0;
  while (y < m || x < n) {
    
    // traverse northeast
    while (y > -1 && x < n) {
      console.log({x, y, direction: "northeast"});
      result.push(matrix[y][x]);
      x++;
      y--;
    }

    y++; // set y to 0
    if (x === n) { // this means corner piece
      x--;
      y++;
    }
    

    // check if we're done
    if (y >= m || x >= n) { break; }


    // traverse southwest
    while (x > -1 && y < m) {
      console.log({x, y, direction: "southwest"});
      result.push(matrix[y][x]);
      x--;
      y++;
    }
    if (y === m) { // corner piece
      y--;
      x++;
    }
    x++;
  }
  return result;
};

const diagonal1 = [[1,2,3],[4,5,6],[7,8,9]];
console.log(findDiagonalOrder(diagonal1));

const diagonal2 = [[1,2],[3,4]];
console.log(findDiagonalOrder(diagonal2));

const diagonal3 = [[2,3]];
console.log(findDiagonalOrder(diagonal3));

const diagonal4 = [[3],[2]];
console.log(findDiagonalOrder(diagonal4));

const diagonal5 = [[1]];
console.log(findDiagonalOrder(diagonal5));


/**
 * 0, 0
 * 1, -1
 * 
 */

export {};
