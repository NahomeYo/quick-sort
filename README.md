# Quick Sort

## Complexity

- Best: O(n log n)
- Worst: O(n^2)
- Avg: O(n log n)
- Space: O(n^2)

## Problem Description

This quick sort implementation chooses a pivot, partitions the array into values less than, equal to, and greater than that pivot, recursively sorts the left and right partitions, and concatenates the results. The key idea is that once the pivot is chosen, every value can be grouped according to how it compares with that pivot.

That partitioning step turns one larger sorting problem into smaller ones. After the smaller left and right parts are sorted, the final result is built by placing the sorted smaller values first, the pivot group in the middle, and the sorted larger values last.

## Code

```javascript
/**
 * Sort an array with quick sort using three-way partitioning.
 *
 * @param {number[]} values Input array.
 * @param {number} pivot Pivot value for the current partition.
 * @returns {number[]} Sorted array.
 */
function quickSort(values, pivot) {
    if (values.length <= 1) {
        return values;
    }

    const left = [];
    const right = [];
    const middle = [];

    for (let index = 0; index < values.length; index++) {
        const currentValue = values[index];

        // Partition values by comparing them to the pivot.
        if (currentValue < pivot) {
            left.push(currentValue);
        } else if (currentValue > pivot) {
            right.push(currentValue);
        } else {
            middle.push(currentValue);
        }
    }

    const sortedLeft = left.length > 0
        ? quickSort(left, left[Math.floor(Math.random() * left.length)])
        : [];
    const sortedRight = right.length > 0
        ? quickSort(right, right[Math.floor(Math.random() * right.length)])
        : [];

    return [...sortedLeft, ...middle, ...sortedRight];
}

/**
 * Run the quick-sort demonstration with a random pivot from the input array.
 *
 * @returns {void}
 */
function main() {
    const array = [4, 1, 6, 8, 9, 102, 55];
    const randomIndex = Math.floor(Math.random() * array.length);
    const pivot = array[randomIndex];

    console.log("Original array =", array);
    console.log("Pivot =", pivot);
    console.log("Sorted array =", quickSort(array, pivot));
}

main();
```

## Algorithm Steps

1. If the array has length 0 or 1, return it because it is already sorted.
2. Choose a pivot value.
3. Partition the array into three groups: values less than the pivot, values equal to the pivot, and values greater than the pivot.
4. Recursively quick sort the left and right groups.
5. Concatenate the sorted left group, the middle group, and the sorted right group.

## Explanation

Quick sort is another divide-and-conquer algorithm, but unlike merge sort, it divides the problem around a pivot rather than around the middle index. The quality of that pivot choice matters a great deal. If the pivot splits the array into fairly balanced parts, the recursion stays shallow and the algorithm performs very well.

In that balanced case, quick sort has about `log n` recursive levels and performs `O(n)` partition work at each level, which gives an average runtime of `O(n log n)`. If the pivot choices are consistently poor and the partitions become heavily unbalanced, the recursion can stretch out and the runtime can degrade to `O(n^2)`.

In this JavaScript version, values are placed into the `left`, `middle`, and `right` arrays with `push()`, and the final answer is rebuilt with the spread operator in `[...sortedLeft, ...middle, ...sortedRight]`. The demo also uses `Math.floor()` and `Math.random()` to choose pivots for recursive calls on the smaller subarrays, which keeps the quick sort implementation close to the way the algorithm is explained on the page.

This implementation uses a three-way partition with `left`, `middle`, and `right` arrays, which handles duplicate values cleanly. Because it builds new arrays during each partitioning step instead of sorting fully in place, its extra space is `O(n)` on balanced recursion paths, but it can grow to `O(n^2)` in the worst case if the partitions stay heavily unbalanced. The complexity box reflects that worst-case bound for this specific implementation.
