Title: Equivalent Properties of a Linear Operator
Tags: linear, operator
Date: 2013-10-24
Slug: props_linear_operators



This is a summary of material from the course ``Advanced topics in
machine learning'' by Arthur Gretton with slightly more intermediate
steps. 

**Theorem**
Let $\left(\mathcal{F},\|\cdot\|_{\mathcal{F}}\right)$ and $\left(\mathcal{G},\|\cdot\|_{\mathcal{G}}\right)$
be normed linear spaces. If $L:\mathcal{F}\mapsto\mathcal{G}$ is
a linear operator, then the following three conditions are equivalent. 

* $L$ is a bounded operator.
* $L$ is continuous on $\mathcal{F}$.
* $L$ is continuous at one point of $\mathcal{F}$.

**Proof**
Equivalence of these conditions can be proved by proving $1\Rightarrow2,2\Rightarrow3$
and $3\Rightarrow1$.

Firstly we prove $1\Rightarrow2$. Assume $L$ is bounded. Then by
definition of a bounded operator, for all $f\in\mathcal{F}$, $\|Lf\|_{\mathcal{G}}\leq\|L\|\|f\|_{\mathcal{F}}$,
where $\|L\|$ is the operator norm. Set $f:=f_{1}-f_{2}$. So, we
have $\|L\left(f_{1}-f_{2}\right)\|_{\mathcal{G}}\leq\|L\|\|f_{1}-f_{2}\|_{\mathcal{F}}$
which is the definition of Lipschitz continuity with Lipschitz constant
$\|L\|$. Since Lipschitz continuity implies continuity, $1\Rightarrow2$
holds.

The implication from 2 to 3 is obvious since by definition an operator
is continuous if it is continuous at every point.

Proving $3\Rightarrow1$ is a bit tricky. Let us recall the definition
of continuity. An operator is said to be continuous at $f_{0}\in\mathcal{F}$
if for all $\epsilon>0$, there exists $\delta(\epsilon,f_{0})>0$
such that for all $f\in\mathcal{F}$, we have 
$$\|f-f_{0}\|_{\mathcal{F}}<\delta\Rightarrow\|Lf-Lf_{0}\|_{\mathcal{G}}<\epsilon.$$ 

Assume $L$ is continuous at $f_{0}$. Then, for $\epsilon=1$, there
exists $\delta>0$, such that $\|\left(f_{0}+\Delta\right)-f_{0}\|_{\mathcal{F}}=\|\Delta\|_{\mathcal{F}}\leq\delta$
for any $\Delta$ implies $\|L\left(f_{0}+\Delta\right)-Lf_{0}\|_{\mathcal{G}}=\|L\Delta\|\leq\epsilon=1$.
Here $f$ in the definition of continuity is set to $f_{0}+\Delta$,
and $\epsilon$ is chosen to be 1. Now we try to show that $L$ is
bounded.

$$\begin{eqnarray*}
\|Lf\|_{\mathcal{G}} & = & \frac{\delta}{\delta}\frac{\|f\|_{\mathcal{F}}}{\|f\|_{\mathcal{F}}}\|Lf\|_{\mathcal{G}}=\frac{1}{\delta}\|f\|_{\mathcal{F}}\left\Vert \frac{\delta}{\|f\|_{\mathcal{F}}}L\left(f\right)\right\Vert _{\mathcal{G}}\\
 & = & \frac{1}{\delta}\|f\|_{\mathcal{F}}\left\Vert L\left(\frac{\delta}{\|f\|_{\mathcal{F}}}f\right)\right\Vert _{\mathcal{G}}
\end{eqnarray*}$$

Here we used the fact that $L$ is linear. Since $\left\Vert \frac{\delta}{\|f\|_{\mathcal{F}}}f\right\Vert _{\mathcal{F}}=\delta$,
if we set $\Delta=\frac{\delta}{\|f\|_{\mathcal{F}}}f$, then we have
$\|\Delta\|_{\mathcal{F}}\leq\delta$. So,

$$\begin{align*}
\left\Vert Lf\right\Vert _{\mathcal{G}} & =\frac{1}{\delta}\|f\|_{\mathcal{F}}\left\Vert L\Delta\right\Vert _{\mathcal{G}}\\
 & \leq\frac{1}{\delta}\|f\|_{\mathcal{F}}.
\end{align*}$$
where we used the fact that $\left\Vert L\Delta\right\Vert \leq1$.
Since $f$ is arbitrary, we have the definition of a bounded operator
with operator norm $\|L\|=\frac{1}{\delta}$.
