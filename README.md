## Finding Redundant Variables in the Data
The repository has the codes to identify co-linear (linearly dependent columns in a data) using linear algebra techniques.  

Here three methods are implemented:

+ Symbolic Method using Sympy.
+ Numerical method using SVD method.
+ Implementation of MATLAB __null(x, 'r')__.

For numerical technique _tol_ can be adjusted to set threshold below which variables can be removed. To be strict choose higher value of _tol_. 

## R Version of the Code

Added Rcpp version of Reduced Row Echelon form (rref) which also return the pivot columns similar to MATLAB implementation. To compile the code 

```r
Rcpp::sourceCpp("src/rref_pivots.cpp")
A <- matrix(c(2, 4, 1, 3, -1, -2, 1,
0, 0, 0, 4, 4, 3, 6, 2, 5), nrow = 4,
byrow = TRUE)
rref_out <- rref_with_pivots(A)
print(rref_out$pivots)
```
