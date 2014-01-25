Title: Convolution Is Commutative
Date: 2013-10-22
Tags: convolution
Slug: convolution_commutative



The convolution of two functions f and g is written as $f\ast g$.
$$\begin{align*}
\left(f\ast g\right)(t)&:=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\, d\tau\\&=\int_{-\infty}^{\infty}f(t-\tau)g(\tau)\, d\tau\\&=\left(g\ast f\right)(t)
\end{align*}$$

Convolution appears quite often when one deals with differential equations and Fourier transforms. Interestingly, the convolution is commutative. That is, $f\ast g=g\ast f
$. This fact bothers me quite a bit as, at the first glance, the definition does not suggest so. Here is my attempt to show that it is indeed commutative to convince myself.

Let $u:=t-\tau$. So, $du=-d\tau$. 
$$\begin{align*}
\left(f\ast g\right)(t)&:=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\, d\tau\\&=\int_{u(\tau=-\infty)}^{u(\tau=\infty)}f(t-u)g(u)(-du)\\&=-\int_{\infty}^{-\infty}g(u)f(t-u)\, du\\&=\int_{-\infty}^{\infty}g(u)f(t-u)\, du\\&=\left(g\ast f\right)(t)
\end{align*}$$

