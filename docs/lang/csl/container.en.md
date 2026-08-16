## Classification

![](images/container1.png)

### Sequence containers

-   **Vector** (`vector`) A sequential list to which elements can be efficiently added at the back end.
-   **Array** (`array`) **C++11**, a fixed-length sequential list, a simple wrapper around a C-style array.
-   **Double-ended queue** (`deque`) A sequential list to which elements can be efficiently added at both ends.
-   **List** (`list`) A linked list that can be traversed in both directions.
-   **Forward list** (`forward_list`) A linked list that can only be traversed in one direction.

### Associative containers

-   **Set** (`set`) A container used to store **distinct** elements in an ordered manner. Its implementation is a red-black tree composed of nodes; each node contains an element, and the nodes are arranged by some predicate comparing the sizes of elements.
-   **Multiset** (`multiset`) A container used to store elements in an ordered manner. Equal elements are allowed to exist.
-   **Map** (`map`) A set composed of {key, value} pairs, arranged by some predicate comparing the size relationship of keys.
-   **Multimap** (`multimap`) A multiset composed of {key, value} pairs, i.e. a map that allows keys to be equal.

???+ note "What is a predicate ([**Predicate**](https://en.wikipedia.org/wiki/Predicate_%28mathematical_logic%29))?"
    A predicate is a function whose return value is true or false. Predicates are often used in STL containers, for template parameters.

### Unordered (associative) containers

-   **Unordered (multi)set** (`unordered_set`/`unordered_multiset`) **C++11**, the difference from `set`/`multiset` is that the elements are unordered, only caring about "whether an element exists", implemented using hashing.
-   **Unordered (multi)map** (`unordered_map`/`unordered_multimap`) **C++11**, the difference from `map`/`multimap` is that the keys are unordered, only caring about "the correspondence between keys and values", implemented using hashing.

### Container adapters

Container adapters are actually not containers. They do not have certain characteristics of containers (such as: having iterators, having a `clear()` function……).

> "An adapter is a mechanism that makes the behavior of one thing similar to the behavior of another thing"; an adapter wraps a container, making it exhibit another kind of behavior.

-   **Stack** (`stack`) A last-in-first-out (LIFO) container, by default a wrapper around a double-ended queue (`deque`).
-   **Queue** (`queue`) A first-in-first-out (FIFO) container, by default a wrapper around a double-ended queue (`deque`).
-   **Priority queue** (`priority_queue`) A queue in which the order of elements is determined by some predicate acting on the stored value pairs, by default a wrapper around a vector (`vector`).

## Commonalities

### Container declaration

They are all of the form `containerName<typeName,...> name`, but the number and form of the template parameters (the parameters inside `<>`) will vary according to the specific container.

The essential reason: STL is the "Standard Template Library", so containers are all template classes.

### Iterators

Please refer to [iterators](./iterator.md).

### Shared functions

`=`: has an assignment operator as well as a copy constructor.

`begin()`: returns an iterator pointing to the beginning element.

`end()`: returns an iterator pointing to the next element after the end. `end()` does not point to a certain element, but it is the successor of the end element.

`size()`: returns the number of elements in the container.

`max_size()`: returns the maximum number of elements the container can **theoretically** store. It varies according to the container type and the type of the stored variable.

`empty()`: returns whether the container is empty.

`swap()`: swaps two containers.

`clear()`: clears the container.

`==`/`!=`/`<`/`>`/`<=`/`>=`: compares the sizes of two containers in **lexicographic order**. (When comparing element sizes, each element of a `map` is equivalent to `set<pair<key, value>>`; unordered containers do not support `<`/`>`/`<=`/`>=`.)
