Title: Compactness and Open Sets in $\mathbb{R}^{d}$
Date: 2014-06-29
Tags: topology, compactness
Slug: compactness_open_sets 


I read the appendix of [Support Vector Machines book](http://www.amazon.co.uk/Support-Machines-Information-Science-Statistics/dp/0387772413) 
on the other day and wondered about how we can show that an open set
in $\mathbb{R}^{d}$ is not compact. Let me start by giving the definition
of compactness and a related theorem. These are from the book.

**Definition** A set $A$ in a topological space is *compact*
if for every family $(O_{i})_{i\in I}$ of open sets with $A\subset\cup_{i\in I}O_{i}$,
there exist finitely many indexes $i_{1},\ldots,i_{n}\in I$ with
$A\subset\cup_{j=1}^{n}O_{i_{j}}$. In other words, $A$ is compact
if each of its open covers has a finite subcover (from this [Wiki page](http://en.wikipedia.org/wiki/Compact_space)).

**Theorem** $A\subset\mathbb{R}^{d}$ is compact if and only
if $A$ is closed and bounded.

Here is what I wondered after reading these two items. Consider an
open unit sphere $S=\left\{ x\mid\|x\|<1\right\} $ in $\mathbb{R}^{d}$.
Obviously by the theorem $S$ is not compact because it is not closed.
That means there must exist an open cover such that there is no finite
subcover. What kind of open cover is that ? That is my question.

I got my answer after discussing with [Zoltan](http://www.gatsby.ucl.ac.uk/~szabo/).
What we need are two things. Firstly, we need to find open covers
$\{O_{i}\}_{i=1}^{\infty}$ that can cover $S$ i.e., $S\subseteq\cup_{i=1}^{\infty}O_{i}$.
Secondly, show that no finite number of $\{O_{i}\}_{i}$ can cover
$S$. 

Define $O_{i}=S_{r_{i}}$ where $S_{r}=\left\{ x\mid\|x\|<r\right\} $
and $(r_{i})_{i}$ is a monotonically increasing sequence converging
to 1 with $r_{i}<1$ for all $i$. No finite number of $\{O_{i}\}_{i}$
will cover $S$ because $\cup_{j\in J}O_{j}=S_{\max\left(\left\{ r_{j}\mid j\in J\right\} \right)}$
for any finite index set $J$ and $S_{\max\left(\left\{ r_{j}\mid j\in J\right\} \right)}\subsetneq S$.
To show $S\subseteq\cup_{i=1}^{\infty}O_{i}$, we need to show that
for all $p\in S,p\in\cup_{i=1}^{\infty}O_{i}$. This is equivalent
to: for all $p\in S$, there always exists an open set $O_{R}\ni p$
for some $R$. The latter statement holds since the open cover sphere
can grow to any radius $<1$.

