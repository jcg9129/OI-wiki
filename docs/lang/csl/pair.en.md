author: sbofgayschool

`std::pair` is a class template defined in the standard library. It is used to associate two variables together to form a "pair", and the data types of the two variables can be different.

??? note "Class template"
    A class template is itself not a class, but a "template" that can produce **different classes** according to **different data types**.
    
    When used, the compiler will produce the corresponding class according to the passed-in data type, and then create the corresponding instance.
    
    Templates are a relatively advanced language feature of C++ and almost never appear in informatics competitions. If you are interested in this, you can further read 《C++ Primer》 to learn deeper C++ knowledge.

By flexibly using `pair`, we can easily cope with scenarios that **need to bundle, store, and process associated data**.

??? note "Struct"
    Compared with a custom `struct`, `pair` does not need to additionally define the structure and overload operators, so it is more convenient to use.
    
    However, the variable naming of a custom `struct` is often clearer (`pair` can only use `first` and `second` to access the two contained variables). At the same time, if we need to associate more than two variables, a custom `struct` is more appropriate.

## Usage

### Initialization

We can directly complete the initialization of a `pair` at the time of definition.

```cpp
pair<int, double> p0(1, 2.0);
```

We can also use the method of defining first and then assigning to complete the initialization of a `pair`.

```cpp
pair<int, double> p1;
p1.first = 1;
p1.second = 2.0;
```

We can also use the `std::make_pair` function. This function accepts two variables and returns a `pair` composed of these two variables.

```cpp
pair<int, double> p2 = make_pair(1, 2.0);
```

A commonly used method is to use the macro definition `#define mp make_pair`, simplifying the somewhat verbose `make_pair` to `mp`.

In C++11 and later versions, `make_pair` can be used together with `auto` to avoid explicitly declaring data types.

```cpp
auto p3 = make_pair(1, 2.0);
```

Regarding the use of `auto` in informatics competitions, see the explanation in the [iterator](./iterator.md) part.

### Access

Through the member functions `first` and `second`, we can access the two variables contained in a `pair`.

```cpp
int i = p0.first;
double d = p0.second;
```

We can also modify them.

```cpp
p1.first++;
```

### Comparison

`pair` has predefined all comparison operators, including `<`, `>`, `<=`, `>=`, `==`, `!=`. Of course, this requires that the data types of the two variables composing the `pair` define the `==` and/or `<` operators.

Among them, the four operators `<`, `>`, `<=`, `>=` first compare the first variables in the two `pair`s, and compare the second variables only when the first variables are equal.

```cpp
if (p2 >= p3) {
  cout << "do something here" << endl;
}
```

Since `pair` defines the `<` and `==` commonly used in STL, it can work well with other STL functions or data structures. For example, `pair` can be used as the data type of `priority_queue`.

```cpp
priority_queue<pair<int, double>> q;
```

### Assignment and swap

We can assign the value of a `pair` to another `pair` of the same type.

```cpp
p0 = p1;
```

We can also use the `swap` function to swap the values of `pair`s.

```cpp
swap(p0, p1);
p2.swap(p3);
```

## Application examples

### Discretization

`pair` can easily implement discretization.

We can create a `pair` array, taking the value of the original data as the first variable of each `pair`, and the position of the original data as the second variable. After sorting, assign the rank of the original data value (the position where this value is located after sorting) to the position where this value was originally located.

```cpp
// a is the original data
pair<int, int> a[MAXN];
// ai is the discretized data
int ai[MAXN];
for (int i = 0; i < n; i++) {
  // first is the value of the original data, second is the position of the original data
  scanf("%d", &a[i].first);
  a[i].second = i;
}
// sort
sort(a, a + n);
for (int i = 0; i < n; i++) {
  // assign the rank of this value to the position where this value was originally located
  ai[a[i].second] = i;
}
```

### Dijkstra

As mentioned above, `pair` can be used as the data type of `priority_queue`.

Then, in the heap optimization of the Dijkstra algorithm, we can use `pair` and `priority_queue` to maintain nodes, taking the node's current distance to the start point as the first variable, and the node number as the second variable.

```cpp
priority_queue<pair<int, int>, std::vector<pair<int, int>>,
               std::greater<pair<int, int>>>
    q;
... while (!q.empty()) {
  // dis is the distance from the node to the start point when pushed into the heap, i is the node number
  int dis = q.top().first, i = q.top().second;
  q.pop();
  ...
}
```

### pair and map

`map` is the data structure in C++ that stores key-value pairs. In many cases, the key-value pairs stored in a `map` are exposed to the outside through `pair`.

```cpp
map<int, double> m;
m.insert(make_pair(1, 2.0));
```

For more content about `map`, see the relevant parts in [associative containers](./associative-container.md) and [unordered associative containers](./unordered-container.md).
