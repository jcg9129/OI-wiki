An array is a container that stores objects of the same type; the objects stored in an array have no names, but are accessed through their positions. The size of an array is fixed; the length of an array cannot be changed arbitrarily.

## Defining an array

The declaration of an array has the form `a[d]`, where `a` is the name of the array and `d` is the number of elements in the array. At compile time, `d` should be known, that is, `d` should be an integer constant expression.

```cpp
unsigned int d1 = 42;
const int d2 = 42;
int arr1[d1];  // error: d1 is not a constant expression
int arr2[d2];  // correct: arr2 is an array of length 42
```

We cannot directly assign one array to another array:

```cpp
int arr1[3];
int arr2 = arr1;  // error
arr2 = arr1;      // error
```

We should try to define larger arrays as global variables. Because local variables are created on the stack, an array that is too large (larger than the size of the stack) will overflow the stack, thereby causing RE. If the array is declared in the global scope, it will be created in the static area.

## Accessing array elements

We can access the elements in an array through the subscript operator `[]`; the index of an array (i.e. the value in the square brackets) starts from 0. Taking an array with 10 elements as an example, its indices are 0 to 9, not 1 to 10. But in OI, for convenience of use, we usually make the array a bit larger, not use the first element of the array, and access array elements starting from subscript 1.

Example 1: Read an integer $n$ from standard input, then read $n$ numbers and store them in an array. Here, $n\leq 1000$.

```cpp
#include <iostream>
using namespace std;

int arr[1001];  // the subscript range of array arr is [0, 1001)

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> arr[i];
  }
}
```

Example 2: (continuing from Example 1) Sum the elements in array `arr` and output the sum. It is satisfied that the sum of all elements in the array is less than or equal to $2^{31} - 1$.

```cpp
#include <iostream>
using namespace std;

int arr[1001];

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> arr[i];
  }

  int sum = 0;
  for (int i = 1; i <= n; ++i) {
    sum += arr[i];
  }

  printf("%d\n", sum);
  return 0;
}
```

### Out-of-bounds subscript access

The subscript $\mathit{idx}$ of an array should satisfy $0\leq \mathit{idx}< \mathit{size}$; if the subscript is not in this range, it is undefined behavior, which will produce unpredictable consequences, such as a segmentation fault (Segmentation Fault), or modifying an unexpected variable, etc.

## Multidimensional arrays

The essence of a multidimensional array is an "array of arrays", i.e. the elements of the outer array are arrays. A two-dimensional array needs two dimensions to define: the length of the array and the length of the elements within the array. When accessing a two-dimensional array, we need to write out two indices:

```cpp
int arr[3][4];  // an array of length 3, whose elements are "arrays of length 4
                // whose elements are int"
arr[2][1] = 1;  // accessing a two-dimensional array
```

We often use nested for loops to process two-dimensional arrays.

Example: Read two numbers $n$ and $m$ from standard input, representing the height and width of a black-and-white picture respectively, satisfying $n,m\leq 1000$. For the next $n$ lines of data, each line has $m$ numbers separated by spaces, representing the brightness value at this position. Now we read this picture and store it in a two-dimensional array.

```cpp
const int MAXN = 1001;
int pic[MAXN][MAXN];
int n, m;

cin >> n >> m;
for (int i = 1; i <= n; ++i)
  for (int j = 1; j <= m; ++j) cin >> pic[i][j];
```

Similarly, you can define three-dimensional, four-dimensional, and higher-dimensional arrays.
