const demNums = [1, 2, 3, 4, 5];

console.log(demNums);

const sum = demNums.reduce( (tempSum, currentVal) => 
{
    console.log('tempSum: ' + tempSum );
    console.log('currentVal: ' + currentVal);
    return tempSum += currentVal;
});

console.log(sum);

const objs = [];

const a = { a: 'a'};
const b = { b: 'b' };
const c = { c: 'c' };

objs.push(a,b,c);

const abc = objs.reduce( (tempSum, currentVal) =>
{
    return {...tempSum, ...currentVal};
}
);
console.log(objs);
console.log(abc);