function numPairsDivisibleBy60(time: number[]): number {
  let answer = 0;
  let map = new Map<number, number>(); // remainder and number times seen

  for (let i = 0; i < time.length; i++) {
    const modResult = time[i] % 60;
    let timesSeen = 1;
    if (map.has(modResult)) {
      timesSeen = map.get(modResult)! + 1;
    }
    // modding by 60 handles if modResult is zero. otherwise the number will be unchanged by the mod
    if (map.has((60 - modResult) % 60)) {
      answer += map.get((60 - modResult) % 60)!;
    }
    map.set(modResult, timesSeen);
  }


  return answer;
};

// test 1
console.log(numPairsDivisibleBy60([30,20,150,100,40]));

// test 2
console.log(numPairsDivisibleBy60([60,60,60]));

// original solution - it works but it's too slow
function numPairsDivisibleBy60On2Solution(time: number[]): number {
  let answer = 0;

  for (let i = 0; i < time.length; i++) {
    for (let j = i; j < time.length; j++) {
      if (i === j) {
        continue;
      }

      if ((time[i] +  time[j]) % 60 === 0) {
        answer++;
      }
    }
  }

  return answer;
};


export {};