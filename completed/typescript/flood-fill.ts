function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
  
  const startingColor = image[sr][sc];
  if (startingColor === color) { return image; }
  colorPixel(image, sr, sc, startingColor, color);
  return image;
    
};

function colorPixel(image: number[][], y: number, x: number, startingColor: number, newColor: number){
  const numRows = image.length;
  const numCols = image[0].length;
  const id = y.toString() + '-' + x.toString();
  if (y < 0 || y >= numRows || x < 0 || x >= numCols) {
    return;
  }
  if (image[y][x] !== startingColor) {
    return;
  }
  image[y][x] = newColor;
  colorPixel(image, y - 1, x, startingColor, newColor);
  colorPixel(image, y, x - 1, startingColor, newColor);
  colorPixel(image, y + 1, x, startingColor, newColor);
  colorPixel(image, y, x + 1, startingColor, newColor);
}


// test 1
console.log(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2));

// test 2
console.log(floodFill([[0,0,0],[0,0,0]], 0, 0, 0));

export {};