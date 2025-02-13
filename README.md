# <span style="color: #ce1403; font-weight: Bold">Python</span>

Python is a `high-level`, versatile programming language known for its simplicity and readability, making it a favorite among beginners and professionals alike. Created by `Guido van Rossum` and first released in `1991`, Python supports multiple programming paradigms, including `procedural`, `object-oriented`, and `functional` programming. Its extensive standard library and active community provide tools for diverse applications, from web development and data analysis to artificial intelligence and scientific computing. Python’s concise syntax enables developers to write code efficiently, enhancing productivity while maintaining clarity. As a result, it has become a cornerstone in modern software development, data science, and machine learning.

# <span style="color: #ebce14;">A Python Programing full Crash cours in Kadoos EDU</span>

# <span style="color: #03ce14;">Getting started</span>

- <span style="color: Red;">About Python</span>

  - The World's Fastest growing programming language
  - Most Popular among Software Engi., Data Analysts, Math, Science, Net Engi., and Kids
  - Google, Facebook, Spotify, DropBox, and etc. use Python
  - Python is simple
  - ![](Images/1.png)
  -
  - Python is a multipurpose Language
  -
  - ![](Images/2.png)
  -
  - Most Desirable language
  - ![](Images/3.png)
  -
  - Python2 and Python3
  -

- <span style="color: Red;">Installation Instruction</span>

  - Install python (Download and install)
  - Note "check `Add python 3 to PATH`"
  - check your installation on windows Command prompt

- <span style="color: Red;">Python Interpreter</span>

  - Check some code in it
  - Check errors

- <span style="color: Red;">Editors</span>

  - Text Editors `Notepad` , `Atom`, `Sublime`
  - IDEs `Pycharm`,
  - Use `VSCode` for this class

- <span style="color: Red;">Create Your First Python File</span>

  - Open your folder in VSCode And create .py file
  - Talk about extensions
  - First Built-in Function `Print()`
  - Execute first code in terminal

- <span style="color: Red;">Turn VSCode to a Powerful IDE Using Extensions</span>

  - Install python Extension in VSCode
  - ![](Images/4.png)
  - Install Linter to find Potential errors
  - Select right Python for your Project

- <span style="color: Red;">PyLint</span>

  - Check PyLint Functionality
  - Check errors in problems panel
  - Talk about command pallet `Shift + ctrl + p`
  - Choose Right linter - `pylint`

- <span style="color: Red;">Python Enhancement Proposal</span>

  - PEPs In google
  - Talk about PEP8
  - Talk about Python code formats
  - Format Document In command pallet
  - `autopep8` Installation
  - Talk about some developer mistake in formatting code
  - Turn auto format on save in `Code>Preferences>sittings`
  - Search for FormatOnSave and turn it on

- <span style="color: Red;">Running Python Code</span>

  - Install Code Runner
  - Running Code by Key or `ctrl+alt+n`

- <span style="color: Red;">Python Implementation</span>

  - ![](Images/4.5.png)
  - Cpython and python interpreter
  - Other Implementations of python Jython, IronPython, PyPy
  - These implementations help us to use other languages code in our python code

- <span style="color: Red;">Execution of Python code</span>

  - `Cpython` and python interpreter
  -
  - C Translation to machine code
  - ![](Images/5.png)
  - Codes are different in Mac and Windows based on compilers
  -
  - ![](Images/6.png)
  -
  - `Java` Solve the problem
  -
  - ![](Images/7.png)
  -
  - Python use it
  - ![](Images/8.png)
  -
  - `Jython Workflow
  -
  - ![](Images/9.png)

<hr>

### <span style="color: #03ce14;">Primitive Types</span>

- <span style="color: Red;">Variables</span>

  - Core concept of storing data by programming languages
  - Three different built-in primitive types in python
  - Numbers (100, 4.9,...), Booleans (True/False), Strings ("Your Name")
  - All your variables' name should be descriptive and meaningful
  - Python is a case sensitive programming language
  - All letters in your variable's name should be in lower case
  - We cannot use a number at the beginning of the name of a variable
  - Set a space before and after your equal sign
  - Use Underline between separate word

- <span style="color: Red;">Strings</span>

  - Surround your text with `"` or `'`
  - For multiline text (long text) we use `"""`
  - Talk about built-in function for String type
  - `len()`
  - Calling Functions concept by using `()`
  - Indexing concept in Python for strings and `[]`
  - End of the string usi ng `[-1]`
  - Slicing strings Using `[:]` (check all options)
  - Using backslash `\` to scape special characters (e.g. `\"`, `\'`, `\\`, `\n`)
  - Concatenate strings using `+`
  - Formatted Strings using `f` and `{}`

- <span style="color: Red;">String Methods</span>

  - Talk about methods and OOP (Dot Notation)
  - `upper()`, `lower()`, and `title()` methods
  - Notice that the original string is not changed after using those methods
  - Use `strip()` method for users input strings (`lstrip()` and `rstrip()`)
  - Use `find()` method to find a special character or series of characters (return an index or `-1`)
  - Use `replace("1", "2")` to change one or sequence of characters
  - `in` and `not in` expressions for checking the existence of something
  - Different between the `find()` and `in` expression is in return value (`index`, `True/False`)

- <span style="color: Red;">Numbers</span>

  - There is three different number type in python
  - `Integer`, `float`, and `complex` (a + bi)
  - Talk about comments `#`

- <span style="color: Red;">Standard Arithmetic Operations</span>

  - `+`, `-`, `*`, `/`, `//`, `%` and `**`
  - Augmented Operations `+=`, `-=`, `*=`, `/=`

- <span style="color: Red;">Built-in Functions for Numbers</span>

  - `round()`
  - `abs()`
  - Talk about modules (`math`) and import the library and check `.` notation
  - Check `math` modules in Google (`Python 3 math modules`)

- <span style="color: Red;">Type Conversion</span>
  - Use `input()` function to get data from user
  - Check the error and explain the reason
  - Built-in Conversion methods in python
  - `int()`, `float`, `bool`, and `str`
  - talk about `type()` method
  - All falsy values in python: `""`, `0`, `False`, `[]`, `{}`, `()`, and `None`
  - Check in interpreter

<hr>

### <span style="color: #03ce14;">Control Flow </span>

- <span style="color: Red;">Comparison Operators</span>

  - `>`, `<`, `<=` `>=`, `==`, `!=`
  - Talk about the differences f `=` and `==`
  - An integer and a string value save differentially in memory `10 == "10"` is wrong
  - every character has unique numeric representation (`unicode`), so `"bag" == "BAG"` is wrong
  - Use `ord()` function to show differences

- <span style="color: Red;">Conditional statement</span>

  - `if` statement (always terminate it with `:`)
  - Explain about code block and indentation on a simple example `temperature`
  - Simple example (`if statement : pass`)
  - Talk about indentation and code block with example of three print under an if statement
  - Explain codes out of if block
  - With `elif` statement we can add more condition to our code
  - If all our conditions are not True we use `else` statement to execute last condition (lots of `elif` and one `else`)
  - nested if statements

- <span style="color: Red;">Ternary Operator</span>

  - Turn 5 line code to one
  - `X = elem1 if rule1 else elem2`
  - message = "OK" if time >= 10 else "Not OK"

- <span style="color: Red;">Logical Operator</span>

  - `and`, `or`, and `not`
  - `and` operator return True if both conditions are True
  - `or` operator return True if one of conditions is True
  - `not` changes the value of a boolean variable
  - Don't use `==` for check a boolean variable
  - Separate conditions logical comparison to make accurate comparison
  - Avoid short circuit in the process of working with logical operators
  - Chain logical operators instead of using theme in word format
  - Use `18 <= age < 40` instead of `age >= 18 and age < 40`

- <span style="color: Red;">For Loops</span>

  - When we need to repeat a task for number of times `For loop' can do it (Ex: print something for 10 times)
  - Show the result of range function using print at first
  - Talk about counter(`number`) and `range` function (step) and add `... * "."`

- <span style="color: Red;">For...else</span>

  - `else` execute when a loop completely was executed and aBreak didn't happen

- <span style="color: Red;">Nested Loops</span>

  - Talk about Outer and inner Loops
  - Explain how exactly python interpreter execute nested loops

- <span style="color: Red;">Iterables</span>

  - Use type for range() function to explain
  - Range is complex type
  - Iterable of strings or lists
  - You can create a `iterable` object and use it in `For` loop

- <span style="color: Red;">While Loop</span>

  - We use `While` loop to repeat something as log as a condition is true
  - Explain While loop in python interpreter as real world example
  - Simulate Terminal using a while loop as extra example
  - Check case sensitive characteristic of python
  - Check a poor way of condition for while loop (A `and` B)

- <span style="color: Red;">Infinite Loop</span>

  - Infinite loop is a loop that runs forever
  - You should always have a way to `break` the infinite loop
  - it can cause crash for your system

- <span style="color: Red;">Exercise</span>
  - A python code that shows even number between 1 to 10 and count them

<hr>

### <span style="color: #03ce14;">Functions</span>

- <span style="color: Red;">How to Define a Function</span>

  - In programming we should break our code in small, reusable, and more maintainable chunks of code
  - Use `def` keyword (short form of define) to declare your function
  - Make sure your function names are meaningful and descriptive
  - Name conventions should apply for functions naming
  - After definition of a function for using it you should call it (Two line break - pep8)

- <span style="color: Red;">Arguments</span>

  - Talk about differences between `print` and our function
  - Define parameters in our function
  - A `parameter` is the input that you define for your function but an `argument` is actual value for a given parameter

- <span style="color: Red;">Types of Functions</span>

  - There is two type of Functions
  - A: A function that perform a task (`say_hello()`, `print()`)
  - B: A function that calculate and return a value (`round()`)
  - We use `return` statement to return a value from a function
  - Write `say_hello()` function with `return` and get it in variable
  - Talk about print a function that doesn't return any value
  - By default all functions return a `None` value (indicator of absence a value) till you place a return statement inside it

- <span style="color: Red;">Keyword Arguments</span>

  - Talk about temporary argument that python create for us when we pass a function to another function
  - Make your code more readable when you are calling your function by using keyword arguments
  - By adding a default value to a parameter we can make it optional
  - (`Important`) All optional parameters should come after the required parameters

- <span style="color: Red;">xargs</span>

  - To pass a list of parameters to function we can use `xargs`
  - It returns a `Tuple`
  - By adding an asterisk (`*`) at beginning of a parameter it can take a list of values
  - Talk about tuples and lists by return xargs argument

- <span style="color: Red;">xxargs</span>

  - To pass a series of keyword arguments to a function we can use `xxargs` parameter
  - By adding double asterisk (`**`) at beginning of a parameter it can take a list of key value peers
  - It returns a `Dictionary`
  - By using `bracket` notation we can get the values of a dictionary

- <span style="color: Red;">Scope</span>

  - It's Impossible to call a variable which defined inside a function, outside of it
  - A local variable only works inside the scope also parameters
  - Thc completely equal variable in two different function is completely separate
  - When a function called, python interpreter allocate a memory to it's variables and release it at end function's execution (`Garbage Collector`)
  - On the other side we have global variables which can be used anywhere in code
  - Global use memory for long time and you should not use them often
  - A global variable's value never change even inside a function
  - By using `global` keyword we can reference a local variable to a global one
  - Using global variables is not recommended because it can has a side effect in other functions

- <span style="color: Red;">Debugging</span>

  - Start debugging process inside `Debug panel` (F5)
  - Choose current file and `VSCode` create a `json` file for your project (`don't touch it`)
  - By using `bullet points` (F9) you can define break point for debug process
  - By pushing F10 key you can step forward in process
  - By pushing F11 key you can step into a sub-process like a function
  - To stop debugger with `shift+F5`
  - Debugger stops wherever you placed a bullet point
  - To step out of a function or loop you can press `shift+F11`

- <span style="color: Red;">VSCode Tricks</span>
  - In each line you can move to the end by pushing `end` key
  - In each line you can move to the beginning by pushing `home` key
  - By pressing `Ctrl+end` cursor move to the end of the file
  - By pressing `Ctrl+home` cursor move to the beginning of the file
  - By pressing `alt` plus `arrow keys` (top-down) you can move a line of code top or down
  - To duplicate a line press `alt+shift+down` keys
  - By pressing `Ctrl+/` you can change a line to comment
  - By typing some characters of a variable you can place it by pushing enter

<hr>

### <span style="color: #03ce14;">Data Structure</span>

- <span style="color: Red;">Lists</span>

  - We use `[]` in Python to define a list or sequence of objects
  - Talk about different type of list (list of numbers, list of lists like a matrix)
  - `zeros = [0] * 100` / Use `+` to concatenate or `*` to multiply
  - In python lists items doesn't need to be a same type
  - Use `list()` method to convert objects to list like `list(range(20))` or `list("Hello")`
  - `list()` function takes an `iterable` as argument
  - Use `len()` method to get length of a list

- <span style="color: Red;">Accessing Items</span>

  - By using Bracket notation we can have access to a list items
  - Talk about similar thing with regard strings
  - To modifying items use assign element. Change list Items like `my_list[1] = "B"`
  - Use [:] to get a range of items in list
  - By slicing a list, original list doesn't change
  - In the list slicing we can place another `:` after second index and the number that comes after it is the step of choosing Items (`[::2]` return every other elements)
  - Use [::-1] to reverse a list ex: `my_list(range(20))[::-1]`

- <span style="color: Red;">Unpacking Lists</span>

  - We can Unpack a list into multiple variables
  - `first, second, third = my_list`
  - Left and right side must be equal in number (Check for error)
  - Unpacking a large list : `first, second, *other = my_list` or `first, *other, last = my_list`
  - Using a asterisk `*` before a variable change it to a list and it is a packing in Python

- <span style="color: Red;">Lopping over Lists</span>

  - Use for to loop over a list
  - `enumerate()` function unpack list item to key and value
  - This function convert each item of list to a `tuple`
  - Use for loop to show `kays` and `values` in a list (By indexing and unpacking)
  - Talk about for loop and represent items in each iteration

- <span style="color: Red;">Adding or Removing Items</span>

  - Use `append()` method to add an item to end of a list
  - Use `insert()` method to add item at specific position in list
  - Use `pop()` method to remove an item from end of a list (remove with index)
  - Use `.remove(item)` to remove first occurrence of that item - remove without index
  - To remove all`"b"` in the list you should loop over list
  - Use `del lst[0]` to delete an item or `del lst[:3]` to delete a range of items. This is difference between `pop()` and `del`
  - Use `clear()` method to delete all items in the list

- <span style="color: Red;">Finding Items</span>

  - To find index of an item use `.index(item)` method
  - `index()` method causes `ValueError` when try to find an item that is not exist
  - Use `if .. in ..` statement to prevent this error
  - Use `count(item)` method to check existence of an item

- <span style="color: Red;">Sorting Lists</span>

  - Use `sort()` method to sort a list
  - Use `reverse` parameter as keyword argument to sort your list in descending format `lst.sort(key, reverse=True|False)`
  - To sort a list without changing the original list use `sorted(lst)` function ex: `sorted(my_list, reverse=True)`
  - To sort a list of unordered items (complex) like list of tuples we should write a function and use sort item and pass all items to this function
  - We can <span style="color: Red;">pass</span> a function not `call` to the `sort()` method as `key` parameter
  - You need to specify `key` parameter as keyword argument

- <span style="color: Red;">Lambda Functions</span>

  - A lambda function is a `one-line` `anonymous` function that we can pass to other functions
  - Lambda function structure: <span style="color: #ef34dd;">lambda parameter: expression</span>

- <span style="color: Red;">Map Function</span>

  - To transform (map) a part of all items in a list of complex items we need to apply a for loop an get the desire value from it
  - By using `map` function we can do it in a shorter and elegant way
  - It returns a map object (an iterable) and by type conversion we can transform it to a list object (`list()`)
  - We can loop over it or convert it to a list

- <span style="color: Red;">Filter Function</span>

  - When we need to apply a filter on a list and get a specific values `filter` function is the way
  - `Filter` function takes a lambda function as first parameter and select items based on the lambda function criteria
  - It returns an iterable object (`filter object`)
  - We can loop over it or convert it to a list

- <span style="color: Red;">List Comprehension</span>

  - List comprehension in python: <span style="color: Orange;"> [Expression for item in items]</span>
  - It's completely the same with the `mapping process` and `filtering process`

- <span style="color: Red;">Zip Function</span>

  - To merge two or more list in a single list of tuples we can use `zip` function
  - It returns a `Zip object` which is a iterable
  - Add a string to zip function and see the result

- <span style="color: Red;">Stacks</span>

  - A `LIFO` data structure (`example of Books`)
  - Website's pages visiting hierarchy is good simple fore Stack
  - We can use `.append()`, `.pop()` methods for simulating stack and `stc[-1]` and `not []' to check it
  - `[]` is another falsy value

- <span style="color: Red;">Queues</span>

  - A `FIFO` data structure
  - We use `deque` for optimize Using queue
  - Use `.popleft()` and `deque` class to manage your queue in optimize way

- <span style="color: Red;">Tuples</span>

  - Tuple is a read only list and we use `()` to define it
  - if we remove () Python Assume it as tuple like `1, or 1,2`
  - Empty parentheses indicate a tuple
  - We can multiple a number into a tuple or concatenate tuples
  - We can convert a list or any iterable into a tuple using `tuple()` function
  - `Indexing`, `packing`, and `unpacking` rules are usable related to tuples
  - We cannot mutate tuples and assign a value of tuple to a new value
  - We use a tuple when we need a sequence of objects that should be untouched throughout the execution of program

- <span style="color: Red;">Swapping Variables</span>

  - `x, y = Y, x` (Exercise)
  - This clause works as unpacking in tuples `x, y = (11, 10)`
  - Explain about tuples without `()`

- <span style="color: Red;">Arrays</span>

  - When we deal with a large sequence of numbers we should use Array
  - Array take less memory and work a little bit faster
  - In 99% of the cases we use lists but sometimes when we experience a <span style="color: yellow;">performance problem</span>, arrays can solve it
  - For the using array we should import it
  - Search for `python 3 Typecode` in Google
  - `Array(typecode, iterable)`
  - We can all methods of lists about arrays
  - All members in array should be the same type (test assigning float to integer array)

- <span style="color: Red;">Sets</span>

  - Set is a unordered collection of data without duplicates
  - By converting a List to set by using `set()` function we can remove all duplicates
  - We use `{}` to define sets
  - Like lists we can add to (`.add()` method) and remove items (`.remove()` method) from a set
  - `len()` function return the size of a set
  - Shining usage of sets is in `mathematics`
  - Use `|` operator to make union of two sets
  - Use `&` operator to get the intersection of two sets
  - Use `-` operator to get the differences between two sets
  - Use `^` operator to get the symmetric differences between two sets
  - Sets items not in sequence and we cannot access them by index
  - We can existence of a value by using `if .. in` statement

- <span style="color: Red;">Dictionaries</span>

  - Dictionary is a `key value pe` collection of data
  - In dictionary <span style="color: #5599ff;">keys</span> can only be an `integer` or a `string` and <span style="color: #5599ff;">value</span> can be kind of `anything`
  - Index in dictionaries is the key items (`my_dict["key1"]`)
  - We can define a dictionary by using `dict()` function
  - Always check for existence of a key before use or call it by `if ... in` statement or `.get()` method
  - To delete an item use `del` statement
  - For loop on a dictionary return keys in each iteration
  - By using `.items()` we can get dictionary's item in the shape of tuple in each iteration
  - Practice on writing list comprehension (Change it to a set)
  - We can use Comprehension for sets and dictionaries
  - `Val = {x : x*2 for x in range(5)}`

- <span style="color: Red;">Generator Expression</span>

  - Comprehension on tuples return a `Generator Objects`
  - Generator object like list is a iterable but generate value in each iteration
  - Generators don't store all values in memory
  - `len()` function doesn't work on generator object

- <span style="color: Red;">Unpacking Operator</span>

  - We can print items of a list by using `[*numbers]` statement
  - We can use unpacking operators to combine lists
  - Also unpack operator work abut dictionaries by using `**`
  - If we have multiple item in our dictionaries, the last item will be used

<hr>

### <span style="color: #03ce14;">Exceptions</span>

- <span style="color: Red;">Exceptions</span>

  - An exception is a kind of error that terminate the execution of the program
  - Usually these errors happens because of programmers mistakes or bad data that we get from the user or resources not being available
  - Like `index error` in lists or getting `None` value is input from user
  - By using a `try exception` block we can handel potential errors
  - If you don't handel exceptions properly your program will crash
  - All codes after try block will be executed after accruing an exception
  - By adding an `else` statement to your try block, if no exception is thrown else block code wil be executed
  - It's possible that different kind of exceptions happens and it's important to handel them
  - We can define `multiple exception` block for our try clause or put all potential exceptions in one exception block (`inside a parentheses`)
  - If one of our try block exceptions be executed other exceptions will be ignored
  - We should release the external resources like files or network connections after finishing our job with them
  - To prevent duplicate or release external resources, we need to define a `finally` at the end of your try block
  - Also we can use `with` statement in the case of working with external resources
  - This resources will be released when the program doesn't need the anymore
  - If any object in python supports <span style="color: Red;">context management protocol</span>, we should open them by `with` statement
  - These files has two `__enter__` and `__exit__` magic method
  - We can open multiple file with one `with` statement
  - We can `raise` an exception by using this statement
  - Check Python 3 built-in exceptions In Google
  - We can manage all raises exceptions by try block
  - Using `Try-exception` is costly and only use it for sample and small programs
  - `Pass` statement is necessary when we need to do nothing
  - Think about using `try` block if you can handel it with a sample `if` statement

<hr>
