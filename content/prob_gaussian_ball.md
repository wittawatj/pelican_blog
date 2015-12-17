Title: $p(\|x\|_2 < R)$ when $x$ follows a normal distribution
Date: 2015-12-17
Tags: probability, gaussian
Slug: prob_gaussian_ball


A friend of mine recently asked 

> What is the value of $p(\|x\|_{2}<R)$ where $x\sim\mathcal{N}(0,\Sigma)$ and
> $x\in\mathbb{R}^{D}$? 

The question is not as easy as it looks. Although I did not get the answer,
I arrived at some expression which is close to the goal. Before I show
what I did, here is one result we will need.

-   If $z^{2}\sim\chi^{2}(d)$ and $v$ is a positive constant, then
    $vz^{2}\sim\mathrm{Gamma}(\frac{d}{2},2v)$ (shape-scale
    parameterization).

Here is what I did. Note that
$p(\|x\|_{2}<R)=p(x^{\top}x<R^2) $. The goal here is to find the CDF of
$x^{\top}x$.
Start by eigen-decomposing $\Sigma=UVU^{\top}$.  Let $y:=U^{\top}x$. It follows that
$x^{\top}x=y^{\top}y=\sum_{i=1}^{D}y_{i}^{2}$ because $U$ is an
orthogonal matrix. So, $p(x^{\top}x<R^2)=p(y^{\top}y<R^2)$ . From the
property of the normal distribution, we know that
$y=U^{\top}x\sim\mathcal{N}(0,V)$. Equivalently,
$y_{i}\sim\mathcal{N}(0,v_{i})$ where $v_{i}:=V_{ii}$. Let
$z\sim\mathcal{N}(0,1)$ be the standard normal random variable. We can
rewrite $y_{i}$ as $y_{i}=\sqrt{v_{i}}z$, and so $y_{i}^{2}=v_{i}z^{2}$,
where $z^{2}\sim\chi^{2}(1)$, the Chi-squared distribution with one
degree of freedom. From the previous result, we have
$y_{i}^{2}\sim\mathrm{Gamma}(\frac{1}{2},2v_{i})$. This implies that the
CDF of $y^{\top}y$ is the same as the CDF of a sum of independent Gamma
random variables. According to [Covo and Elalouf,
2014](https://projecteuclid.org/euclid.ejs/1403812157) and
[Moschopoulos,
1985](https://www.researchgate.net/publication/225242960_The_Distribution_of_the_Sum_of_Independent_Gamma_Random_Variables),
the CDF is not trivial to compute.
