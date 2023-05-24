## DSA Intro 
DS : a way of storing and organizing data 
they also provide methods of accessing and modifying them(CRUD-ing). 

Exist as defaults in two states : mutable and immutable.

## key vocabs 
1. Sequence : a way in which data is stored and accessed in a specific order 
2. Stack :  a linear data structure that follows the L.I.F.O principle 
3. Queue : a linear data structure that follows the F.I.F.O principle 
4. Index : location of an element in a sequence 
5. Iterable : able to be broken down into smaller parts of equal sizes and processed in turns i.e. loop , trasverse 
6. Slice : a group of neighbouring elements in a sequence 
7. List : a mutable (can be changed/reassigned) that can store many data types 
8. Tuple : Immutable data type that can store many data types 
9. Dictionaries : a linear data structure , Mutable data type used to store data in value and keys pairs
10. Sets : a data structure that is unordered , imutable , unindexed and do not allow duplicated values 
11. Range : a data type that stores integers in a fixed pattern 
12. String : a sequence of indexed characters.
13. Trees : non linear data structure that is hierarchial and composed of nodes which have values and can have zero or more child nodes 
14. Graphs : non linear data structure that is a collection of nodes connected by edges 
15. Linked Lists : a linear data structure in which elements are stored as individual nodes each containing a value and a reference 

### use cases 
1. The Javascript DOM , -> exists as a data structure known as a tree : this is a tree transversal method that allows one to find a child element within the DOM tree.
2. React JS has a custom ds known as the React fibre tree : its own version of the DOM 
3. Call Stack : a call stack helps to manage the execution of functions and sub routines in a program.
It uses a stack : DS to keep track of all the currently running functions in a program and makes sure execution is in the correct order 
The Call Stack operates on a L.I.F.O basis meaning the most recently pushed execution context is the first one to be popped and resumed 
When the call stack is too large a STACK OVERFLOW error occurs.

### Segue : How do Functions work ? 
- a function is a block of code that performs a specific task and can be called in other parts of a program 
- When a function is called
1. An execution context(context in which a function is executed) is created : an execution context includes all the local variables , parameters and return addresses
The return address is simply the memory location from which the function was called. It allows a program to know where to return after a function completes its executions  
2. The execution context of the calling function is suspended , and the execution context of the called function is passed to the call stack 
3. If the called function also invokes another function its execution context is also pushed to the stack , creating a stack of nested functions calls 
4. The functions are therefore executed in a L.I.F.O order (a stack)
5. The return address is used to resume execution from when a function was called. 
6. Thus the calling functions execution context is restored allowing its execution to resume from where it left off. 
7. If the call stack is too large a stack overflow error occurs. 

### Creating a custom DSA 
The DSA should 
1. Store collections of values
2. Store the relationship between those values 
3. Provide methods that will allow interactions with those values

check customdsafile in DSA package for example. 

- An advantage of building custom DSA's is it makes it easier to unders Big O notation runtimes 

BIG O terms : https://gist.github.com/josephbill/fe4c5372ef01eaa36cc774ed1dd9e8cd


