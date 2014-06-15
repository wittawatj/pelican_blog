Title: Kernel PCA
Date: 2014-05-07
Slug: kpca
Tags: kernel


The goal of the ordinary PCA (Principal Component Analysis) is to
find a set of orthogonal directions such that the variance of the
projected data is maximized. Assume we have samples $\{x_{i}\}_{i=1}^{n}$.
This idea can be formalized as 
$$
u_{1}=\arg\max_{\|u\|\leq1}\frac{1}{n}\sum_{i=1}^{n}\left(u^{\top}x_{i}-u^{\top}\bar{x}\right)^{2}
$$
where $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_{i}$ and $u$ is the direction
we wish to find. Define $C=\frac{1}{n}XHX^{\top}$ where
$$\begin{eqnarray*}
X & = & \left(x_{1}|\cdots|x_{n}\right)\\
H & = & I-\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}.
\end{eqnarray*}$$
Then the PCA problem can be solved by considering the eigenvalue problem:
$$
Cu=\lambda u.
$$



### KPCA

In kernel PCA or KPCA, the goal is to do PCA in the feature space.
That is $\{x_{i}\}_{i=1}^{n}$ are mapped into a high (or even infinite)
dimensional space and PCA is carried out in that space. Let $\phi$
be such feature map. KPCA can be formalized as
$$
f_{1}=\arg\max_{\|f\|_{\mathcal{H}}\leq1}\frac{1}{n}\sum_{i=1}^{n}\left\langle f,\phi(x_{i})-\bar{\phi}\right\rangle _{\mathcal{H}}^{2}
$$
where $\bar{\phi}=\frac{1}{n}\sum_{i=1}^{n}\phi(x_{i})$, $f$ is
the direction (can be infinite-dimensional) we wish to find, and $\mathcal{H}$
is assumed to be a reproducing kernel Hilbert space with the inner
product given by a kernel $k$ i.e., $\left\langle \phi(x),\phi(y)\right\rangle _{\mathcal{H}}=k(x,y)$.
Let $\tilde{\phi}_{i}:=\phi(x_{i})-\bar{\phi}$ for convenience. The
squared inner product in the sum can be simplified as 
$$\begin{eqnarray*}
\left\langle f,\tilde{\phi}_{i}\right\rangle _{\mathcal{H}}^{2} & = & \left\langle f,\tilde{\phi}_{i}\right\rangle _{\mathcal{H}}\left\langle f,\tilde{\phi}_{i}\right\rangle _{\mathcal{H}}=\left\langle f,\left\langle f,\tilde{\phi}_{i}\right\rangle _{\mathcal{H}}\tilde{\phi}_{i}\right\rangle _{\mathcal{H}}\\
 & = & \left\langle f,\left(\tilde{\phi}_{i}\otimes\tilde{\phi}_{i}\right)f\right\rangle _{\mathcal{H}}.
\end{eqnarray*}$$
With this form, the optimization problem can be rewritten as
$$
f_{1}=\arg\max_{\|f\|_{\mathcal{H}}\leq1}\left\langle f,Cf\right\rangle _{\mathcal{H}}
$$
where $C:=\frac{1}{n}\sum_{i=1}^{n}\tilde{\phi}_{i}\otimes\tilde{\phi}_{i}$.
Notice that $Cf$ involves an inner product of $f$ and $\tilde{\phi}_{i}$.
This implies that if $f$ has any component orthogonal to $\tilde{\phi}_{i}$,
it will vanish after taking the inner product. Hence, we can conclude
that $f$ must be a linear combination of $\{\tilde{\phi}_{i}\}_{i}$
(lie in the span of $\{\tilde{\phi}_{i}\}_{i}$):
$$
f_{l}=\sum_{i=1}^{n}\alpha_{li}\tilde{\phi}_{i}=\tilde{X}\boldsymbol{\alpha}_{l}
$$
where we define $\tilde{X}:=\left(\tilde{\phi}_{1}|\cdots|\tilde{\phi}_{n}\right)$
and $\boldsymbol{\alpha}_{l}$ are coefficients. With the definition
of $\tilde{X}$, we have $C=\frac{1}{n}\tilde{X}\tilde{X}^{\top}$.


### Eigenvalue problem for KPCA

The KPCA can be solved by considering the following eigenvalue problem.
$$
f_{l}\lambda_{l}=Cf_{l}
$$
Recall that $f_{l}$ can be infinite-dimensional. To solve the problem,
we multiply both sides to the left by $\tilde{X}^{\top}$.
$$
\tilde{X}^{\top}f_{l}\lambda_{l}=\tilde{X}^{\top}\tilde{X}\boldsymbol{\alpha}_{l}\lambda_{l}=\tilde{K}\boldsymbol{\alpha}_{l}\lambda_{l}
$$
where $\tilde{K}:=\tilde{X}^{\top}\tilde{X}=HKH$ is the centered
gram matrix. For the right hand side,
$$\begin{eqnarray*}
\tilde{X}^{\top}Cf_{l} & = & \frac{1}{n}\tilde{X}^{\top}\tilde{X}\tilde{X}^{\top}f_{l}=\frac{1}{n}\tilde{X}^{\top}\tilde{X}\tilde{X}^{\top}\tilde{X}\boldsymbol{\alpha}_{l}\\
 & = & \frac{1}{n}\tilde{K}^{2}\boldsymbol{\alpha}_{l}.
\end{eqnarray*}$$
Equating the previous two equations, we have
$$
n\lambda_{l}\tilde{K}\boldsymbol{\alpha}_{l}=\tilde{K}^{2}\boldsymbol{\alpha}_{l}\iff n\lambda_{l}\boldsymbol{\alpha}_{l}=\tilde{K}\boldsymbol{\alpha}_{l}
$$
which is just an $n$-dimensional eigenvalue problem. 


### Norm constraint of KPCA

Recall that we have the constraint $\|f\|_{\mathcal{H}}\leq1$. Since
the maximization problem benefits from scaling up $f$, the solution
will satisfy $\|f\|_{\mathcal{H}}=1=\|f\|_{\mathcal{H}}^{2}$. 
$$\begin{eqnarray*}
\|f\|_{\mathcal{H}}^{2} & = & 1=\left\langle \tilde{X}\boldsymbol{\alpha},\tilde{X}\boldsymbol{\alpha}\right\rangle _{\mathcal{H}}\\
 & = & \boldsymbol{\alpha}\tilde{K}\boldsymbol{\alpha}\\
 & = & n\lambda\boldsymbol{\alpha}^{\top}\boldsymbol{\alpha}=1
\end{eqnarray*}$$
where we use the identity from the eigenvalue equation in the last
two lines. The last line implies that 
$$
\|\boldsymbol{\alpha}\|_{\mathcal{H}}^{2}=\frac{1}{n\lambda}\iff\|\boldsymbol{\alpha}\|_{\mathcal{H}}=\frac{1}{\sqrt{n\lambda}}.
$$
This means that to force the norm constraint $\|f\|_{\mathcal{H}}=1$,
we need to make sure that $\|\boldsymbol{\alpha}\|_{\mathcal{H}}=\frac{1}{\sqrt{n\lambda}}$.
This can be done by renormalizing $\boldsymbol{\alpha}$ obtained
from the eigenvalue problem by
$$
\boldsymbol{\alpha}\leftarrow\frac{\boldsymbol{\alpha}}{\|\boldsymbol{\alpha}\|_{2}}\frac{1}{\sqrt{n\lambda}}.
$$



### KPCA projection

Define the projection operator $P_{d}$ for projection onto the first
$d$ eigenvectors as
$$\begin{eqnarray*}
P_{d}\phi(x^{*}) & = & \sum_{i=1}^{d}P_{f_{i}}\phi(x^{*})\\
P_{f}\phi(x^{*}) & = & \left\langle f,\phi(x^{*})\right\rangle _{\mathcal{H}}f.
\end{eqnarray*}$$
Given a new point $x^{*}$ its projection can be found with 
$$
y^{*}=\arg\min_{y\in\mathcal{X}}\|\phi(y)-P_{d}\phi(x^{*})\|_{\mathcal{H}}^{2}.
$$
This is useful, for example, in image denoising where $x^{*}$ is
a noisy image, and a denoised (projected) image $y^{*}$ is the goal. 


### KPCA coordinates

If dimensionality reduction or visualization is the goal, then the
projection step is not needed. In these cases, one simply needs the
first $d$ coordinates (where $d$ is usually chosen to be low). The
$d$ coordinates are given by
$$
\left(\begin{array}{c}
\left\langle \phi(x^{*}),f_{1}\right\rangle _{\mathcal{H}}\\
\left\langle \phi(x^{*}),f_{2}\right\rangle _{\mathcal{H}}\\
\vdots\\
\left\langle \phi(x^{*}),f_{d}\right\rangle _{\mathcal{H}}
\end{array}\right)=\left(\begin{array}{c}
\left\langle \phi(x^{*}),\tilde{X}\boldsymbol{\alpha}_{1}\right\rangle _{\mathcal{H}}\\
\left\langle \phi(x^{*}),\tilde{X}\boldsymbol{\alpha}_{2}\right\rangle _{\mathcal{H}}\\
\vdots\\
\left\langle \phi(x^{*}),\tilde{X}\boldsymbol{\alpha}_{d}\right\rangle _{\mathcal{H}}
\end{array}\right)=\left(\begin{array}{c}
\sum_{i=1}^{n}\tilde{k}(x^{*},x_{i})\alpha_{1,i}\\
\sum_{i=1}^{n}\tilde{k}(x^{*},x_{i})\alpha_{2,i}\\
\vdots\\
\sum_{i=1}^{n}\tilde{k}(x^{*},x_{i})\alpha_{d,i}
\end{array}\right).
$$
Note that $f_{1}$ corresponds to the largest eigenvector, $f_{2}$
the second largest, and so on.