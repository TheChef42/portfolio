
//Excersise 1: Looping triangle
let x = "#"

for(let i = 0; i < 7; i++){
    console.log(x)
    x = x + "#"
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

//Excercise 5: The sum of a range
let array = []

function range(start,end, inc){
    if (inc === undefined){
        inc = 1
    }
    console.log(inc)
    let j = start
    for (let i = 0; i <= end-start ; i += inc){
        array[i] = j++
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
console.log(range(5,2,-1)) //TODO: implement the increment to work
console.log(sum(range(1, 10)))

