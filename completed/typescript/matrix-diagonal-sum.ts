function diagonalSum(mat: number[][]): number {
    // the matrix is square
    const n = mat.length;
    let answer = 0;
    for (let i = 0; i < n; i++) {
        answer += mat[i][i];
        // if both indexes are the same, we're at the middle, and we only count the middle once
        if (i === n - 1 -i) { continue; }
        answer += mat[i][n - 1 -i];
    }
    return answer;
};

// test 1 - expect 25
console.log(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]));

// test 2  - expect 8
console.log(diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]));

// test 3 - expect 5
console.log(diagonalSum([[5]]));

// test 4 - expect 55
console.log(diagonalSum([
  [7,3,1,9],
  [3,4,6,9],
  [6,9,6,6],
  [9,5,8,5]
]));
