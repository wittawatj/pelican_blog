Title: Expectation Particle Belief Propagation
Date: 2015-06-28
Tags: ep, bp, particle
Slug: epbp


This post summarizes

    Expectation Particle Belief Propagation (2015)
    Thibaut Lienart, Yee Whye Teh, Arnaud Doucet
    arXiv:1506.05934

The [paper](http://arxiv.org/abs/1506.05934) proposes an update scheme
for the proposal distribution in the message computation of [particle
belief
propagation](http://ttic.uchicago.edu/~dmcallester/aistats09.pdf). The
proposal distribution is in the exponential family and is iteratively
updated in an expectation propgation (EP) framework. The computation at
each iteration is quadratic in the number of particles.

Particle Belief Propagation {.unnumbered}
---------------------------

Let $\psi_{u}$ and $\psi_{uv}$ be node and edge potentials,
respectively. Let $\Gamma_{u}$ be the set of neighbouring variables
connected to node $u$. The loopy belief propagation (LBP) message
updates are written as

$$\begin{aligned}
m_{uv}^{t}(x_{v}) & =\int\psi_{uv}(x_{u},x_{v})\psi_{u}(x_{u})\prod_{w\in\Gamma_{u}\backslash v}m_{wu}^{t-1}(x_{u})\,\mathrm{d}x_{u},\\
B_{u}^{t}(x_{u}) & =\psi_{u}(x_{u})\prod_{w\in\Gamma_{u}}m_{wu}^{t}(x_{u}),\end{aligned}$$

where the superscript $\cdot^{t}$ denotes iteration number, $B_{u}$
denotes the belief at node $u$, and $m_{uv}$ is the message from node
$u$ to node $v$. Particle belief propgation (PBP) uses importance
sampling to compute the messages $m_{uv}$. Given a proposal distribution
$q_{u}$ on node $u$, and a set of $N$ particles
$\{x_{u}^{(i)}\}_{i=1}^{N}\sim q_{u}(x_{u})$, PBP messages
$\hat{m}_{uv}^{\mathrm{PBP}}$ are written as:

$$\begin{aligned}
 & \int\psi_{uv}(x_{u},x_{v})\psi_{u}(x_{u})\prod_{w\in\Gamma_{u}\backslash v}m_{wu}^{t-1}(x_{u})\,\mathrm{d}x_{u}\\
 & =\int\psi_{uv}(x_{u},x_{v})\psi_{u}(x_{u})\prod_{w\in\Gamma_{u}\backslash v}m_{wu}^{t-1}(x_{u})\frac{q_{u}(x_{u})}{q_{u}(x_{u})}\,\mathrm{d}x_{u}\\
 & =\frac{1}{N}\sum_{i=1}^{N}\psi_{uv}(x_{u}^{(i)},x_{v})\frac{\psi_{u}(x_{u}^{(i)})}{q_{u}(x_{u}^{(i)})}\prod_{w\in\Gamma_{u}\backslash v}m_{wu}^{t-1}(x_{u}^{(i)})\\
 & :=\sum_{i=1}^{N}\psi_{uv}(x_{u}^{(i)},x_{v})w_{uv}^{(i)}=:\hat{m}_{uv}^{\mathrm{PBP}}(x_{v}),\end{aligned}$$

where the importance weight
$w_{uv}^{(i)}:=\frac{1}{N}\frac{\psi_{u}(x_{u}^{(i)})}{q_{u}(x_{u}^{(i)})}\prod_{w\in\Gamma_{u}\backslash v}m_{wu}^{t-1}(x_{u}^{(i)})$.
The choice of $q_{u}$ determines the approximation quality.

Expectation Particle Belief Propagation {.unnumbered}
---------------------------------------

Let $\hat{m}_{uv}(x_{v})$ be the particle approximation of the exact
message $m_{uv}$. The particle approximation to the belief at node $v$
is

$$\begin{aligned}
\hat{B}_{u}(x_{u}) & \approx\frac{1}{N}\sum_{i=1}^{N}\frac{\psi_{u}(x_{u}^{(i)})\prod_{w\in\Gamma_{u}}\hat{m}_{wu}(x_{u}^{(i)})}{q_{u}(x_{u}^{(i)})}\delta_{x_{u}^{(i)}}(x_{u}),\end{aligned}$$

where $\delta_{x}$ is a delta measure at $x$. It can be seen that the
best proposal $q_{u}$ is the belief itself, which is unknown. An idea to
approximately achieve that is to use a tractable exponential family
distribution for $q_{u}$ instead:
$$q_{u}(x_{u})\propto\eta_{u}(x_{u})\prod_{w\in\Gamma_{U}}\eta_{wu}(x_{u}),$$
where $\eta_{u}$ and $\eta_{wu}$ are exponential family approximations
of $\psi_{u}$ and $\hat{m}_{wu}$ respectively. The exponential family
distribution for $q_{u}$ is computed with EP. Specifically, each
$\eta_{wu}$ is iteratively updated with
$$\eta_{wu}=\arg \min_{\eta\in\mathrm{ExpFam}}\mathrm{KL}\left[\hat{m}_{wu}(x_{u})q_{u}^{\backslash w}(x_{u})\,\big\|\,\eta(x_{u})q_{u}^{\backslash w}(x_{u})\right],$$
where the cavity distribution
$q_{u}^{\backslash w}\propto q_{u}/\eta_{wu}$. It is known that the
solution $\eta_{wu}$ is the one such that the moments (expected
sufficient statistics) of the tilted distribution
$\hat{m}_{wu}q_{u}^{\backslash w}$ match that of
$\eta q_{u}^{\backslash w}$. The computation of moments can be performed
crudely as $q_{u}$ is only used as a proposal distribution.

It is unclear if this scheme will work in the case that $q_{u}$ is high
dimensional.
