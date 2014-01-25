Title: Log-Sum-Exp Trick to Prevent Numerical Underflow
Date: 2013-07-16
Slug: log-sum_exp_underflow
Tags: underflow, probability


Multiplying a series of terms $p_1p_2\cdots p_n$ where $0 \leq p_i \leq 1$ can easily
result in a numerical underflow. This is especially the case when dealing with probabilistic
models which involve such multiplication all the time. One solution commonly used is to work
with the log of probabilities instead:

$\log p_1\cdots p_n = \sum_i \log p_i $,

which turns multiplication into a summation. Since a summation does not decrease the magnitude 
of the result, the underflow problem can be avoided.

Unfortunately, this little trick alone does not work when we have a sum of products of 
probabilities as in the case of, for example, the backward algorithm used in HMM:

$\beta_k(z_k) = \sum_{z_{k+1}} \beta_{k+1}(z_{k+1})  p(x_{k+1} ~|~ z_{k+1}) p(z_{k+1} ~|~ z_k) $.

The exact meaning of each term is irrelevant. What is important here is that as we successively
apply this recurrence relation (i.e., as $k$ gets lower), $\beta_k(z_k)$ will underflow. 
The solution here is the same as before. That is, we work with
$\log \beta_k(z_k)$ instead. So, by taking the $\log$ on both sides as well as putting $\exp \log$
in the sum, we have:

 
$\begin{align*}
\log \beta_k(z_k) &= \log \sum_{z_{k+1}} \exp \log \beta_{k+1}(z_{k+1})  p(x_{k+1} ~|~ z_{k+1}) p(z_{k+1} ~|~ z_k)\\
 &\rightarrow \log \sum_{i} \exp a_i.
\end{align*}$

The reason to apply $\exp \log$ on the RHS is to make the $\log$ version of  $\beta_{k+1}$ 
so the recurrence relation can be used. We have defined $a_i$ which absorbs the $\log$ term on 
the RHS. Note that typically $a_i \ll 0$. So we still have the underflow when calculating $\exp a_i$.
The remedy this time is to define

$b = \max_i a_i$,

and calculate $\log \exp(b) \sum_i \exp(a_i -b)$ instead.

$\begin{align*}
\log \sum_{i} \exp a_i &= \log \exp(b) \sum_i \exp(a_i -b) \\
 &= b + \log \sum_i \exp(a_i -b ) 
\end{align*}$ 

Since $b < 0$, $a_i - b$ is actually positive. So, underflow does not occur when computing $\exp(a_i -b)$. 
We have avoided the underflow problem by using the RHS of the last line.

## Soft-Max Function 

Just a side note, $\log \sum_i \exp a_i$ is called a *soft max* function because 

$\log \sum_i \exp a_i \approx \max_i a_i$. 

The approximation error tends to get larger as the magnitude of $a_i$ gets smaller, however.

Source: [(ML 14.10) Underflow and the log-sum-exp trick  by mathematicalmonk](https://www.youtube.com/watch?v=-RVM21Voo7Q)








