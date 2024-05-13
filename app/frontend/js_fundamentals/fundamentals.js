////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: Closure:

// Definition: A closure is the combination of a function bundled together with references to its surrounding state (the lexical environment) where it was declared.
// In simpler terms, a closure gives you access to an outer function's scope from an inner function.

function outerFunction() {
  let outerVariable = 'I am from outer function';
  function innerFunction() {
    console.log(outerVariable); // Accessing outerVariable from the outer function's scope
  }
  return innerFunction;
}

let innerFunc = outerFunction();
innerFunc(); // Output: I am from outer function

// Explanation: In this example, innerFunction is defined inside outerFunction, and it has access to outerVariable, which is declared in the scope of outerFunction.
// Even after outerFunction has finished executing, innerFunction still has access to outerVariable, thanks to closure.

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: Hoisting:

// Definition: Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope during the compile phase before the code execution.

// Example:
console.log(x); // Output: undefined
var x = 5;

// Explanation: Even though x is logged before it's declared, JavaScript doesn't throw an error.
// Instead, it hoists the declaration to the top, making the code effectively behave like this:

var x;
console.log(x); // Output: undefined
x = 5;

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: The difference between == and ===:

// ==: Loose equality comparison. It performs type coercion before comparing two values.
// If the types are different, JavaScript will attempt to convert them to the same type before making the comparison.

// ===: Strict equality comparison. It compares both the value and the type.
// It returns true only if both the value and the type are the same.

console.log(5 == '5'); // Output: true (value comparison, type coercion)
console.log(5 === '5'); // Output: false (value and type comparison)

// Explanation: In the first example, 5 is coerced into a string and then compared with '5', resulting in true.
// In the second example, 5 and '5' have different types, so the strict comparison returns false.

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: The difference between data types [var, let, const])

// TODO: var:

// Definition: var is the oldest way to declare variables in JavaScript.
// Variables declared with var are function-scoped or globally scoped.

function example() {
  if (true) {
    var x = 5;
  }
  console.log(x); // Output: 5
}
example();

// Explanation: Variables declared with var are hoisted to the top of their containing function or global scope.
// This means you can access the variable before it's declared, and its scope is not limited by blocks (such as if statements or loops).

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: let:

// Definition: let was introduced in ES6 (ECMAScript 2015) and provides block-scoping for variables.

function example() {
  if (true) {
    let x = 5;
  }
  console.log(x); // Error: x is not defined
}
example();

// Explanation: Variables declared with let are hoisted to the top of their containing block
// but are not initialized until the declaration statement is executed.
// They are only accessible within the block where they are declared.

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: const

// Definition: const is also introduced in ES6 and is used to declare constants, whose values cannot be reassigned.

function example() {
  const x = 5;
  x = 10; // Error: Assignment to constant variable
}
example();

// Explanation: Variables declared with const must be initialized when declared and cannot be reassigned to a new value.
// However, the contents of objects or arrays declared with const can still be modified.

////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////

// TODO: In summary:

// 1. Use var for traditional variable declarations, but be cautious of its hoisting behavior and global scope.
// 2. Use let for variables that need block-scoping and may be reassigned.
// 3. Use const for variables that should not be reassigned, providing immutability, and for declaring constants.