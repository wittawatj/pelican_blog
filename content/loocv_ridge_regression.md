Title: Leave-one-out Cross Validation for Ridge Regression
Date: 2013-07-30
Slug: loocv_ridge_regression
Tags: regression, model selection, cross validation, linear


$\newcommand{\bs}[1]{\boldsymbol{#1}}$
$\newcommand{\al}{\bs{\alpha}}
\newcommand{\bphi}{\bs{\phi}}
\newcommand{\x}{\bs{x}}
\newcommand{\y}{\bs{y}}$

Given a dataset $\{\x_i, y_i\}_{i=1}^n \subset \mathcal{X} \times \mathbb{R}$ the 
goal of ridge regression is to learn a linear (in parameter) function $\widehat{f}(x) = \al^\top \bphi(\x)$,
such that the squared-loss:

$\frac{1}{n} \sum_{i=1}^n ( \al^\top \bphi(\x_i) - y_i )^2 + \lambda \al^\top \al $

is minimized. Here $\lambda \geq 0$ is a regularization parameter and $\bphi(\cdot): \mathcal{X} \mapsto \mathbb{R}^D$
is a fixed basis function. 
The regularization parameter and parameter(s) in the basis function are often chosen by cross validation where data
is partitioned into $K$ non-overlapping sets of which $K-1$ sets are used to
learn $\widehat{f}$, and the last set is used for testing. This is repeated so that
each set becomes a test set exactly once. The cross validation error $E_{CV}$ is the average error over
the $K$ test sets. Finally, the parameter combination which minimizes $E_{CV}$ is selected. 
This parameter selection process is known as  *$K$-fold cross validation*. In the special case where $K=n$,
this process is also called *leave-one-out cross validation* (LOOCV) (so called 
because only one example is left out for testing).

In $K$-fold cross validation, it is necessary to learn the model $K$ times with
the $K$ dataset partitions. In LOOCV, it turns out that there is a way to avoid learning the model
$n$ times. Surprisingly, for each parameter combination the LOOCV error $E_{LOOCV}$ can be computed
with the same computational complexity as learning a model only once.

<theorem>
In ridge regression, $E_{LOOCV} = \frac{1}{n} \| H \widetilde{H}^{-1} \y \|^2$
where \
$\begin{align*}
H &= I - \Phi^\top L \\
\Phi &= \left( \bphi(\x_1) | \cdots | \bphi(\x_n) \right) \\
L &= \left( \Phi \Phi^\top + \lambda I \right)^{-1} \Phi \\
\end{align*}$ \
and $\widetilde{H}$ is a matrix with the same diagonal as $H$ and all zeros off-diagonal.
$I$ is the identity matrix.
</theorem>

**Proof**
By definition the LOOCV error is

$E_{LOOCV} = \frac{1}{n} \sum_{j=1}^n (\bphi_j^\top \widehat{\al}_j - y_j )^2 $,

where we let $\bphi_j := \bphi(\x_j)$ and $\widehat{\al}_j$ be the solution learned
using the original dataset with the $j^{th}$ example excluded. The plan here is to express
$\widehat{\al}_j$ in terms of $\widehat{\al}$ which is the solution when all examples are used, and
is given by [the normal equation](http://en.wikipedia.org/wiki/Linear_least_squares_%28mathematics%29#Derivation_of_the_normal_equations):

$\widehat{\al} = \left( \Phi \Phi^\top + \lambda I \right)^{-1} \Phi\y  = L\y $

Using the above equation but excluding the $j^{th}$ example, we have 

$\begin{align*}
\widehat{\al}_j &= \left( \Phi \Phi^\top + \lambda I - \bphi_j \bphi_j^\top \right)^{-1} (\Phi \y - \bphi_j y_j) \\
 &=\widehat{\al} + \frac{ Q^{-1} \bphi_j \bphi_j^\top \widehat{\al} - Q^{-1} \bphi_j y_j  }{1-\beta_j}
\end{align*}$

where $Q = (\Phi \Phi^\top + \lambda I)$, $\beta_j = \bphi_j^\top Q^{-1} \bphi_j $, 
and we used [Sherman-Morrison fomula](http://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula) 
to go from the first to the second line by viewing $-\bphi_j \bphi_j^\top$ as a rank-one update.
Plugging $\widehat{\al}_j$ in to $E_{LOOCV}$ above yields

$\begin{align*}
E_{LOOCV} &= \frac{1}{n}\sum_{j=1}^n \left[ \frac{1}{1-\beta_j}  (\bphi_j^\top \widehat{\al} - y_j) \right]^2 \\
 &= \frac{1}{n} \left\| \left( \Phi^\top L \y - \y \right) \widetilde{H}^{-1} \right\|^2 \\
 &= \frac{1}{n} \| H \widetilde{H}^{-1} \y \|^2
\end{align*}$

as desired. Q.E.D.


