## Introduction

![](./images/stack.svg)

The stack is a linear data structure commonly used in OI. Note that this article mainly discusses the stack data structure, rather than the system stack / stack space during program execution.

The modification and access of a stack are performed according to the last-in-first-out principle, so a stack is usually called a last-in-first-out (LIFO) list.

??? warning "Warning"
    LIFO expresses that the last to enter among those **currently in the container** is the first to leave.
    
    Consider such a stack
    
    ```text
    push(1)
    pop(1)
    push(2)
    pop(2)
    ```
    
    If considered as a whole, 1 enters the stack first and leaves first, 2 enters the stack last and leaves last, which would make it a first-in-first-out list, which is obviously wrong.
    
    So, when considering whether a data structure is LIFO or FIFO, one should consider the situation within the current container.

## Simulating a stack with an array

We can conveniently use an array to simulate a stack, as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        int st[N];
        // here st[0] (i.e. *st) is used to represent the number of elements in the stack, and is also the top-of-stack index
        
        // push:
        st[++*st] = var1;
        // get top of stack:
        int u = st[*st];
        // pop: note the out-of-bounds problem, cannot continue popping when *st == 0
        if (*st) --*st;
        // clear the stack
        *st = 0;
        ```
    
    === "Python"
        ```python
        st = [0] * N
        # here st[0] is used to represent the number of elements in the stack, and is also the top-of-stack index
        
        # push:
        st[st[0] + 1] = var1
        st[0] = st[0] + 1
        # get top of stack:
        u = st[st[0]]
        # pop: note the out-of-bounds problem, cannot continue popping when *st == 0
        if st[0]:
            st[0] = st[0] - 1
        # clear the stack
        st[0] = 0
        ```

## The stack in the C++ STL

The STL in C++ also provides a container `std::stack`; before use you need to include the `stack` header file.

???+ info "The definition of `stack` in the STL"
    ```cpp
    // clang-format off
    template<
        class T,
        class Container = std::deque<T>
    > class stack;
    ```
    
    `T` is the data type to be stored in the stack.
    
    `Container` is the underlying container type used to store elements. This container must provide the following functions with the usual semantics:
    
    -   `back()`
    -   `push_back()`
    -   `pop_back()`
    
    The STL containers `std::vector`, `std::deque`, and `std::list` satisfy these requirements. If not specified, `std::deque` is used as the underlying container by default.

The `stack` container in the STL provides a host of member functions to call, among which the more commonly used ones are:

-   Element access
    -   `st.top()` returns the top of the stack
-   Modification
    -   `st.push()` inserts the passed argument onto the top of the stack
    -   `st.pop()` pops the top of the stack
-   Capacity
    -   `st.empty()` returns whether it is empty
    -   `st.size()` returns the number of elements

In addition, `std::stack` also provides some operators. The more commonly used one is using the assignment operator `=` to assign to a `stack`; example:

```cpp
// create two stacks st1 and st2
std::stack<int> st1, st2;

// load 1 into st1
st1.push(1);

// assign st1 to st2
st2 = st1;

// output the top element of st2
cout << st2.top() << endl;
// output: 1
```

## Simulating a stack with a list in Python

In Python, you can use a list to simulate a stack:

???+ note "Implementation"
    ```python
    st = [5, 1, 4]
    
    # use append() to add an element to the top of the stack
    st.append(2)
    st.append(3)
    # >>> st
    # [5, 1, 4, 2, 3]
    
    # use pop to take out the top element of the stack
    st.pop()
    # >>> st
    # [5, 1, 4, 2]
    
    # use clear to clear the stack
    st.clear()
    ```

## References

1.  [std::stack - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/stack)
