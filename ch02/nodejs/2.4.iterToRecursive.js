console.log('Code in a loop');

let i = 0;

while (i < 5) {
    console.log(i, 'Hello');
    i++
}

const hello = i => {
    if (i === undefined) i = 0;
    console.log(i, 'Hello');

    i + 1 < 5 && hello(i + 1)
}

console.log('Code in Recursive function');
hello()