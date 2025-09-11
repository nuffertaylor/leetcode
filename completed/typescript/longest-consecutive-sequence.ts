function longestConsecutive(nums: number[]): number {
    let longest = 0;
    let set = new Set<number>(nums);

    for (const num of set) {
      // check if num - 1 is in map - if not, this is the start of a sequence
      if (!set.has(num - 1)) {
        const sequenceLength = getSequenceLength(set, num);
        if (sequenceLength > longest) {
          longest = sequenceLength;
        }
      }
    }

    return longest;
};

function getSequenceLength(map: Set<number>, startingIndex: number): number {
  let i = startingIndex;
  let length = 0;
  while (map.has(i)) {
    length++;
    i++;
  }
  return length;
}

// ignore this method - solving a problem that I could easily avoid
function findStartingIndex(map: Set<number>, startingIndex: number): number {
  let i = startingIndex;
  while (map.has(i)) {
    i--;
  }
  i++;
  return i;
}


// test 1
console.log(longestConsecutive([100,4,200,1,3,2]));

// test 2
console.log(longestConsecutive([0,3,7,2,5,8,4,6,0,1]));

// test 3
console.log(longestConsecutive([1,0,1,2]));

export {};