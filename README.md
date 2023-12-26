# Lab 1: Variables, Booleans and user errors
This lab will deal with improving your understanding of variables, booleans and user errors.

`tax.py` will be used for task 1 and task 2

`correctme.py` will be used for task 3

### *__Preface 1: Semantic Error & Type Errors__*

__Syntax errors__ are similar to grammatical errors, where programming languages will have its own rules that will define the way you code.
So if the rules are violated, it will result in an error, specifically a __Syntax error__.

Syntax errors can be the following:
* Missing parenthesis
* Wrong indentation
* Structure issues
* Misuse of operators

__Type Errors__ are usually related to using an unintended data type in an operation,
i.e:
* Trying to add a str type to an int type `"Hello" + 1`
* Putting a string to an input that only accepts integer `int("Pain")`
* Putting a float to an int only input. `int("1.0")`

Both of these types of errors will appear in the console, so it is relatively easier to fix compared to a logic or semantic error.



### __Task 1__: 
`tax.py` is a program that calculates the income tax of a user but it reeks of syntax errors. Help fix the program so that it will run without any errors.

For now, ensure that the code runs properly as the output may be incorrect!
>_Hint: Run the program and check the console_


### __Task 2.1: if, elif and else__
In `tax.py`, You may have notice that when you put an invalid data type, it causes a type error, How would you use if statments (elif and else if you need to) to fix this problem?

To Do:
* Income Variable
   - Check for int type
   - Ensure that the value is more than 0
* Tax Variable
   - Check for either int or float _(if you wanna use percentage or decimals)_
   - The tax is in between 0 and 100 percent
* If either income or tax has an invalid value, print `Invalid input`


> _Hint: Use type() to check the input type_


### __Task 2.2: Loops__
Now that you have checked the input, but now you want to force the user to correct their input by repeating the request for the input.

How would you use a while or a for loop to do this?

>_Hint Don't forget about continue and break!_


### *__Preface 2: Semantic Errors__*

Logic Errors are any errors related incorrect logic inside the code, i.e:
* Any logic that causes an unintended result.
- A user wants to check if x is more than y but puts `x < y`
   - Uses the wrong conditioanl operator
* Operation that were not done in order

Semantic errors are errors in the meaning of statements (usually variables), i.e:
* A user uses the wrong variable

Semantic and Logic Errors are harder to deal with, as python will not output any error signatures (the console errors), as python can only check for type and syntax errors. This means that the output or program will run irregardless of the semantic or logic errors that exists inside the code.

Therefore these errors requires the user to fully understand how their program work and being able back track until you see these errors.

>__This is why comments are very important, as they can define the meaning and logic of a code without having to parse the code itself.__

Example
```
number = 2
if(number % 2 == 1):
   print('is even')
else:
   print('is odd')
```

This code is incorrect, but you really don't know where it went wrong.

Adding comments...
```
if(number % 2 == 1): # Take the modulus, if remainder is 0, it will be odd
   print('is even')
else:
   print('is odd')
```
The comment has describes the wrong logic that the code had but in a readable form, `number % 2`, if it is equal to 1 it is an odd number and 0 if it is an even number.

When the codebase of your program grows, Always comment, as your comment will preserve the logic that you used at the time. So always comments especially complicated code.

### __Task 3: It smells pretty bad in here...__
This code has all flavours of errors, and it is really disgusting, please fix it for me.

Correct all errors and change comments if there are logical or semantic errors.

Assume the comments are correct and the coded logic is not `:)`

To test your code click the flask on the left and select _test* names and restart vscode if the test does not appear there

>_Hint: Understand what the code is doing before fixing logic and semantic errors_ 