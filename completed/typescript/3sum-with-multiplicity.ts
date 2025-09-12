/*
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target

As the answer can be very large, return it modulo 10^9 + 7.

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300

*/


function threeSumMulti(arr: number[], target: number): number {
  let answer = 0;
  const MOD = 1000000007;

  arr.sort((a,b) => a - b);

  for (let i = 0; i < arr.length - 2; i++) {
    let j = i + 1;
    let k = arr.length - 1;
    const adjustedTarget = target - arr[i];
    while (j < k) {
      const curResult = arr[j] + arr[k];
      // this means we've got a duplicate, so just keep moving in
      if (curResult === adjustedTarget) {
        // now count duplicates
        if (arr[j] === arr[k]) {
          // Special case: j and k point to same value
          const count = k - j + 1;
          answer = (answer + (count * (count - 1)) / 2) % MOD;
          break; // No more valid pairs possible
        } else {
          // Count duplicates by finding boundaries
          let leftCount = 1;
          let rightCount = 1;
          
          // Skip all duplicates of arr[j]
          while (j + leftCount <= k && arr[j + leftCount] === arr[j]) {
              leftCount++;
          }
          
          // Skip all duplicates of arr[k] 
          while (k - rightCount >= j && arr[k - rightCount] === arr[k]) {
              rightCount++;
          }
          
          answer = (answer + leftCount * rightCount) % MOD;
          
          // Jump past all duplicates in one step
          j += leftCount;
          k -= rightCount;
        }
      }
      else if (curResult < adjustedTarget) {
        // move j (left) up
        j++;
      } else {
        // move k (right) down until new value found
        k--;
      }
    }
  }

  return answer;
};

// works but too slow
function threeSumMultiON3(arr: number[], target: number): number {
  let answer = 0;
  const MOD = 1000000007;

  for (let i = 0; i < arr.length - 2; i++) {
    for (let j = i + 1; j < arr.length - 1; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        if (arr[i] + arr[j] + arr[k] === target) {
          answer = (answer + 1) % MOD;
        }
      }
    }
  }

  return answer;
};

// test 1 - expect 20
console.log(threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8));

// test 2 - expect 12
console.log(threeSumMulti([1,1,2,2,2,2], 5));

// test 3 - expect 1
console.log(threeSumMulti([2,1,3], 6));

export {};