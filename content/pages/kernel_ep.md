Title:  Kernel-Based Just-In-Time Learning for Passing Expectation Propagation Messages
Slug: kernel_ep

The goal of this project is to learn a kernel-based message operator which
takes as input all incoming messages to a factor and produces a projected
outgoing expectation propagation (EP) message. In ordinary EP, computing an
outgoing message may involve solving a difficult integral for minimizing the KL
divergence between the tilted distribution and the approximate posterior. Such
operator allows one to bypass the computation of the integral by directly
mapping all incoming messages into an outgoing message. Learning of such an
operator is done online during EP.  The operator is termed **KJIT** for
**K**ernel-based **J**ust-**I**n-**T**ime learning for passing EP messages.


Short description of the project can be found in [our
poster](files/kjit_dali2015_poster.pdf) or this [presentation slides](files/slides/kjit_ep_research.pdf). 
Full details are in our [UAI 2015 paper](http://auai.org/uai2015/proceedings/papers/235.pdf).
Supplementary matrial is [here](http://auai.org/uai2015/proceedings/supp/239_supp.pdf).

    Wittawat Jitkrittum, Arthur Gretton, Nicolas Heess, 
    S. M. Ali Eslami, Balaji Lakshminarayanan, Dino Sejdinovic, and Zoltan Szabo
    "Kernel-Based Just-In-Time Learning for Passing Expectation Propagation Messages"
    arXiv:1503.02551, 2015

## Code 
All the code is available on the project's [github
page](https://github.com/wittawatj/kernel-ep).
