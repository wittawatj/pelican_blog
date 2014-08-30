Title: Summary of Expectation Propagation
Date: 2014-08-30
Tags: ep, inference 
Slug: expectation_propagation


Expectation propagation (EP) is an approximate inference method used to
infer approximate distributions of latent variables. In many
probabilistic models, the joint distribution of the data $X$ and latent
variables $\theta$ takes the form of a product of factors $f_{i}$
$$p(X,\theta)=\prod_{i=1}^{m}f_{i}(X|\theta).$$ EP can be used to
estimate the posterior distribution $p(\theta|X)$. With $X$ observed,
the idea of EP is to approximate the posterior with
$$q(\theta)\propto\prod_{i=1}^{m}\tilde{f}_{i}(X|\theta)$$ where
$\tilde{f}_{i}$ is an approximate factor corresponding to $f_{i}$ with
the constraint that $\tilde{f}_{i}$ belongs to a chosen parametric form
(e.g., Gaussian) in the exponential family. Instead of considering each
factor $f_{i}$ individually and finding its corresponding
$\tilde{f}_{i}$, EP takes into account the fact that the final quantity
of interest is the posterior $q(\theta)$ which is given by the product
of all estimated factors. Hence, in finding each approximate factor
$\tilde{f}_{i}$, EP uses other approximate factors
$q^{\backslash i}(\theta):=\prod_{j\neq i}\tilde{f}_{j}(X|\theta)$ as a
context.

Given that $X$ is observed to be $X_{0}$, EP iteratively refines
$\tilde{f}_{i}$ for each $i$ with the following update

$$\begin{aligned}
q(\theta) & =\arg\min_{q}KL\left(f_{i}(X_{0}|\theta)q^{\backslash i}(\theta)\,\|\, q(\theta)\right)\\
 & =\arg\min_{q}\int d\theta\, f_{i}(X_{0}|\theta)q^{\backslash i}(\theta)\log\left(\frac{f_{i}(X_{0}|\theta)q^{\backslash i}(\theta)}{q(\theta)}\right).\end{aligned}$$

For notational convenience, define $\text{proj}\left[\cdot\right]$
operator as
$$\text{proj}\left[p\right]=\arg\min_{q}KL\left(p\,\|\, q\right)$$ where
$q$ takes a prespecified form in the exponential family. Since
$q(\theta)=q^{\backslash i}(\theta)\tilde{f}_{i}(X_{0}|\theta)$, the
update for each $\tilde{f}_{i}$ is given by
$$\tilde{f}_{i}=\frac{\text{proj}\left[f_{i}(X_{0}|\theta)q^{\backslash i}(\theta)\right]}{q^{\backslash i}(\theta)}.$$
In the EP literature, $q^{\backslash i}$ is known as a **cavity
distribution **and $f_{i}(X_{0}|\theta)q^{\backslash i}(\theta)$ is
known as **tilted distribution**.** **Each factor $f_{i}$ is known as a
**site**.

#### Why $\tilde{f}_{i}\in\text{ExpFam}$ ?

The main reason to require $q$ to be in the exponential family is to
make the KL minimization easy. Assume $q$ is in the exponential family,
$$q(\theta)=h(\theta)g(\eta)\exp\left(\eta^{\top}u(\theta)\right)$$
where $u(\theta)$ is the **sufficient statistic **of $q$ and $\eta$ is
the **natural parameter**. It can be shown (by expanding the definition
of KL divergence, taking the derivative with respect to $\eta$, and
setting it to 0) that $q^{*}=\arg\min_{q}KL(p\,\|\, q)$ is the one such
that
$$\mathbb{E}_{q^{*}(\theta)}\left[u(\theta)\right]=\mathbb{E}_{p(\theta)}\left[u(\theta)\right].$$
That is, the projection of $p$ onto the exponential family is given by
the exponential family distribution $q^{*}$ that has the same moment
parameters as the moments under $p$. This procedure is known as **moment
matching**. For example, if $q$ is chosen to be a Gaussian, then
$u(\theta)=\left(\theta,\theta^{2}\right)^{\top}$. So the projection of
$p$ amounts to finding a Gaussian $q$ that has the same first two
moments.

If each $\tilde{f}_{i}$ is in the exponential family, then $q$ is also
in the exponential family as the family is close under multiplication
and division. Division of two exponential family distributions amounts
to subtraction of their natural parameters followed by a
renormalization.

#### Message View of EP

Besides factor-based treatment, one can view EP as a message passing
algorithm by considering the following changes.

1.  The cavity $q^{\backslash i}$ can be thought of as a message
    carrying information about $\theta$ to the factor $i$. We denote it
    by $m_{\theta\rightarrow f_{i}}(\theta)$.
2.  $\tilde{f}_{i}$ can be treated as a message from
    $f_{i}(X_{0}|\theta)$ to $\theta$. We denote it by
    $m_{f_{i}\rightarrow\theta}(\theta)$.
3.  In the KL objective, one can replace $f_{i}(X_{0}|\theta)$ with
    $\int dX\, m_{X\rightarrow f_{i}}(X)f_{i}(X|\theta)$ where
    $m_{X\rightarrow f_{i}}(X):=\delta(X-X_{0})$ is a message from $X$
    carrying information about $X$ to the factor $f_{i}$. In this case,
    it indicates that the distribution of $X$ is a point mass at
    $X_{0}$. In general, the observed evidence does not have to be an
    exact value. We may, say, observe that $X$ is non-negative which
    gives $m_{X\rightarrow f_{i}}(X)=p(X|X>0)$.

With these changes, the factor update can be rewritten as

$$m_{f_{i}\rightarrow\theta}(\theta)=\frac{\text{proj}\left[\int dX\, f(X|\theta)m_{X\rightarrow f_{i}}(X)m_{\theta\rightarrow f_{i}}(\theta)\right]}{m_{\theta\rightarrow f_{i}}(\theta)}.\label{eq:ep_msg_update}$$

The estimated posterior then becomes
$q(\theta)=\prod_{i=1}^{m}m_{f_{i}\rightarrow\theta}(\theta)$. For
comparison purpose, a belief propagation (BP) message from $f_{i}$ to
$\theta$ is
$$m_{f_{i}\rightarrow\theta}(\theta)=\int dX\, f(X|\theta)m_{X\rightarrow f_{i}}(X).$$
Two notable differences between EP and BP are

1.  In BP, no projection is involved in computing a message.
2.  In BP, to send a message from $f_{i}$ to $\theta$, there is no need
    to gather a message from $\theta$ to $f_{i}$. EP needs it to compute
    an outgoing message to give a context for the global posterior and
    then divide it out after the projection.

#### General EP Messages

Let $f$ be a factor and
$\mathcal{V}(f)=\left\{ v_{1}^{f},\ldots,v_{D}^{f}\right\} $ be the set
of variables connected to $f$. In general, an EP message from $f$ to a
variable $v'\in\mathcal{V}(f)$ takes the following form

$$m_{f\rightarrow v'}(v')=\frac{\text{proj}\left[\int d\mathcal{V}\backslash\{v'\}\, f(\mathcal{V})\prod_{v\in\mathcal{V}(f)}m_{v\rightarrow f}(v)\right]}{m_{v'\rightarrow f}(v')}\label{eq:ep_msg_update_general}$$

where $\int d\mathcal{V}\backslash\{v'\}$ denotes an integral over all
variables except $v'$. In the previous example,
$\mathcal{V}(f)=\{X,\theta\}$. Note that the division is easy to carry
out since both numerator and denominator messages are in the exponential
family.

#### EP Update Sequence

As $X=X_{0}$, we will sometimes drop $X_{0}$ (constant) from
$\tilde{f}_{i}$.

-   $q(\theta)=\mathcal{N}(\theta|m_{0},v_{0})$ (prior)
-   $m_{f_{i}\rightarrow\theta}(\theta)=\tilde{f}_{i}(\theta)=1$ for all
    $i$
-   Repeat EP iterations until convergence (make several passes over
    $1,\ldots,m$)
    -   for each factor $i=1\ldots,m$
        -   **Deletion**:
            $q^{\backslash i}(\theta)\propto q(\theta)/m_{f_{i}\rightarrow\theta}(\theta)=\prod_{j\neq i}\tilde{f}_{j}(\theta)$
        -   **Inclusion**: Compute
            $q(\theta)=\text{proj}\left[f_{i}(X|\theta)q^{\backslash i}(\theta)\right]$
        -   **Update**:
            $m_{f_{i}\rightarrow\theta}(\theta)=\tilde{f}_{i}(\theta)=q(\theta)/q^{\backslash i}(\theta)$

$q(\theta)$ is the posterior of the latent $\theta$ that we are after.

