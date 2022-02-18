//optional parameters
function power(a,b = 2){
    //a**b
    // a to the power of b
    let result = 1
    for (let i = 1; i<=b; i++){
        result *= a
    }
    return result
}
console.log("2 to the power of 3 is: " + power(2,3))
console.log("2 to the power of 2 is: " + power(2))

//rest parameters
function max2 (...elements){
    //The function can be called with what ever number of parameters
    //elements is converted to an array
    let result = -Infinity
    for (let i =0; i < elements.length; i++){
        if (elements[i] > result){
            result = elements[i]
        }
    }
    return result
}
console.log(max2(2,3,8,-1,90))


let a = []
console.log(typeof a)
a.push(3)
a.push(5)
a.push(10)
console.log(a)
a.indexOf(3)
console.log(a.indexOf(12)) //-1


a = [3,5,6,2,3,7,2,3,-1,0]

//properties
a.creator = "daniel"

//Objects (not as in OOP) but as in data structure
let person1 = {
    name: "Bob",
    lastName: "Marley",
    age: 34,
}
console.log(person1.name)
person1.country = "US"
delete person1.age
//cosnole.log(person1.age) //undefined

//task calculate sum of the array
let array = [3, 6, 1, 9, 2]
let sum = 0
// for each loop
for ( let n of array){
    sum += n
}

//forEach higher order function
sum = 0
array.forEach(n => {sum += n})

array.forEach(n => console.log(n))

array.filter(n => n % 2 === 0)//[6,2]
console.log(array.filter(n => n % 2 === 0))//[6,2]
let arrayB = array.map(n => n * 2)
let arrayC = array.map(n => n ** 2)


