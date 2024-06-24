const callstack = [];
let returnValue;

callstack.push({
    'returnAddr': 'start',
    'number': 5
});


while(callstack.length > 0) {

    const { returnAddr, number } = callstack[callstack.length - 1]
    console.log(callstack)
    if (returnAddr === 'start') {
        if (number === 1) {
            returnValue = 1;
            callstack.pop();
            continue;
        } else {
            callstack[callstack.length - 1].returnAddr = 'after recursive call';
            callstack.push({
                'returnAddr': 'start',
                'number': number - 1
            })

            continue
        }
    }

    if (returnAddr === 'after recursive call') {
        returnValue *= number;

        callstack.pop();
        console.log(returnValue)
        continue
    }
}

console.log(returnValue)