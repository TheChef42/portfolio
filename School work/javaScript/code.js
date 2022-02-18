
//Excersise 1: Looping triangle
let x = "#"

for(let i = 0; i < 7; i++){
    console.log(x)
    x += "#"
}

//Exercise 2: FizzBuzz

for (let i = 1; i <= 100; i++){
    if ( i % 15 === 0){
        console.log(i + " FizzBuzz")
    } else if (i % 3 === 0){
        console.log(i + " Fizz")
    } else if (i % 5 === 0){
        console.log(i + " Buzz")
    }
}

//Excersise 3: Chess board
let board = ""
let width = 8
let height = 8
for (let i = 0; i < height; i++){
    for (let j = 0; j < width; j++) {
        if ((i + j) % 2 === 0) {
            board = board + " "
        }
        else {
            board = board + "#"
        }
    }
    board = board + "\n"
}
console.log(board)

//Excersise 4: Bean counting
let bCounter = 0
let charCounter = 0

function countBs (string){
    for (let i = 0; i < string.length; i++){
        if (string[i] === "B"){
            bCounter++
        }
    } return bCounter
}
function countChar (string, char){
    for (let i = 0; i < string.length; i++){
        if (string[i] === char){
            charCounter++
        }
    } return charCounter
}
console.log(countBs("BBC"))
console.log(countChar("kakkerlak","k"))


//CLASS 2

//Excercise 1: The sum of a range
function range(start,end, inc = 1){
    let array = []
    let j = start
    for (let i = 0; i <= (end-start)/inc ; i++){
        array[i] = j
        j += inc
    }
    return array
}
let arraySum = 0
function sum(arr){
    for (let i = 0; i < arr.length; i++){
        arraySum += arr[i]
    }
    return arraySum
}
console.log(range(1,10))
console.log(sum(range(1, 10)))

//excercise 2: Reversing array

function reverseArray (array){
    // [1,2,3]
    let j = array.length-1
    let arrayReverse = []
    for (let i = 0; i < array.length; i++){
        arrayReverse[i] = array[j--]
    }
    return arrayReverse
}
console.log(reverseArray(["A","B","C"]))



function reverseArrayInPlace(array){
    let j = array.length-1
    let arrayReverse = []
    for (let i = 0; i < array.length; i++){
        arrayReverse[i] = array[j--]
    }
    array = arrayReverse
    return array
}
let arrayValue = [1,2,3,4,5]
arrayValue = reverseArrayInPlace(arrayValue);
console.log(arrayValue);


