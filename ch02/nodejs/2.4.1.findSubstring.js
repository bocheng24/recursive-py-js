const findSubstringIter = (needle, haystack) => {
    for (let i = 0; i < haystack.length; i++) {
        if (haystack.slice(i, i + needle.length) === needle) return i
    }

    return -1
}

console.log(findSubstringIter('cat', 'My cat zophie'))

const findSubstringRecur = (needle, haystack, i = 0) => {
    if (i > haystack.length) return -1;

    if (haystack.slice(i, needle.length + i) === needle) return i;

    return findSubstringRecur(needle, haystack, i + 1);
}

console.log(findSubstringRecur('cat', 'My cat zophie'))