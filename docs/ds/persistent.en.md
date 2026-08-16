author: morris821028

## Introduction

A persistent data structure can always retain every historical version and supports the immutable characteristic of operations.

## Classification of persistence

### Partially persistent

All versions can be accessed, but only the latest version can be modified.

### Fully persistent

All versions can be both accessed and modified.

If merging two historical versions is supported, it is also called confluently persistent.

## Practical applications

### Geometric computation

In geometric computation there are many offline algorithms, such as the sweep-line algorithm that sweeps across once to answer all queries, which is excellent in terms of time-complexity analysis. But in a forced-online situation, sweeping each time reduces the time complexity of a query operation from logarithmic to linear. To solve this situation, persistence technology provides another way of thinking: we take the time axis of the sweep line as a basis for variation and persist the related structure; as long as we can shuttle a query through this time axis in logarithmic time, we can surely solve the previous problem dynamically.

### String processing

To achieve very high-efficiency merge operations and prevent the performance degradation accompanying the generation of large amounts of duplicated strings, all kinds of operations can be far below linear operations. For example, C++'s rope is a persistent data structure. Not only string operations—if the processed type has many duplicates, the concept of persistence can come in handy.

### Version rollback

This actually corresponds to the redo/undo in most application software. If a database/operation change comes with a complex structure for high-efficiency operations (not like hash or set reversal operations that need only constant or logarithmic time), then to quickly roll back the change result, the persistent structure is meant to reduce the cost of redo/undo.

The database itself can roll back in constant time, needing only to record part of the change. And for application-layer computation, most implementations delete the cache and recompute a new structure; sometimes the size of the rolled-back change is m, but recomputing the structure consumes n+m; if the gap between n and m is very large, then the experience of continuous rollback is very poor.

### Functional programming

Functional programming requires special data structures to conform to language characteristics, among which the immutable property is more important, to facilitate parallel environments and debugging. For example, object-oriented Java 8 and later introduced the stream class, supporting writing functional-style syntax design and providing special features such as lazy evaluation and infinite value ranges.

## References

-   <https://en.wikipedia.org/wiki/Persistent_data_structure>
-   MIT course <https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-854j-advanced-algorithms-fall-2005/lecture-notes/persistent.pdf>
