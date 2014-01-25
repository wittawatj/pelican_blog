Title: Hadamard Product to trace() of Matrix Product 
Date: 2013-08-09
Slug: hadamard-diag-trace
Tags: matrix, hadamard


$\newcommand{\diag}{\operatorname{diag}}
\newcommand{\trace}{\operatorname{tr}}$

There is an interesting matrix formula in a summary sheet by Thomas P. Minka titled 
[Old and New Matrix Algebra Useful for Statistics]( http://research.microsoft.com/~minka/papers/matrix/minka-matrix.pdf).
The formula is the following:

$x^\top (A \circ B) y = \trace( (\diag(x)A)^\top B\diag(y))$,

where $A, B$ are matrices of the same size but not necessarily square, and $x, y$ are vectors of appropriate size.
What is interesting about this formula is that it eliminates the [Hadamard product](http://en.wikipedia.org/wiki/Hadamard_product_%28matrices%29)
and turns it into a trace of product of matrices.

## Justification

One way to see that the formula is valid is to note that

$x^\top (A \circ B) y = \sum_i \sum_j x_i a_{ij}  y_j b_{ij}$,

which is equal to the sum of element-wise product of $A$ and $B$ with the 
$i^{th}$ row of $A$ weighted by $x_i$, and the $j^{th}$ column of $B$  weighted by $y_j$.
Now, $\diag(x)A$ is nothing more than $A$ with the $i^{th}$ row weighted by $x_i$.
Likewise, $B\diag(y)$ is just $B$ with each column weighted by $y_j$. 
So,

$\text{tr}( (\diag(x)A)^\top B\diag(y)) = \sum_i \sum_j x_i a_{ij} y_j b_{ij}$,

where we used the fact that $\trace(C^\top D)$ is the sum of the element-wise product
of $C$ and $D$. As an extra note, it should be obvious that 
 $\trace(C^\top D) = \boldsymbol{1}^\top (C \circ D) \boldsymbol{1}$.
