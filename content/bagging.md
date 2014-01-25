Title: Bagging
Date: 2013-07-04 
Category: ml
Tags: bagging
Author: Wittawat Jitkrittum

Bootstrap Aggregating (Bagging) is an idea aimed to reduce the variance of a prediction by averaging many predictions. This is accomplished simply by uniformly sampling (with replacement) from the original sample to generate $m$ datasets, and training $m$ models. At the prediction phase, the predicted value is the average of the $m$ models. A more elaborated explanation is as follows. 

Given a sample $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^n \overset{\text{i.i.d.}}{\sim} P_{x,y}$, the goal of a regression task is to estimate $f(x)$ given $x$ where $f$ is unknown. Let $Y$ be the estimate of $f(x)$ which may be based on a model. Assume that $\mathbb{E}[Y|X=x] = f(x)$ i.e., the estimator is unbiased. Under a square-loss error function, the expected prediction error of $x$ is 

$\mathbb{E}_{Y|X}[( Y - \mathbb{E}[Y|X=x])^2] = \mathbb{V}[Y|X=x]$

Now, consider the case where we can draw $m$ independent samples $\mathcal{D}_1, \ldots, \mathcal{D}_m$ from $P_{x,y}$. We similarly denote $Y_1, \ldots, Y_m$ to be the predicted value from each of the $m$ models given $x$, and let $Z = \frac{1}{m} \sum_{i=1}^m Y_i$ i.e., average of the predicted values. It can be shown that $Z$ is also unbiased just like $Y$. That is, 

$\mathbb{E}[Z | X=x] = \frac{1}{m} \sum_{i=1}^m \mathbb{E}[Y_i|X=x] = f(x)$

As for the prediction error on $x$, we have

$$\begin{align*}
\mathbb{V}[Z | X=x] &= \mathbb{V}[\frac{1}{m} \sum_{i=1}^m Y_i | X=x] \nonumber \\ 
 &= \frac{1}{m^2} \mathbb{V}[\sum_{i=1}^m Y_i | X=x]  \nonumber \\  
 &= \frac{1}{m} \mathbb{V}[Y | X=x]   \label{eq:bagging_variance}
\end{align*}$$

where we have used the fact that $Y_i$ and $Y_j$ are independent (so $\text{Cov}[Y_i, Y_j] = 0$) since $\mathcal{D}_i$ and $\mathcal{D}_j$ are independent. It is interesting to see that by drawing more samples, we can reduce the prediction error as much as we want. Of course, in reality we have only one sample $\mathcal{D}$. The way bagging proceeds is to approximate the operation of independent drawings of $m$ samples from $P$ by uniformly sampling with replacement from $\mathcal{D}$ instead. 

## Caveat of Bagging ?

Here is my opinion. Sampling from the same fixed sample breaks the analysis given previously as $\mathcal{D}_i$ and $\mathcal{D}_j$ are no longer independent. As a result $Y_i$ and $Y_j$ are also not independent. So, it is possible that $\text{Cov}[Y_i, Y_j] \neq 0$ and we may not be guaranteed to have a reduced prediction error ? 

Source: [Bagging by *mathematicalmonk* on Youtube](https://www.youtube.com/watch?v=5Lu1eTiX7qM)
