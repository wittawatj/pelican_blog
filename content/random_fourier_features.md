Title: Random Fourier Features 
Date: 2014-08-30 
Tags: kernel, primal, random 
Slug: random_fourier_features


A kernel $k(x,y)=\left\langle \phi(x),\phi(y)\right\rangle $ in general
may correspond to an inner product in an infinite-dimensional space
whose feature map $\phi$ cannot be explicitly computed. In
[Rahimi & Recht 2007](https://keysduplicated.com/~ali/random-features/)
, methods for computing an approximate feature
maps $\hat{\phi}$ were proposed. The approximate feature maps are such
that $k(x,y)\approx\hat{\phi}(x)^{\top}\hat{\phi}(y)$ (with equality in
expectation) where $\hat{\phi}\in\mathbb{R}^{d}$ and $d$ is a free
parameter. High $d$ yields a better approximation with higher
computational cost.

Assume $k(x,y)=k(x-y)$ (translation invariant) and $x,y\in\mathbb{R}^{m}$. Random Fourier features
$\hat{\phi}(x)\in\mathbb{R}^{d}$ such that
$k(x,y)\approx\hat{\phi}(x)^{\top}\hat{\phi}(y)$ are generated as following.

1.  Compute the Fourier transform $\hat{k}$ of the kernel $k$. That is, 
    $\hat{k}(\omega)=\frac{1}{2\pi}\int e^{-j\omega^{\top}\delta}k(\delta)\, d\delta$.
    For a Gaussian kernel with unit width,
    $\hat{k}(\omega)=\left(2\pi\right)^{-m/2}e^{-\|\omega\|^{2}/2}$.

2.  Draw $d$ i.i.d. samples
    $\omega_{1},\ldots,\omega_{d}\in\mathbb{R}^{m}$ from $p$ i.e.,
    `randn(m, d)`. Draw $d$ i.i.d samples
    $b_{1},\ldots,b_{d}\in\mathbb{R}$ from $U[0,2\pi]$ (uniform
    distribution).

3.  $\hat{\phi}(x)=\sqrt{\frac{2}{d}}\left(\cos\left(\omega_{1}^{\top}x+b_{1}\right),\ldots,\cos\left(\omega_{d}^{\top}x+b_{d}\right)\right)^{\top}$

### Why it works ?

**Bochner’s theorem**: A continuous kernel $k(x,y)=k(x-y)$ on
$\mathbb{R}^{m}$ is positive definite iff $k(\delta)$ is the Fourier
transform of a non-negative measure.

Furthermore, if a translation invariant kernel $k(\delta)$ is properly
scaled, Bochner’s theorem guarantees that its Fourier transform
$\hat{k}(\omega)$ is a proper probability distribution. From this fact, we
have
$$k(x-y)=\int\hat{k}(\omega)e^{j\omega^{\top}\left(x-y\right)}\, d\omega=\mathbb{E}_{\omega}\left[\eta_{\omega}(x)\eta_{\omega}(y)^{*}\right]$$
where $\eta_{\omega}(x)=e^{j\omega^{\top}x}$ and $\cdot^{*}$ denotes the
complex conjugate. Since both $\hat{k}$ and $k$ are real, the complex
exponential contains only the cosine terms. Drawing $d$ samples is for
lowering the variance of the approximation. The uniformly random numbers 
$\{b_i\}_i$ are to correct the bias of the estimator.

