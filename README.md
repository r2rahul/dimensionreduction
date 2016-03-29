## Finding Redundant Variables in the Data
The repository has the codes to identify co-linear (linearly dependent columns in a data) using linear algebra techniques.  

Here three methods are implemented:

+ Symbolic Method using Sympy.
+ Numerical method using SVD method.
+ Implementation of MATLAB __null(x, 'r')__.

For numerical technique _tol_ can be adjusted to set threshold below which variables can be removed. To be strict choose higher value of _tol_. 
