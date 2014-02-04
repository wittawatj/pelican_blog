Title: Viterbi Algorithm in HMM
Date: 31/12/2013
Slug: viterbi_hmm
Tags: hmm, probability


Viterbi algorithm in the context of a Hidden Markov Model (HMM) aims
to find the sequence of hidden states which gives the highest posterior
probability. Let $X=X_{1:T}$ (all observations from time 1 to time
$T$) be the observations and $Z=Z_{1:T}$ be the latent variables.
Viterbi algorithm solves the following problem

$$\begin{align*}
\max_{Z}p(Z|X) & \propto\max_{Z}p(X,Z)\\
 & =\max_{Z_{1:T}}p(z_{1})\prod_{i=1}^{T}p(x_{i}|z_{i})\prod_{i=2}^{T}p(z_{i}|z_{i-1})
\end{align*}$$

If each $Z_{i}$ have $K$ states, then we have totally $K^{T}$ possible
sequences to consider. Certainly it is computationally prohibitive
to enumerate each sequence, evaluate its probability and take the
maximal one. Instead, we want to take advantage of the chain structure
and design an efficient algorithm which incrementally finds the best
state for the next time point $t+1$ given the solution upto time
$t$. This is what the Viterbi algorithm does.

Consider the case where the chain has length 1 i.e., $T=1$. The problem
becomes


$$\max_{Z_{1}}p(z_{1})p(x_{1}|z_{1})$$

which can be solved straightforwardly by enumerating just $K$ possible
values of $Z_{1}$. 

With $T=2$, we have
$$\begin{align*}
\max_{Z}p(X,Z) & =\max_{Z_{1:2}}p(z_{1})p(x_{1}|z_{1})p(z_{2}|z_{1})p(x_{2}|z_{2})\\
 & =\max_{Z_{2}}p(x_{2}|z_{2})\overbrace{\max_{Z_{1}}p(z_{1})p(x_{1}|z_{1})p(z_{2}|z_{1})}^{\text{function of }Z_{2}}.
\end{align*}$$


For $T=3$, we have
$$\begin{align*}
\max_{Z}p(X,Z) & =\max_{Z_{1:3}}p(z_{1})p(x_{1}|z_{1})p(z_{2}|z_{1})p(x_{2}|z_{2})p(z_{3}|z_{2})p(x_{3}|z_{3})\\
 & =\max_{Z_{3}}p(x_{3}|z_{3})\underbrace{\max_{Z_{2}}p(x_{2}|z_{2})p(z_{3}|z_{2})\overbrace{\max_{Z_{1}}p(z_{1})p(x_{1}|z_{1})p(z_{2}|z_{1})}^{\text{function of }Z_{2}}}_{\text{function of }Z_{3}}.
\end{align*}$$
It can be seen that the solution to the case $T=3$ contains some
part which is exactly identical to the term in the solution for the
case $T=2$, namely $\overbrace{\max_{Z_{1}}p(z_{1})p(x_{1}|z_{1})p(z_{2}|z_{1})}^{\text{function of }Z_{2}}$.
This suggests that if we have the solution up to time $t$, solving
the problem up to time $t+1$ can be carried out by updating the solution.
Updating the solution is done through a function (actually a vector
of $K$ values) $m_{t}$. 

Define $m_{1}(k):=p(x_{1}|Z_{1}=k)p(Z_{1}=k)$. The solution to the
case $T=1$ is
$$\begin{align*}
\max_{Z_{1}}m_{1}(Z_{1}) & .
\end{align*}$$
If we define $m_{2}(k)$ as 
$$\begin{align*}
m_{2}(k) & :=p(x_{2}|Z_{2}=k)\max_{Z_{1}}m_{1}(Z_{1})p(Z_{2}=k|Z_{1}),
\end{align*}$$
then the solution to the case $T=2$ is $\max_{Z_{2}}m_{2}(Z_{2}).$
Following the same pattern, for $T=3$, we define $m_{3}$ as
$$\begin{align*}
m_{3}(k) & :=p(x_{3}|Z_{3}=k)\max_{Z_{2}}m_{2}(Z_{2})p(Z_{3}=k|Z_{2})
\end{align*}$$
and we have the solution to the case $T=3$ as $\max_{Z_{3}}m_{3}(Z_{3})$.
The problems written in terms of $m_{1},m_{2}$ and $m_{3}$ are exactly
the same as previously given in terms of conditional probabilities
alone.

In general, define $m_{t}(k)$ as 
$$\begin{eqnarray*}
m_{t}(k) & := & p(x_{t}|Z_{t}=k)\max_{z_{t-1}}m_{t-1}(z_{t-1})p(Z_{t}=k|z_{t-1})\\
m_{1}(k) & := & p(x_{1}|Z_{1}=k)p(Z_{1}=k).
\end{eqnarray*}$$
So the solution to our original problem is $\max_{Z_{T}}m_{T}(Z_{T})$.
Note that $m_{t}(k)$ can be interpreted as the maximum probability
among all possible sequences which end with $Z_{t}=k$. Obviously
the best sequence can be found by updating $m_{t}$ from $t=1$ to
$T$ and keep track of 


$$Z_{t}=\arg\max_{k}m_{t}(k).$$
