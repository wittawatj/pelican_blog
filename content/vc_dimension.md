Title: VC Dimension
Date: 2013-07-09
Slug: vc_dimension
Tags: vc, learning


In learning theory, the [VC dimension](https://en.wikipedia.org/wiki/VC_dimension) is a measure of 
capacity of a class of hypotheses $\mathcal{H}$ (e.g., a set of classifiers). This notion of 
capacity indicates how complicated $\mathcal{H}$ is. Although complicated $\mathcal{H}$ may be able
to fit well to the dataset at hand, yielding a low training error, there is a possibility that
it overfits and gives high generalization error. The VC dimension provides a tool to analyze
the generalization error of a class of hypotheses based on how complicated it is, independent
of the input distribution, the target function, and the learning algorithm (i.e., a systematic
approach to choose the best hypothesis $g \in \mathcal{H}$).

Capacity in VC theory is captured by the concept called *shattering*. Here we focus only on binary
classification problems.

<definition>
A hypothesis class $\mathcal{H}$ is said to **shatter** $n$ points if *there exists* a 
dataset $\boldsymbol{X} = \{x_1,\ldots, x_n\}$ such that
for any label assignment $\boldsymbol{y} = (y_1, \ldots, y_n)$ where $y_i \in \{-1, +1\}$, there exists 
a hypothesis $h \in \mathcal{H}$ which can produce $\boldsymbol{y} = h(\boldsymbol{X})$.
</definition>

In a simpler terms, we say $\mathcal{H}$ shatters $n$ points if **there exists** a configuration of
$\boldsymbol{X} = \{x_1,\ldots, x_n\}$ such that $\mathcal{H}$ can produce all possible $2^n$ 
assignments of $\boldsymbol{y}$. Things worth noting are

* If $\mathcal{H}$ can produce any assignment of $\boldsymbol{y}$ on just even one configuration of 
$n$ points, then we say $\mathcal{H}$ can shatter $n$ points. 
So, when constructing an example, it makes sense to imagine a configuration of points such that 
$\mathcal{H}$ can shatter easily.
* If $\mathcal{H}$ can shatter $n$ points, then obviously it can shatter less than $n$ points.
* Likewise, if $\mathcal{H}$ cannot shatter $n$ points, then it cannot shatter more than $n$ points.  


<definition>
The VC dimension of $\mathcal{H}$, denoted by $d_{VC}(\mathcal{H})$, is the largest number of points
$\mathcal{H}$ can shatter.
</definition>

As an example, the VC dimension of a linear classifier in two-dimensional space is 3. 
That is, three is the highest number of points a line can produce all possible $\{-1, +1\}$ assignments. 
With four points, there are two cases out of 16 possible assignments a line cannot produce. 
In general, $d_{VC}(\text{linear classifiers}) = d+1$ where $d$ is the input dimension.

The VC dimension can be used to bound probabilistically the difference between the training 
and test errors. This result is known as VC inequality.

**Source**: [Lectures by Professor Yaser Abu-Mostafa](http://work.caltech.edu/lectures.html). 

* Lecture 5 (Training versus Testing) 
* Lecture 6 (Theory of Generalization)
* Lecture 7 (The VC Dimension) 
