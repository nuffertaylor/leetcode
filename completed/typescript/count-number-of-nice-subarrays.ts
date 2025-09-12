function numberOfSubarrays(nums: number[], k: number): number {
  return atMostK(nums, k) - atMostK(nums, k -1);
};

function atMostK(nums: number[], k: number): number {
  let leftPointer = 0;
  let rightPointer = 0;
  let oddCount = 0;
  let atMostKCount = 0;
  
  while (rightPointer < nums.length) {
    if (isOdd(nums[rightPointer])) {
      oddCount++;
    }
    
    while (oddCount > k) {
      if (isOdd(nums[leftPointer])) {
        oddCount--;
      }
      leftPointer++;
    }
    
    // when we reach this line, we KNOW that this array (and all its possible subarrays)
    // contain at most "K" odds. from max windowsize (rightPointer - leftPointer) to windowSize of 1.
    // so we can add all those into our array. This is the trick of "at most". were we counting exact, we couldn't do this.
    // we can take advantage of this neat property by running k and k-1 and subtracting the two results for our ultimate answer.
    // there's no way people just figure this stuff out in thirty minutes, they have to be exposed to the idea already. crazy
    atMostKCount += rightPointer - leftPointer + 1;
    rightPointer++;
  }
  
  return atMostKCount;
}

function isOdd(num: number): boolean {
  return num % 2 === 1;
}

function numberOfSubarraysOn3(nums: number[], k: number): number {
  let numberOfSubarrays = 0;
  // sliding window - k gives us our minimum window size
  for (let windowSize = k; windowSize <= nums.length; windowSize++) {
    let numOdd = 0;
    for (let startingPos = 0; startingPos <= nums.length - windowSize; startingPos++) {
      // calculate the whole window value on the first iteration
      if (startingPos === 0) {
        for (let j = startingPos; j < startingPos + windowSize; j++) {
          if (isOdd(nums[j])) {
            numOdd++;
          }
        }
      }
      else {
        // subtract if the now exterior value was odd
        if (isOdd(nums[startingPos - 1])) {
          numOdd--;
        }
        // add if the new value is odd
        if (isOdd(nums[startingPos - 1 + windowSize])) {
          numOdd++;
        }
      }
      
      if (numOdd === k) {
        // nice subarray found
        numberOfSubarrays++;
      }
    }

  }
  return numberOfSubarrays;
};

// test 1 - expect 2
console.log(numberOfSubarrays([1,1,2,1,1], 3));

// test 2 - expect 0
console.log(numberOfSubarrays([2,4,6], 1));

// test 3 - expect 16
console.log(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2));