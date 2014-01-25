Title: Laplace Approximation and Bayesian Information Criterion
Date: 2013-12-01
Tags: model selection, bayesian
Slug: laplace_apporx_bic


Consider a model selection problem in which we attempt to find the
model best describing our observed data. Given an observed sample
$\mathcal{D}=\{\mathbf{x}_{1},\ldots,\mathbf{x}_{N}\}$, frequentist
treatment will find the best $\theta^{*}$ such that $p(\mathcal{D}|\theta^{*})$
is largest. Here we assume that the data follow some parametric model
parameterized by $\theta$. Instead of considering only one best parameter,
Bayesian model selection considers a distribution of possible parameters.
This distribution is encapsulated in a model class. A model class
$m$ is a set of distributions parameterized by $\theta_{m}$. An
example of a model class might be a mixture of $K$ Gaussians. Instead
of the usual notion of likelihood $p(\mathcal{D}|\theta)$, we now
consider $p(\mathcal{D}|m)$ which is known as Bayesian evidence for
model $m$. 
$$\begin{align*}
p(\mathcal{D}|m) & =\int_{\Theta_{m}}p(\mathcal{D},\theta_{m}|m)\, d\theta_{m}\\
 & =\int_{\Theta_{m}}p(\mathcal{D}|\theta_{m},m)p(\theta_{m}|m)\, d\theta_{m}
\end{align*}$$
The Bayesian evidence $p(\mathcal{D}|m)$ can be interpreted as the
probability that randomly selected parameter from the model class
would generate the data set $\mathcal{D}$. So, not just one single
parameter but a range of parameters are considered.


## Why Bayesian evidence ? 

The drawback of the data likelihood is that $p(\mathcal{D}|\theta)$
is always larger for more complex models due to overfitting. In Bayesian
evidence, if a model $m_{1}$ is very complex, then $m_{1}$ can generate
many possible data sets. As a result, it is unlikely to generate the
particular data set $\mathcal{D}$ at random. If the model $m_{2}$
is too simple, the likelihood will be small, suggesting that it is
unlikely to be a good fit. So, roughly speaking, Bayesian evidence
has a regularization in itself allowing us to choose the model which
is just right. 


## Laplace Approximation

One drawback of considering Bayesian evidence is that it is difficult
to evaluate $p(\mathcal{D}|m)=\int_{\Theta_{m}}p(\mathcal{D},\theta_{m}|m)\, d\theta_{m}$.
Laplace approximation is a way to approximate $p(\mathcal{D}|m)$
by observing that as data size $N$ grows relative to the parameter
count $d$, $\theta_{m}$ becomes more concentrated around the posterior
mode $\theta_{m}^{*}$. The idea here is to approximate $\log p(\mathcal{D},\theta_{m}|m)$
to the second-order around $\theta_{m}^{*}$ by Taylor expansion.
$$\begin{align*}
 & \int p(\mathcal{D},\theta_{m}|m)\, d\theta_{m}\\
 & =\int\exp\log p(\mathcal{D},\theta_{m}|m)\, d\theta_{m}\\
 & \approx\int p(\mathcal{D},\theta_{m}^{*}|m)\exp\left(\overbrace{\nabla\log p(\mathcal{D},\theta_{m}^{*}|m)}^{=0\text{ (}\theta_{m}^{*}\text{ is at the mode)}}(\theta_{m}-\theta_{m}^{*})+\frac{1}{2}(\theta_{m}-\theta_{m}^{*})^{\top}\overbrace{\nabla^{2}\log(\mathcal{D},\theta_{m}^{*}|m)}^{=-A}(\theta_{m}-\theta_{m}^{*})\right)\, d\theta_{m}\\
 & =p(\mathcal{D},\theta_{m}^{*}|m)\int\exp\left(\frac{1}{2}(\theta_{m}-\theta_{m}^{*})^{\top}\overbrace{\nabla^{2}\log(\mathcal{D},\theta_{m}^{*}|m)}^{=-A}(\theta_{m}-\theta_{m}^{*})\right)\, d\theta_{m}\\
 & =p(\mathcal{D}|\theta_{m}^{*},m)p(\theta_{m}^{*}|m)(2\pi)^{d/2}|A|^{-1/2}
\end{align*}$$
where we let $A:=-\nabla^{2}\log(\mathcal{D},\theta_{m}^{*}|m)$,
the negavie Hessian evaluated at $\theta_{m}^{*}$ which is negative
definite. Notice that the integral evaluation in the last line is
the same as in a multivariate normal distribution. So we end up having
the normalization factor $(2\pi)^{d/2}|A|^{-1/2}$. As can be seen,
the integral $\int p(\mathcal{D},\theta_{m}|m)\, d\theta_{m}$ in
the end turns out to be a point evaluation at $\theta_{m}^{*}$. The
difficult component to evalute in this case may be the negative Hessian
$A$. 


## Bayesian Information Criterion (BIC)

BIC simplifies the Laplace approximation even further by assuming
that the sample size $N\rightarrow\infty$. Since $\log p(\mathcal{D}|\theta_{m}^{*},m)$
grows with $N$ (i.e., we have $\log p(\mathbf{x}^{(n)}|\theta_{m}^{*},m)$
for each $n^{th}$example), when $N$ is large, the term will dominate
the rest. Hence, we can drop the terms which do not depend on $N$.
$$\begin{align*}
\log p(\mathcal{D}|m) & \approx\log p(\mathcal{D}|\theta_{m}^{*},m)+\overbrace{\log p(\theta_{m}^{*}|m)}^{\text{independent of }N}+\log(2\pi)^{d/2}+\log|A|^{-1/2}
\end{align*}$$
Note that the matrix $A$ grows as $NA_{0}$ for some constant matrix
$A_{0}$. So $\log|A|^{-1/2}\approx\log|NA_{0}|^{-1/2}=-\frac{d}{2}\log N+\log|A_{0}|^{-1/2}$.
By dropping all terms which are independent of $N$, we have
$$\begin{align*}
\log p(\mathcal{D}|m) & \approx\log p(\mathcal{D}|\theta_{m}^{*},m)-\frac{d}{2}\log N.
\end{align*}$$
The final BIC equation is just the usual likelihood under the parameter
$\theta_{m}^{*}$ subtracted by a multiple of the number of parameters
$d$. Intuitively the higher $d$ (the more complex the model), the
likelihood term will be higher. However, the second term will penalize
that complexity. BIC is easy to compute and does not depend on any
prior. 

