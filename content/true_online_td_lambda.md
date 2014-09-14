Title: True Online TD$(\lambda)$
Date: 2014-09-14 10:05:00
Tags: reinforcement learning, td, online
Slug: true_online_td_lambda

This post contains a summary of the
[paper](http://jmlr.org/proceedings/papers/v32/seijen14.html) titled
“True Online TD$(\lambda)$” appearing in ICML 2014.

Classical TD$(\lambda)$ 
------------------------

TD$(\lambda)$ is a core model-free algorithm in reinforcement learning
for estimating a value function. Let $\hat{v}_{t}(S_{t})$ be the
estimated value at time $t$ of state $S_{t}$. Often a stochastic
gradient descent-like update of the following form is used
$$\theta_{t+1}=\theta_{t}+\alpha\left(U_{t}-\hat{v}_{t}(S_{t})\right)\nabla_{\theta_{t}}\hat{v}_{t}(S_{t})$$
where $\theta$ is the parameter of $\hat{v}$ to estimate, $U_{t}$
denotes an update target, and $\nabla_{\theta_{t}}\hat{v}_{t}(S_{t})$ is
the derivative of $\hat{v}$ with respect to $\theta_{t}$. By definition,
the value of a state $s$ is the total expected sum of discounted future
rewards starting from state $s$. In math,
$$v(s)=\mathbb{E}\left[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\cdots\mid S_{t}=s\right].$$
A sensible and unbiased estimate for this expectation is given by an
observed trajectory of rewards
$U_{t}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\cdots$ starting from
state $s$. This choice of update target is called Monte Carlo update.
Note that it cannot be used online since the target depends on the
future. So one has to wait until the end of an episode first. Then, come
back and update each time step.

A popular update target $U_{t}$ meant to be an online version of Monte
Carlo update is given by TD$(0)$ which comes from the fact that

$$\begin{aligned}
v(s) & = & \mathbb{E}\left[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\cdots\mid S_{t}=s\right]\\
 & = & \mathbb{E}\left[R_{t+1}+\gamma v(S_{t+1})\mid S_{t}=s\right].\end{aligned}$$

TD(0) approximates the quantity with one realization of the term in the
expectation. That is, $$U_{t}=R_{t+1}+\gamma\hat{v}_{t}(S_{t+1}).$$ This
update can be used online as it depends only the reward of one time step
ahead of current time $t$. Now of course one can follow the same trick
by doing

$$\begin{aligned}
\mathbb{E}\left[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\cdots\mid S_{t}=s\right] & = & \mathbb{E}\left[R_{t+1}+\gamma R_{t+2}+\gamma^{2}v(S_{t+2})\mid S_{t}=s\right]\end{aligned}$$

and use $U_{t}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}v(S_{t+2})$. This target
is called a 2-step return. The previous TD(0) target is called 1-step
return. From this, one can obviously define an $n$-step return from time
$t$ as
$$G_{\theta}^{(n)}(t):=\left(\sum_{i=1}^{n}\gamma^{i-1}R_{t+i}\right)+\gamma^{n}\theta^{\top}\phi_{t+n}$$
where we will assume that $\hat{v}(S_{t})=\theta^{\top}\phi(S_{t})$ for
basis function $\phi$ and $\phi_{t}:=\phi(S_{t})$. This leads to the
question: “Which $n$ do we use ?”. One answer is that we use all of them
by geometrically weighting all $n$-returns. This combined returns are
referred to as $\lambda$-return
$$L_{\theta}^{\lambda}(t):=\left(1-\lambda\right)\sum_{n=1}^{\infty}\lambda^{n-1}G_{\theta}^{(n)}(t)$$
where $\lambda\in[0,1]$. If $\lambda=0$,
$L_{\theta}^{\lambda}(t)=R_{t+1}+\gamma\hat{v}_{t}(S_{t+1})$ giving back
TD(0) update target. If $\lambda=1$, the $\lambda$-return is equivalent
to Monto Carlo update target. Hence, $\lambda$-return provides a smooth
blend between TD(0) and Monte Carlo update parametrized by $\lambda$.

Forward and Backward TD$(\lambda)$ 
-----------------------------------

Updating $\theta$ with
$$\theta_{t+1}=\theta_{t}+\alpha\left(L_{\theta}^{\lambda}(t)-\hat{v}(S_{t})\right)\phi_{t}$$
is referred to as forward-view TD$(\lambda)$ which is not online since,
like Monte Carlo update, $L_{\theta}^{\lambda}$ depends on the rewards
in the future. Interestingly, an equivalent way to update $\theta$ in an
online way using $L_{\theta}^{\lambda}$ exists. This is called
backward-view TD$(\lambda)$,

$$\begin{aligned}
\text{(TD error) }\delta_{t} & = & R_{t+1}+\gamma\overbrace{\theta_{t}^{\top}\phi_{t+1}}^{\hat{v}_{t}(S_{t+1})}-\overbrace{\theta_{t}^{\top}\phi_{t}}^{\hat{v}_{t}(S_{t})}\\
\boldsymbol{e}_{t} & = & \gamma\lambda\boldsymbol{e}_{t-1}+\alpha\phi_{t}\\
\theta_{t+1} & = & \theta_{t}+\delta_{t}\boldsymbol{e}_{t}\end{aligned}$$

where $\boldsymbol{e}_{t}$ is called eligibility traces containing
footprints of recently visited states and
$\boldsymbol{e}_{0}=\boldsymbol{0}$. Instead of updating $\theta_{t+1}$
toward $\phi_{t}$ weighted by some quantity, here we update
$\theta_{t+1}$ towards $\boldsymbol{e}_{t}$ which accumulates many
visited states in the past, weighted down exponentially by
$\gamma\lambda$. Essentially if the agent is highly rewarded in a state
$s'$, not only the preceding state $s$ leading to $s'$ that is credited,
but all previous states leading to $s$ are also given credits (although
exponentially less because of $\gamma\lambda$ factor). The following is
a well-known result.

**Theorem. **The sum of **offline** updates is identical for
forward-view and backward-view TD$(\lambda)$
$$\sum_{t=1}^{T}\delta_{t}\boldsymbol{e}_{t}=\sum_{t=1}^{T}\alpha\left(L_{\theta}^{\lambda}(t)-\hat{v}(S_{t})\right)\phi_{t}$$
where $T$ is the last time step in the episode.

Although interesting, the two views are not equivalent for online
updates (only approximatedly equal).

Idea of the paper
-----------------

The paper proposes a $\lambda$-return called truncated $\lambda$-return
which is basically like the classical $\lambda$-return except that it is
truncated at the current time step. This gives rise to a new
forward-view and backward-view TD$(\lambda)$ which they call true online
TD$(\lambda)$. It is called so because of the following theorem given in
the paper.

**Theorem. **$\theta_{t}$ from backward update is exactly equal to
$\theta_{t,t}$ from forward update for all $t$.

The new backward-view update equations are

$$\begin{aligned}
\delta_{t}&=&R_{t+1}+\gamma\theta_{t}^{\top}\phi_{t+1}-\theta_{t-1}^{\top}\phi_{t}\\
\boldsymbol{e}_{t}&=&\gamma\lambda\boldsymbol{e}_{t-1}+\alpha_{t}\phi_{t} -\alpha_{t}\gamma\lambda\left(\boldsymbol{e}_{t-1}^{\top}\phi_{t}\right)\phi_{t}\\
\theta_{t+1}&=&\theta_{t}+\delta_{t}\boldsymbol{e}_{t} +\alpha_{t}\left(\theta_{t-1}^{\top}\phi_{t}-\theta_{t}^{\top}\phi_{t}\right)\phi_{t}.\end{aligned}$$
