function imageSmoother(img: number[][]): number[][] {
  let result: number[][] = []
  const rowLength = img.length;
  const colLength = img[0].length;
  for (let row = 0; row < rowLength; row++) {
    let avgRow: number[] = [];
    for (let col = 0; col < colLength; col++) {
      let sum = img[row][col];
      let numCounted = 1;
      if (col - 1 >= 0) {
        sum += img[row][col-1];
        numCounted++;
      }
      if (col - 1 >= 0 && row - 1 >= 0) {
        sum += img[row - 1][col-1];
        numCounted++;
      }
      if (row -1 >= 0) {
        sum += img[row -1][col];
        numCounted++;
      }
      if (col + 1 < colLength) {
        sum += img[row][col+1];
        numCounted++;
      }
      if (col + 1 < colLength && row - 1 >= 0) {
        sum += img[row - 1][col+1];
        numCounted++;
      }
      if (col - 1 >= 0 && row + 1 < rowLength) {
        sum += img[row + 1][col - 1];
        numCounted++;
      }
      if (col + 1 < colLength && row + 1 < rowLength) {
        sum += img[row + 1][col+1];
        numCounted++;
      }
      if (row + 1 < rowLength) {
        sum += img[row + 1][col];
        numCounted++;
      }
      avgRow.push(Math.floor(sum / numCounted));
    }
    result.push(avgRow);
  }
  return result;
    
};