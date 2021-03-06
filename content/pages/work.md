Title: 
Slug: work


## Projects

* [Interpretable Two-Sample
  Test](https://github.com/wittawatj/interpretable-test) -- The goal of this
project is to learn a set of features to distinguish two given distributions P
and Q, as observed through two samples. This task is formulated as a two-sample
test problem. (05/2016)

* [Locally Linear Latent Variable Model
  (LL-LVM)](https://github.com/mijungi/lllvm) -- LL-LVM is a probabilistic
model for non-linear manifold discovery that describes a joint distribution
over observations, their manifold coordinates and locally linear maps
conditioned on a set of neighbourhood relationships. (09/2015)

* [Learning to Pass EP Messages](kernel_ep.html) -- In this project, we propose to learn a kernel-based message operator 
that replaces the multivariate integral required in classical EP to compute an outgoing message given incoming messages.
The operator allows fast computations of outgoing messages and can be updated online cheaply during EP inference. (03/2015)

* [$\ell_1$-LSMI](l1lsmi.html) -- A supervised feature selection algorithm based on a squared-loss variant of mutual information. 
Implementation is available in Matlab. (03/2013)

* [Classifier-based Thai Word Tokenizer](https://github.com/wittawatj/ctwt) --  Decision tree-based Java library to tokenize Thai text. The project was finished in two months for a competition. **Warning**: Not for production use. Detail is in this [presentation file](files/wordseg_dt.pdf). (02/2010)

* [JTCC](https://github.com/wittawatj/jtcc) -- Rule-based Java library to tokenize
  Thai text into a list of Thai Character Clusters (TCC). See [its github page](https://github.com/wittawatj/jtcc)
  for details. (03/2010)


## Publications

<!--should check http://nipg.inf.elte.hu/publications-embedded/2.html-->
<!--for a table of publications-->

<!--CSS style for publications -->
<style>
#publications dl {

}
#publications dd a {
    color: #0000aa;
}

.publications .author_list{

}

.publications .links a{
    margin-right: 5px;
    margin-left: 5px;

}

.publications {
    padding-left: 1em;
}

.publications .paper{
    /*border-bottom: 1px solid black;*/
    margin-bottom: 15px;

}
</style>

<script type="text/javascript">
    // script to make a sliding effect when clicking bib link

    // The keyword "jQuery" is needed because of "noConflict(..)"
    jQuery(document).ready(function(){
        
        $(".bibsrc").css("display", "none");

        $(".bibsrc").slideUp(1);

        $(".biblink").click(function(){
            $(this).parents(".paper").children(".bibsrc").slideToggle(100) ;
        });

    });

</script>

<div class="publications"> 

<div class="paper"> 
<div class="paper_title">Cognitive Bias in Ambiguity Judgements: Using Computational Models to Dissect the Effects of Mild Mood Manipulation in Humans</div>
<div class="author_list"><a href="http://kyoiigaya.weebly.com/">Kiyohito Iigaya</a>, Aurelie Jolivald, <b>Wittawat Jitkrittum</b>, Iain Gilchrist, <a href="http://www.gatsby.ucl.ac.uk/~dayan/">Peter Dayan</a>, Elizabeth Paul, and Michael Mendl</div>
<span class="submit_to">PLOS ONE</span>, 2016. 
<div class="links">Link: 
<a class="wj_http" href="http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165840">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{iigaya2016,
 author = {Kiyohito Iigaya and Aurelie Jolivald and Wittawat Jitkrittum and Iain Gilchrist and Peter Dayan and Elizabeth Paul and Michael Mendl},
 issn = {1932-6203},
 journal = {PLOS ONE},
 month = {10},
 publisher = {Public Library of Science},
 title = {Cognitive Bias in Ambiguity Judgements: Using Computational Models to Dissect the Effects of Mild Mood Manipulation in Humans},
 year = {2016}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">An Adaptive Test of Independence with Analytic Kernel Embeddings</div>
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://www.gatsby.ucl.ac.uk/~szabo/">Zoltan Szabo</a>, and <a href="http://www.gatsby.ucl.ac.uk/~gretton/">Arthur Gretton</a></div>
<span class="submit_to">arXiv:1610.04782</span>, 2016. 
<div class="links">Link: 
<a class="wj_http" href="https://arxiv.org/abs/1610.04782">http</a>
<a class="wj_code" href="https://github.com/wittawatj/fsic-test">code</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{jitkrittum+al:2016:indtest,
 author = {Wittawat Jitkrittum and Zoltan Szabo and Arthur Gretton},
 journal = {{arXiv}:1610.04782},
 link = {https://arxiv.org/abs/1610.04782},
 title = {An Adaptive Test of Independence with Analytic Kernel Embeddings},
 wj_code = {https://github.com/wittawatj/fsic-test},
 year = {2016}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Interpretable Distribution Features with Maximum Testing Power</div>
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://www.gatsby.ucl.ac.uk/~szabo/">Zoltán Szabó</a>, Kacper Chwialkowski, and <a href="http://www.gatsby.ucl.ac.uk/~gretton/">Arthur Gretton</a></div>
<span class="submit_to">arXiv:1605.06796</span>, 2016. 
<div class="links">Link: 
<a class="wj_http" href="http://arxiv.org/abs/1605.06796">http</a>
<a class="wj_code" href="https://github.com/wittawatj/interpretable-test">code</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{fotest_arxiv2016,
 author = {Wittawat Jitkrittum and Zoltán Szabó and Kacper Chwialkowski and Arthur Gretton},
 journal = {{arXiv}:1605.06796},
 link = {http://arxiv.org/abs/1605.06796},
 title = {Interpretable Distribution Features with Maximum Testing Power},
 wj_code = {https://github.com/wittawatj/interpretable-test},
 year = {2016}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">K2-ABC: Approximate Bayesian Computation with Infinite Dimensional Summary Statistics via Kernel Embeddings</div>
<div class="author_list"><a href="http://www.gatsby.ucl.ac.uk/~mijung/">Mijung Park</a>, <b>Wittawat Jitkrittum</b>, and <a href="http://www.stats.ox.ac.uk/~sejdinov/">Dino Sejdinovic</a></div>
<span class="submit_to">AISTATS</span>, 2016. 
<div class="links">Link: 
<a class="wj_http" href="http://jmlr.org/proceedings/papers/v51/park16.html">http</a>
<a class="wj_code" href="https://github.com/wittawatj/k2abc">code</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{part_k2abc_2015_arxiv,
 author = {Mijung Park and Wittawat Jitkrittum and Dino Sejdinovic},
 booktitle = {AISTATS},
 link = {http://jmlr.org/proceedings/papers/v51/park16.html},
 title = {{K2-ABC}: Approximate {B}ayesian Computation with Infinite Dimensional Summary Statistics via Kernel Embeddings},
 wj_code = {https://github.com/wittawatj/k2abc},
 year = {2016}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Bayesian Manifold Learning: The Locally Linear Latent Variable Model</div>
<div class="author_list"><a href="http://www.gatsby.ucl.ac.uk/~mijung/">Mijung Park</a>, <b>Wittawat Jitkrittum</b>, Ahmad Qamar, <a href="http://www.gatsby.ucl.ac.uk/~szabo/">Zoltán Szabó</a>, Lars Buesing, and Maneesh Sahani</div>
<span class="submit_to">NIPS</span>, 2015. 
<div class="links">Link: 
<a class="wj_http" href="http://arxiv.org/abs/1410.6791">http</a>
<a class="wj_code" href="https://github.com/mijungi/lllvm">code</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{Park2015,
 author = {Mijung Park and Wittawat Jitkrittum and Ahmad Qamar and  Zoltán Szabó and Lars Buesing and  Maneesh Sahani},
 booktitle = {NIPS},
 link = {http://arxiv.org/abs/1410.6791},
 title = {Bayesian Manifold Learning: The Locally Linear Latent Variable Model},
 wj_code = {https://github.com/mijungi/lllvm},
 year = {2015}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Kernel-Based Just-In-Time Learning for Passing Expectation Propagation Messages</div>
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://www.gatsby.ucl.ac.uk/~gretton/">Arthur Gretton</a>, <a href="http://homepages.inf.ed.ac.uk/s0677090/">Nicolas Heess</a>, <a href="http://arkitus.com/">S. M. Ali Eslami</a>, <a href="http://www.gatsby.ucl.ac.uk/~balaji/">Balaji Lakshminarayanan</a>, <a href="http://www.stats.ox.ac.uk/~sejdinov/">Dino Sejdinovic</a>, and <a href="http://www.gatsby.ucl.ac.uk/~szabo/">Zoltán Szabó</a></div>
<span class="submit_to">UAI</span>, 2015. 
<div class="links">Link: 
<a class="wj_http" href="http://arxiv.org/abs/1503.02551">http</a>
<a class="wj_code" href="https://github.com/wittawatj/kernel-ep">code</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{jitkrittum_kernel-based_2015,
 author = {Jitkrittum, Wittawat and Gretton, Arthur and Heess, Nicolas and Eslami, S. M. Ali and Lakshminarayanan, Balaji and Sejdinovic, Dino and Szabó, Zoltán},
 booktitle = {UAI},
 link = {http://arxiv.org/abs/1503.02551},
 title = {Kernel-{Based} {Just}-{In}-{Time} {Learning} for {Passing} {Expectation} {Propagation} {Messages}},
 wj_code = {https://github.com/wittawatj/kernel-ep},
 year = {2015}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">High-Dimensional Feature Selection by Feature-Wise Kernelized
Lasso</div>
<div class="author_list"><a href="http://www.makotoyamada-ml.com/">Makoto Yamada</a>, <b>Wittawat Jitkrittum</b>, <a href="http://cs.brown.edu/~ls/">Leonid Sigal</a>, <a href="http://www.cs.cmu.edu/~epxing/">Eric P. Xing</a>, and <a href="http://www.ms.k.u-tokyo.ac.jp/index.html">Masashi Sugiyama</a></div>
<span class="submit_to">Neural Computation</span>, 2014. 
<div class="links">Link: 
<a class="wj_http" href="http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00537#.U9O7Idtsylg">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{YamadaJSXS14,
 author = {Makoto Yamada and
Wittawat Jitkrittum and
Leonid Sigal and
Eric P. Xing and
Masashi Sugiyama},
 journal = {Neural Computation},
 link = {http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00537#.U9O7Idtsylg},
 number = {1},
 pages = {185-207},
 title = {High-Dimensional Feature Selection by Feature-Wise Kernelized
Lasso},
 volume = {26},
 year = {2014}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Feature Selection via $\ell_1$-Penalized Squared-Loss Mutual Information</div>
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://sugiyama-www.cs.titech.ac.jp/~hachiya/">Hirotaka Hachiya</a>, and <a href="http://www.ms.k.u-tokyo.ac.jp/index.html">Masashi Sugiyama</a></div>
<span class="submit_to">IEICE Transactions</span>, 2013. 
<div class="links">Link: 
<a class="wj_pdf" href="http://wittawat.com/pages/files/L1LSMI.pdf">pdf</a>
<a class="wj_code" href="https://github.com/wittawatj/l1lsmi">code</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{Jitkrittum2013,
 author = {Wittawat Jitkrittum and Hirotaka Hachiya and Masashi Sugiyama},
 journal = {IEICE Transactions},
 number = {7},
 pages = {1513-1524},
 title = {Feature Selection via $\ell_1$-Penalized Squared-Loss Mutual Information},
 volume = {96-D},
 wj_code = {https://github.com/wittawatj/l1lsmi},
 year = {2013}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Squared-loss Mutual Information Regularization: A Novel Information-theoretic
Approach to Semi-supervised Learning</div>
<div class="author_list"><a href="http://sugiyama-www.cs.titech.ac.jp/~gang/">Gang Niu</a>, <b>Wittawat Jitkrittum</b>, <a href="https://sites.google.com/site/daibohr/">Bo Dai</a>, <a href="http://sugiyama-www.cs.titech.ac.jp/~hachiya/">Hirotaka Hachiya</a>, and <a href="http://www.ms.k.u-tokyo.ac.jp/index.html">Masashi Sugiyama</a></div>
<span class="submit_to">ICML, JMLR W & CP</span>, 2013. 
<div class="links">Link: 
<a class="wj_pdf" href="http://jmlr.org/proceedings/papers/v28/niu13.pdf">pdf</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{Niu2013,
 author = {Gang Niu and Wittawat Jitkrittum and Bo Dai and Hirotaka Hachiya and Masashi Sugiyama},
 booktitle = {ICML, JMLR W \& CP},
 link = {http://jmlr.org/proceedings/papers/v28/niu13.pdf},
 pages = {10-18},
 title = {Squared-loss Mutual Information Regularization: A Novel Information-theoretic
Approach to Semi-supervised Learning},
 volume = {28},
 year = {2013}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">QAST: Question Answering System for Thai Wikipedia</div>
<div class="author_list"><b>Wittawat Jitkrittum</b>, Choochart Haruechaiyasak, and Thanaruk Theeramunkong</div>
<span class="submit_to">Proceedings of the 2009 Workshop on Knowledge and Reasoning for Answering
Questions</span>, 2009. 
<div class="links">Link: 
<a class="wj_http" href="http://dl.acm.org/citation.cfm?id=1697288.1697291">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{Jitkrittum2009,
 author = {Wittawat Jitkrittum and  Choochart Haruechaiyasak and Thanaruk Theeramunkong},
 booktitle = {Proceedings of the 2009 Workshop on Knowledge and Reasoning for Answering
Questions},
 link = {http://dl.acm.org/citation.cfm?id=1697288.1697291},
 pages = {11--14},
 publisher = {Association for Computational Linguistics},
 series = {KRAQ '09},
 title = {{QAST}: Question Answering System for {Thai} Wikipedia},
 year = {2009}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Implementing News Article Category Browsing Based on Text Categorization
Technique</div>
<div class="author_list">Choochart Haruechaiyasak, <b>Wittawat Jitkrittum</b>, Chatchawal Sangkeettrakarn, and Chaianun Damrongrat</div>
<span class="submit_to">Web Intelligence/IAT Workshops</span>, 2008. 
<div class="links">Link: 
<a class="wj_http" href="http://dx.doi.org/10.1109/WIIAT.2008.61">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{Haruechaiyasak2008,
 author = {Choochart Haruechaiyasak and Wittawat Jitkrittum and Chatchawal Sangkeettrakarn
and Chaianun Damrongrat},
 booktitle = {Web Intelligence/IAT Workshops},
 ee = {http://dx.doi.org/10.1109/WIIAT.2008.61},
 pages = {143-146},
 title = {Implementing News Article Category Browsing Based on Text Categorization
Technique},
 year = {2008}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="paper_title">Managing Offline Educational Web Contents with Search Engine Tools</div>
<div class="author_list">Choochart Haruechaiyasak, Chatchawal Sangkeettrakarn, and <b>Wittawat Jitkrittum</b></div>
<span class="submit_to">ICADL</span>, 2007. 
<div class="links">Link: 
<a class="wj_http" href="http://dx.doi.org/10.1007/978-3-540-77094-7_56">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@inproceedings{Haruechaiyasak2007,
 author = {Choochart Haruechaiyasak and Chatchawal Sangkeettrakarn and Wittawat
Jitkrittum},
 booktitle = {ICADL},
 ee = {http://dx.doi.org/10.1007/978-3-540-77094-7_56},
 pages = {444-453},
 title = {Managing Offline Educational Web Contents with Search Engine Tools},
 year = {2007}
}

</pre><!-- end bib source -->
</div>

</div> 

