```markdown
# JavaScript Objects, Scopes, Closures

This repository contains JavaScript code for handling objects, scopes, and closures. The project includes several tasks, each addressing specific concepts in JavaScript programming.

## Table of Contents

1. [Rectangle #0](#rectangle-0)
2. [Rectangle #1](#rectangle-1)
3. [Rectangle #2](#rectangle-2)
4. [Rectangle #3](#rectangle-3)
5. [Rectangle #4](#rectangle-4)
6. [Square #0](#square-0)
7. [Square #1](#square-1)
8. [Occurrences](#occurrences)
9. [Esrever](#esrever)
10. [Log me](#log-me)
11. [Number conversion](#number-conversion)

## Tasks

### Rectangle #0

Write an empty class Rectangle that defines a rectangle.

```javascript
// Example usage
const Rectangle = require('./0-rectangle');
const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
```

### Rectangle #1

Write a class Rectangle that defines a rectangle.

```javascript
// Example usage
const Rectangle = require('./1-rectangle');
const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);
```

### Rectangle #2

Write a class Rectangle that defines a rectangle.

```javascript
// Example usage
const Rectangle = require('./2-rectangle');
const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);
```

### Rectangle #3

Write a class Rectangle that defines a rectangle and includes a `print` method.

```javascript
// Example usage
const Rectangle = require('./3-rectangle');
const r1 = new Rectangle(2, 3);
r1.print();
```

### Rectangle #4

Write a class Rectangle that defines a rectangle with additional methods.

```javascript
// Example usage
const Rectangle = require('./4-rectangle');
const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();
console.log('Double:');
r1.double();
r1.print();
console.log('Rotate:');
r1.rotate();
r1.print();
```

### Square #0

Write a class Square that defines a square and inherits from Rectangle.

```javascript
// Example usage
const Square = require('./5-square');
const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
```

### Square #1

Write a class Square that defines a square and inherits from Square.

```javascript
// Example usage
const Square = require('./6-square');
const s1 = new Square(4);
s1.charPrint();
s1.charPrint('C');
```

### Occurrences

Write a function that returns the number of occurrences in a list.

```javascript
// Example usage
const nbOccurrences = require('./7-occurrences').nbOccurrences;
console.log(nbOccurrences([1, 2, 3, 4, 5, 6], 3));
```

### Esrever

Write a function that returns the reversed version of a list.

```javascript
// Example usage
const esrever = require('./8-esrever').esrever;
console.log(esrever([1, 2, 3, 4, 5]));
```

### Log me

Write a function that prints the number of arguments already printed and the new argument value.

```javascript
// Example usage
const logMe = require('./9-logme').logMe;
logMe("Hello");
logMe("Best");
logMe("School");
```

### Number conversion

Write a function that converts a number from base 10 to another base passed as an argument.

```javascript
// Example usage
const converter = require('./10-converter').converter;
let myConverter = converter(10);
console.log(myConverter(2));
```

## Setup and Execution

1. Install Node.js (version 14.x):

   ```bash
   curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. Install `semistandard`:

   ```bash
   sudo npm install semistandard --global
   ```

3. Execute the JavaScript files:

   ```bash
   ./filename.js
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Please adjust the placeholders like `filename.js` and update the sections as per your project structure and content.
