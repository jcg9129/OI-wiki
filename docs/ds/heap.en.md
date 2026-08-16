author: ouuan, HeRaNO

A heap is a tree in which each node has a key value, and the key value of each node is greater than or equal to / less than or equal to the key value of its parent.

A heap in which the key value of each node is greater than or equal to its parent's key value is called a min-heap; otherwise it is called a max-heap. The [`priority_queue` in the STL](../lang/csl/container-adapter.md#priority-queue) is actually a max-heap.

The operations a (min-)heap mainly supports are: inserting a number, querying the minimum value, deleting the minimum value, merging two heaps, and decreasing the value of an element.

Some powerful heaps (mergeable heaps) can also (efficiently) support operations such as merge.

Some even more powerful heaps also support persistence, i.e. querying or operating on any historical version to produce a new version.

## Classification of heaps

|    Operation `\` data structure[^ref4]   |                                      Pairing heap                                     |      Binary heap     |      Leftist tree     |          Binomial heap         |        Fibonacci heap       |
| :---------------------: | :--------------------------------------------------------------------------: | :----------: | :----------: | :------------------: | :----------------: |
|        insert       |                                    $O(1)$                                    |  $O(\log n)$ |  $O(\log n)$ |  $O(\log n)$[^ref1]  |       $O(1)$       |
|     find-min     |                                    $O(1)$                                    |    $O(1)$    |    $O(1)$    | $O(1)$[^ref2][^ref3] |       $O(1)$       |
|    delete-min    |                              $O(\log n)$[^ref3]                              |  $O(\log n)$ |  $O(\log n)$ |      $O(\log n)$     | $O(\log n)$[^ref3] |
|        merge       |                                    $O(1)$                                    |    $O(n)$    |  $O(\log n)$ |      $O(\log n)$     |       $O(1)$       |
| decrease-key | $o(\log n)$ (lower bound $\Omega(\log \log n)$, upper bound $O(2^{2\sqrt{\log \log n}})$)[^ref3] |  $O(\log n)$ |  $O(\log n)$ |      $O(\log n)$     |    $O(1)$[^ref3]   |
|         supports persistence        |                                   $\times$                                   | $\checkmark$ | $\checkmark$ |     $\checkmark$     |      $\times$      |

[^ref1]: The complexity of a single insertion is $O(\log n)$, but with $k$ consecutive insertions, one can create a binomial heap containing only the elements to be inserted and then merge this heap with the original binomial heap, giving an amortized complexity of $O(1)$

[^ref2]: One can keep a pointer to the minimum element and modify this pointer when performing other operations, so that queries can be done in $O(1)$ complexity

[^ref3]: The complexity is amortized

[^ref4]: The table is from [Wikipedia](https://en.wikipedia.org/wiki/Priority_queue#Summary_of_running_times)

By convention, when "heap" is mentioned without qualification, it usually refers to a binary heap.
