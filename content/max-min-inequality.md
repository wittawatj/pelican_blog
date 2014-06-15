Title: Max-Min Inequality
Date: 2014-05-26
Tags: inequality, max-min
Slug: max_min_inequality

The max-min inequality states that 
$$
\sup_{y}\inf_{x}f(x,y)\leq\inf_{x}\sup_{y}f(x,y).
$$
At first glance, it is not clear why swapping the order of $\sup$
and $\inf$ will make any difference. Here is an example taken from [a math exchange page](http://math.stackexchange.com/questions/186697/max-min-of-function-less-than-min-max-of-function)
which will make it clear. Suppose $f(x,y)=\sin(x+y)$. Then $\inf_{x}\sin(x+y)=-1$
and $\sup_{y}\sin(x+y)=1$. Clearly, 
$$
\sup_{y}-1\leq\inf_{x}1
$$
holds. 

The proof for general case relies on the following inequality:
$$
\inf_{x'}f(x',y)\leq\sup_{y'}f(x,y')
$$
for all $x,y$. This is certainly true because any setting of $y$
will not yield a value larger than $y'$ such that $f$ achieves its
maximum. Likewise any setting of $x$ will not give a value smaller
than $x'$ such that $f$ achieves its minimum. Since the inequality
holds for **any** $x$ and $y$, it must hold for $x$ such that
the right hand side achieves its minimum and for $y$ such that the
left hand side achieves its maximum. Hence,
$$
\sup_{y}\inf_{x'}f(x',y)\leq\inf_{x}\sup_{y'}f(x,y').
$$

