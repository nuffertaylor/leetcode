function longestPalindrome(words: string[]): number {
  let answer = 0;
  let map = new Map<string, number>(); // str, numOccurences

  // we can assume every item in words will be two char long
  for (const word of words) {
    const reversed = word[1] + word[0];
    if (map.has(reversed)) {
      console.log(word + reversed);
      let numOccurences = map.get(reversed)!;
      if (numOccurences === 1) {
        map.delete(reversed);
      } else {
        map.set(reversed, numOccurences - 1);
      }
      answer += 4;
    }
    else {
      if (map.has(word)) {
        let numOccurences = map.get(word)!;
        map.set(word, numOccurences + 1);
      }
      else {
        map.set(word, 1);
      }
    }
  }

  // check if there are any leftover palidrome words to be placed in the middle (can only be done once)
  for (const word of map.keys()) {
    if (word[0] === word[1]) {
      answer+= 2;
      break;
    }
  }


  return answer;
};

// time to finish: 21 min


// test 1 - expect 6
console.log(longestPalindrome(["lc","cl","gg"]));

// test 2 - expect 8
console.log(longestPalindrome(["ab","ty","yt","lc","cl","ab"]));

// test 3 - expect 2
console.log(longestPalindrome(["cc","ll","xx"]));

// test 4 - expect 26
console.log(longestPalindrome(["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]));

// test 5 - expect 30
console.log(longestPalindrome(["lx","xl","cl","cc","cx","ll","lx","xc","xc","cx","ll","xx","xc","xx","xx","lx","lx","xx","cc","xx"]));

export {};