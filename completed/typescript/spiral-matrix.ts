function spiralOrder(matrix: number[][]): number[] {
  let m = matrix.length;
  let n = matrix[0].length;
  let result: number[] = [];
  let topBound = -1;
  let leftBound = -1;
  let bottomBound = m; 
  let rightBound = n;
  let x = 0;
  let y = 0;

  while (topBound < bottomBound && leftBound < rightBound) {

    if (x >= rightBound) { break; }
    while (x < rightBound) {
      result.push(matrix[y][x]);
      x++;
    }
    x--;
    y++;
    topBound += 1;

    if (y >= bottomBound) { break; }
    while (y < bottomBound) {
      result.push(matrix[y][x]);
      y++;
    }
    y--;
    x--;
    rightBound -= 1;

    if (x <= leftBound) { break; }
    while (x > leftBound) {
      result.push(matrix[y][x]);
      x--;
    }
    x++;
    y--;
    bottomBound -=1;

    if (y <= topBound) { break; }
    while (y > topBound) {
      result.push(matrix[y][x]);
      y--;
    }
    y++;
    x++;
    leftBound += 1;
  }
  return result;
};

const test1 = [[1,2,3],[4,5,6],[7,8,9]];
const test2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]];

const result1 = spiralOrder(test1);
console.log(result1);
const result2 = spiralOrder(test2);
console.log(result2);