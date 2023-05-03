This tutorial is part of the deep learning course 11-785 Introduction to Deep Leaning https://deeplearning.cs.cmu.edu/S23/index.html The short summary of the tutorial is provided here. For hands-on, checkout out the jupyter notebook ```basics.ipynb``` or original resource (Recitation-0B) from the course page.

## Intialization
### Intrinsic Numpy array creation

- 1D array creation
  - ```numpy.arange(start, stop, step)```- Return evenly spaced values within a given interval.
  - ```numpy.linspace(start, stop, num)``` - Return evenly spaced numbers over a specified interval.
- General array creation
  - From scratch
    - ```numpy.zeros(shape)```- Return a new array of given shape and type, filled with zeros.
    - ```numpy.empty(shape)```- Return a new array of given shape and type, without initializing entries.
    - ```numpy.ones(shape)```- Return a new array of given shape and type, filled with ones.
    - ```numpy.full(shape, fill_value)```- Return a new array of given shape and type, filled with fill_value.
  - Based on existing arrays
    - ```numpy.zeros_like(size)```
    - ```numpy.ones_like(size)```
    - ```numpy.full_like(size)```
  - Special 2D arrays
    - ```numpy.eye(m,n)```- Return a 2-D array with ones on the diagonal and zeros elsewhere.
    - ```numpy.identity(n)```- Return the identity array (Return the identity array.)
    
### Create array from existing data

- Converison from other python structures
  - ```numpy.array(object[List/Tuple])```- Any python object wih the array interface i.e an object that has ```__array__``` method returns an array.
- Reading from disk
  - ```numpy.loadtxt(fname)```- Load data from a text file.
  - ```numpy.load(file)```- Load arrays or pickled objects from .npy, .npz or pickled files.
 
### Use of specific library functions 
#### Random 
- ```numpy.random.ranint(low, high=None, size=None)```- Return random integers from low (inclusive) to high (exclusive).
- ```numpy.random.rand(d0,d1,...,dn)```- Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
- ```numpy.random.randn(d0,d1,...,dn)```- Return a sample (or samples) from the “standard normal” distribution.
  - For random samples from the normal distribution with mean mu and standard deviation sigma, use: ```sigma * np.random.randn(...) + mu```  

## Accessing data
- **Indexing**- ```array[i,j,k,..]```
- **Slicing** Accessing subsections of numpy arrays based on indices 
  - With range- ```array[i1:i2,j1:j2,k1:k2,..]```
  - With Intervals- ```array[start:stop:step_size]```

## Modifying data
When the array or its elements are assigned to new variable. We need to explicitly use numpy.copy, otherwise the variable is a view into the original array. 

## Pivoting data

- **Reshaping data**
  - ```numpy.reshape(arr, newshape)```- It gives a new shape to an array without changing its data. The returned array will be a new view object if possible; otherwise, it will be a copy.
- **Transposing Arrays** - The transpose operation reverses the order of an array. It switches the rows to columns and vice versa. In a multi-dimensional array, the transpose operation moves the data from one axis to another in the order specified in the transpose method.
  - ```numpy.transpose(a, axes=None)```- For an n-D array, if axes are given, their order indicates how the axes are permuted
- **Flattening Arrays** - The flatten operation in Numpy collapses arrays of multiple dimensions into one dimension.
  - ```ndarray.flatten(order='C')``` - Return a copy of the array collapsed into one dimension.
  - ```ndarray.reshape(-1)```- Flattening can be done by reshaping
- **Squeezing Arrays** - ```numpy.squeeze(arr, axis=None)``` The squeeze operation allows reduction of numpy arrays axes by dropping a specified axis, so long as it is of **unit length**. The product of the shape (overall size of the array) remains the same.
- **Unsqueezing Arrays** - ```ndarray.expand-dims(arr, axis)``` A new unit axis is inserted in specified position. Multiple unit axes can be inserted by using a tuple on the 'axis' attribute. 

## Combining Data
- **Concatenation** ```numpy.concatenate((a1, a2, ...), axis=0)```- A concatenation operation joins a sequence of arrays along an existing axis. All arrays must either have the same shape (except in the concatenating dimension) or be empty.
- **Stacking**  ```numpy.stack(arrays, axis=0)```- The stack operation joins a sequence of arrays along a *new* axis. The axis parameter specifies the index of the new axis in the dimensions of the result. All arrays need to be of the same size. The stacked array has one more dimension than the input arrays.
- **Repeat** ```numpy.repeat(arr, repeats, axis=None)```- The repeat operation repeats elements of an array. The number of repetitions for each element is broadcasted to fit the shape of the given axis. The axis parameter specifies along which axis to repeat values. By default, it uses the flattened input array, and returns a flat output array.

## Math operations
### Broadcasting
- The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes
- Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python.
  - they are equal, or 
  - one of them is 1.
- More details on this page- https://numpy.org/doc/stable/user/basics.broadcasting.html

### Element-wise operations 
- **Basic Arithmatic**- Just like basic mathematical operation on two numbers ```(+/-/*)```
- **Hamdard Product**
  - ```prod = arr1*arr2``` or ```numpy.multiply(arr1,arr2)```- If arr1.shape != arr2.shape, they must be broadcastable to a common shape (which becomes the shape of the output).
- **Others**- ```numpy.abs(arr)```, ```numpy.sqrt(arr)```

### Reduction
- ```numpy.max(arr, axis=None)``` or ```numpy.amax(arr, axis=None)```-  Return the maximum of an array or maximum along an axis. NaN values are propagated, that is if at least one item is NaN, the corresponding max value will be NaN as well.  To ignore NaN values (MATLAB behavior), please use nanmax.
- ```numpy.min(arr, axis=None)``` or ```numpy.amin(arr, axis=None)```- Return the minimum of an array or minimum along an axis. Same behavior as ```numpy.amax``` for NaN values.
- ```numpy.sum(arr, axis=None)```- Sum of array elements over a given axis.
- ```numpy.argmax(a, axis=None)```- Returns the indices of the maximum values along an axis. By default, the index is into the flattened array, otherwise along the specified axis.
- ```numpy.argmin(a, axis=None)```- Returns the indices of the minimum values along an axis. By default, the index is into the flattened array, otherwise along the specified axis.
- ```linalg.norm(x, ord=None, axis=None)```- This function is able to return one of eight different matrix norms, or one of an infinite number of vector norms. By default, it's Frobenius norm.

### Comparison
- **Element-wise**- We can use ```<,>,==,!=``` to compare two arrays element-wise. It will return a boolean numpy array.
- **Combination with Reduction**- Example ```(arr1 < arr2).any()``` 
  - ```numpy.any(arr, axis=None)```- Test whether any array element along a given axis evaluates to True.
  - ```numpy.all(arr, axis=None)```- Test whether all array elements along a given axis evaluate to True.

### Vector/Matrix operations

```numpy.matmul(x1,x2) or x1@x2```- Matrix product of two arrays. 
  - Returns 
    - scalar only when both x1,x2 are 1-d vectors
    - If both arguments are 2-D they are multiplied like conventional matrices.
    - If either argument is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly. 
    - If the first argument is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed. 
    - If the second argument is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed.
  - **Vector X Vector**- Scalar value, the Hamdard product
  - **Matrix X Vector**- The result will be a vector.
  - **Matrix X Matrix**- Basic matrix multiplication.

### Tensordot
First, we need to understand ```numpy.dot``` function.

```numpy.dot(a,b)```- Dot product of two arrays.
- If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation). Inner product theory- https://www.statlect.com/matrix-algebra/inner-product
- If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred. 
- If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred. 
- If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b. 
- If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b

```numpy.tensordot(a, b, axes=2)```- Compute tensor dot product along specified axes. Given two tensors, a and b, and an array_like object containing two array_like objects, (a_axes, b_axes), sum the products of a’s and b’s elements (components) over the axes specified by a_axes and b_axes.

## References
- Numpy official docs- https://numpy.org/doc/stable/reference/
- CS231 Spring 2023- https://deeplearning.cs.cmu.edu/S23/index.html

