function generateMatrix(n: number): number[][] {
  // instantiate an empty matrix
  let result: number[][] = emptyMatrix(n);
  let topBound = -1;
  let bottomBound = n;
  let leftBound = -1;
  let rightBound = n;
  let x = 0;
  let y = 0;
  let curVal = 1;
  while (leftBound < rightBound && topBound < bottomBound) {
    if(x >= rightBound) {break;}
    while (x < rightBound) {
      result[y][x] = curVal;
      curVal++;
      x++;
    }
    x--;
    y++;
    topBound++;

    if (y >= bottomBound) {break;}
    while (y < bottomBound) {
      result[y][x] = curVal;
      curVal++;
      y++;
    }
    y--;
    x--;
    rightBound--;

    if (x <= leftBound) {break;}
    while (x > leftBound) {
      result[y][x] = curVal;
      curVal++;
      x--;
    }
    x++;
    y--;
    bottomBound--;

    if (y<= topBound) {break;}
    while (y > topBound) {
      result[y][x] = curVal;
      curVal++;
      y--;
    }
    y++;
    x++;
    leftBound++;
  }

  return result;
};

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

console.log(generateMatrix(3));
console.log(generateMatrix(1));
console.log(generateMatrix(20));

export {};
