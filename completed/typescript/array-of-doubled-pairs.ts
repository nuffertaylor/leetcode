// return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2
function canReorderDoubled(arr: number[]): boolean {
  // we don't actually need to bother with the reordering. just determine if possible

  arr.sort((a, b) => Math.abs(a) > Math.abs(b) ? -1 : 1);
  let map = new Map<number, number>(); // value, occurences

  for (let num of arr) {

    if (findAndRemoveMult(map, num)) {
      continue;
    }
    else {
      if (map.has(num)) {
        let numOccurences = map.get(num)!;
        map.set(num, numOccurences + 1);
      }
      else {
        map.set(num, 1);
      }
    }
  }
  if (map.size === 0) {
    return true;
  }

  return false;
};

// returns true if 2 * num found and removed
function findAndRemoveMult(map: Map<number, number>, num: number): boolean {
  const mult = 2 * num;

  if (map.has(mult)) {
    let numOccurences = map.get(mult)!;
    if (numOccurences === 1) {
      map.delete(mult);
    }
    else {
      map.set(mult, numOccurences - 1);
    }
    return true;
  }
  return false;
}


/*
i = 0
arr[1] = 2 * arr[0]
i = 1
arr[3] = 2 * arr[2]
i = 2
arr[5] = 2 * arr[4]
*/

// test case 1 - expect false
console.log(canReorderDoubled([3,1,3,6]));

// test case 2 - expect false
console.log(canReorderDoubled([2,1,2,6]));

// test case 3 - expect true
console.log(canReorderDoubled([4,-2,2,-4]));
// reordered to [-2,-4,2,4]

// test case 4 - expect true
console.log(canReorderDoubled([2,4,0,0,8,1]));

// test case 5 - expect true
console.log(canReorderDoubled([-62,86,96,-18,43,-24,-76,13,-31,-26,-88,-13,96,-44,9,-20,-42,100,-44,-24,-36,28,-32,58,-72,20,48,-36,-45,14,24,-64,-90,-44,-16,86,-33,48,26,29,-84,10,46,50,-66,-8,-38,92,-19,43,48,-38,-22,18,-32,-48,-64,-10,-22,-48]));

export {};