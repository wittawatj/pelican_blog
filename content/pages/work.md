Title: 
Slug: work


## Projects

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
        $(".bibsrc").slideUp();

        $(".biblink").click(function(){
            $(this).parents(".paper").children(".bibsrc").slideToggle(200) ;
        });
    });

</script>

<div class="publications"> 

<div class="paper"> 
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://www.gatsby.ucl.ac.uk/~gretton/">Arthur Gretton</a>, <a href="http://homepages.inf.ed.ac.uk/s0677090/">Nicolas Heess</a>, <a href="http://arkitus.com/">S. M. Ali Eslami</a>, <a href="http://www.gatsby.ucl.ac.uk/~balaji/">Balaji Lakshminarayanan</a>, <a href="http://www.stats.ox.ac.uk/~sejdinov/">Dino Sejdinovic</a>, and <a href="http://www.gatsby.ucl.ac.uk/~szabo/">Zoltán Szabó</a></div>
<div class="paper_title">Kernel-Based Just-In-Time Learning for Passing Expectation Propagation Messages</div>
<span class="submit_to">arXiv:1503.02551</span>, 2015. 
<div class="links">Link: 
<a class="wj_http" href="http://arxiv.org/abs/1503.02551">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{jitkrittum_kernel-based_2015,
 author = {Jitkrittum, Wittawat and Gretton, Arthur and Heess, Nicolas and Eslami, S. M. Ali and Lakshminarayanan, Balaji and Sejdinovic, Dino and Szabó, Zoltán},
 journal = {arXiv:1503.02551},
 link = {http://arxiv.org/abs/1503.02551},
 title = {Kernel-{Based} {Just}-{In}-{Time} {Learning} for {Passing} {Expectation} {Propagation} {Messages}},
 year = {2015}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="author_list"><a href="http://www.gatsby.ucl.ac.uk/~mijung/">Mijung Park</a>, <b>Wittawat Jitkrittum</b>, and <a href="http://www.stats.ox.ac.uk/~sejdinov/">Dino Sejdinovic</a></div>
<div class="paper_title">K2-ABC: Approximate Bayesian Computation with Infinite Dimensional Summary Statistics via Kernel Embeddings</div>
<span class="submit_to">arXiv:1502.02558</span>, 2015. 
<div class="links">Link: 
<a class="wj_http" href="http://arxiv.org/abs/1502.02558">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{part_k2abc_2015_arxiv,
 author = {Mijung Park and Wittawat Jitkrittum and Dino Sejdinovic},
 journal = {{arXiv}:1502.02558},
 link = {http://arxiv.org/abs/1502.02558},
 title = {{K2-ABC}: Approximate {B}ayesian Computation with Infinite Dimensional Summary Statistics via Kernel Embeddings},
 year = {2015}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://www.gatsby.ucl.ac.uk/~gretton/">Arthur Gretton</a>, and <a href="http://homepages.inf.ed.ac.uk/s0677090/">Nicolas Heess</a></div>
<div class="paper_title">Passing Expectation Propagation Messages with Kernel Methods</div>
<span class="submit_to">arXiv:1501.00375</span>, 2015. 
<div class="links">Link: 
<a class="wj_http" href="http://arxiv.org/abs/1501.00375">http</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{jitkrittum_passing_2015,
 annote = {Comment: Accepted to Advances in Variational Inference, {NIPS} 2014 Workshop},
 author = {Wittawat Jitkrittum and Arthur Gretton and Nicolas Heess},
 journal = {{arXiv}:1501.00375},
 link = {http://arxiv.org/abs/1501.00375},
 title = {Passing Expectation Propagation Messages with Kernel Methods},
 year = {2015}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="author_list"><a href="http://www.makotoyamada-ml.com/">Makoto Yamada</a>, <b>Wittawat Jitkrittum</b>, <a href="http://cs.brown.edu/~ls/">Leonid Sigal</a>, <a href="http://www.cs.cmu.edu/~epxing/">Eric P. Xing</a>, and <a href="http://www.ms.k.u-tokyo.ac.jp/index.html">Masashi Sugiyama</a></div>
<div class="paper_title">High-Dimensional Feature Selection by Feature-Wise Kernelized
Lasso</div>
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
<div class="author_list"><b>Wittawat Jitkrittum</b>, <a href="http://sugiyama-www.cs.titech.ac.jp/~hachiya/">Hirotaka Hachiya</a>, and <a href="http://www.ms.k.u-tokyo.ac.jp/index.html">Masashi Sugiyama</a></div>
<div class="paper_title">Feature Selection via $\ell_1$-Penalized Squared-Loss Mutual Information</div>
<span class="submit_to">IEICE Transactions</span>, 2013. 
<div class="links">Link: 
<a class="wj_pdf" href="http://wittawat.com/pages/files/L1LSMI.pdf">pdf</a>
<a class="biblink">bib</a> 
</div> <!-- end links -->
<pre class="bibsrc">@article{Jitkrittum2013,
 author = {Wittawat Jitkrittum and Hirotaka Hachiya and Masashi Sugiyama},
 journal = {IEICE Transactions},
 number = {7},
 pages = {1513-1524},
 title = {Feature Selection via $\ell_1$-Penalized Squared-Loss Mutual Information},
 volume = {96-D},
 year = {2013}
}

</pre><!-- end bib source -->
</div>

<div class="paper"> 
<div class="author_list"><a href="http://sugiyama-www.cs.titech.ac.jp/~gang/">Gang Niu</a>, <b>Wittawat Jitkrittum</b>, <a href="https://sites.google.com/site/daibohr/">Bo Dai</a>, <a href="http://sugiyama-www.cs.titech.ac.jp/~hachiya/">Hirotaka Hachiya</a>, and <a href="http://www.ms.k.u-tokyo.ac.jp/index.html">Masashi Sugiyama</a></div>
<div class="paper_title">Squared-loss Mutual Information Regularization: A Novel Information-theoretic
Approach to Semi-supervised Learning</div>
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
<div class="author_list"><b>Wittawat Jitkrittum</b>, Choochart Haruechaiyasak, and Thanaruk Theeramunkong</div>
<div class="paper_title">QAST: Question Answering System for Thai Wikipedia</div>
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
<div class="author_list">Choochart Haruechaiyasak, <b>Wittawat Jitkrittum</b>, Chatchawal Sangkeettrakarn, and Chaianun Damrongrat</div>
<div class="paper_title">Implementing News Article Category Browsing Based on Text Categorization
Technique</div>
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
<div class="author_list">Choochart Haruechaiyasak, Chatchawal Sangkeettrakarn, and <b>Wittawat Jitkrittum</b></div>
<div class="paper_title">Managing Offline Educational Web Contents with Search Engine Tools</div>
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


<!--<div id="publications">-->

<!--<dl>-->

<!--<dt>-->
<!--<a name="jitkrittum_kernel-based_2015">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--W.&nbsp;Jitkrittum, A.&nbsp;Gretton, N.&nbsp;Heess, S.&nbsp;M.&nbsp;A. Eslami, B.&nbsp;Lakshminarayanan,-->
  <!--D.&nbsp;Sejdinovic, and Z.&nbsp;Szabó.-->
 <!--Kernel-Based Just-In-Time Learning for Passing-->
  <!--Expectation Propagation Messages.-->
 <!--<em>arXiv:1503.02551 [cs, stat]</em>, 2015.-->
 <!--URL <a href="http://arxiv.org/abs/1503.02551">http://arxiv.org/abs/1503.02551</a>.-->
<!--[&nbsp;<a href="wjpubs_bib.html#jitkrittum_kernel-based_2015">bib</a>&nbsp;| -->
<!--<a href="http://arxiv.org/abs/1503.02551">http</a>&nbsp;]-->

<!--</dd>-->

<!--<dt>-->
<!--<a name="part_k2abc_2015_arxiv">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--M.&nbsp;Park, W.&nbsp;Jitkrittum, and D.&nbsp;Sejdinovic.-->

 <!--K2-ABC: Approximate bayesian computation with infinite dimensional-->
  <!--summary statistics via kernel embeddings.-->
 <!--Technical Report arXiv:1502.02558, 2015.-->
 <!--URL <a href="http://arxiv.org/abs/1502.02558">http://arxiv.org/abs/1502.02558</a>.-->
<!--[&nbsp;<a href="wjpubs_bib.html#part_k2abc_2015_arxiv">bib</a>&nbsp;| -->
<!--<a href="http://arxiv.org/abs/1502.02558">http</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="jitkrittum_passing_2015">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--W.&nbsp;Jitkrittum, A.&nbsp;Gretton, and N.&nbsp;Heess.-->
 <!--Passing expectation propagation messages with kernel methods.-->
 <!--Technical Report arXiv:1501.00375 [stat], 2015.-->
 <!--URL <a href="http://arxiv.org/abs/1501.00375">http://arxiv.org/abs/1501.00375</a>.-->
<!--[&nbsp;<a href="wjpubs_bib.html#jitkrittum_passing_2015">bib</a>&nbsp;| -->
<!--<a href="http://arxiv.org/abs/1501.00375">http</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="YamadaJSXS14">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--M.&nbsp;Yamada, W.&nbsp;Jitkrittum, L.&nbsp;Sigal, E.&nbsp;P. Xing, and M.&nbsp;Sugiyama.-->
 <!--High-dimensional feature selection by feature-wise kernelized lasso.-->
 <!--<em>Neural Computation</em>, 260 (1):0 185-207, 2014.-->
 <!--URL-->
  <!--<a href="http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00537#.U9O7Idtsylg">http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00537#.U9O7Idtsylg</a>.-->
<!--[&nbsp;<a href="wjpubs_bib.html#YamadaJSXS14">bib</a>&nbsp;| -->
<!--<a href="http://www.mitpressjournals.org/doi/abs/10.1162/NECO_a_00537#.U9O7Idtsylg">http</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="Jitkrittum2013">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--W.&nbsp;Jitkrittum, H.&nbsp;Hachiya, and M.&nbsp;Sugiyama.-->
 <!--Feature selection via L<sub>1</sub>-penalized squared-loss mutual-->
  <!--information.-->
 <!--<em>IEICE Transactions</em>, 96-D0 (7):0 1513-1524,-->
  <!--2013.-->
<!--[&nbsp;<a href="wjpubs_bib.html#Jitkrittum2013">bib</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="Niu2013">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--G.&nbsp;Niu, W.&nbsp;Jitkrittum, B.&nbsp;Dai, H.&nbsp;Hachiya, and M.&nbsp;Sugiyama.-->
 <!--Squared-loss mutual information regularization: A novel-->
  <!--information-theoretic approach to semi-supervised learning.-->
 <!--In <em>ICML, JMLR W &amp; CP</em>, volume&nbsp;28, pages 10-18, 2013.-->
 <!--URL <a href="http://jmlr.org/proceedings/papers/v28/niu13.pdf">http://jmlr.org/proceedings/papers/v28/niu13.pdf</a>.-->
<!--[&nbsp;<a href="wjpubs_bib.html#Niu2013">bib</a>&nbsp;| -->
<!--<a href="http://jmlr.org/proceedings/papers/v28/niu13.pdf">.pdf</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="Jitkrittum2009">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--W.&nbsp;Jitkrittum, C.&nbsp;Haruechaiyasak, and T.&nbsp;Theeramunkong.-->
 <!--QAST: Question answering system for Thai wikipedia.-->
 <!--In <em>Proceedings of the 2009 Workshop on Knowledge and Reasoning-->
  <!--for Answering Questions</em>, KRAQ '09, pages 11-14. Association for-->
  <!--Computational Linguistics, 2009.-->
 <!--URL <a href="http://dl.acm.org/citation.cfm?id=1697288.1697291">http://dl.acm.org/citation.cfm?id=1697288.1697291</a>.-->
<!--[&nbsp;<a href="wjpubs_bib.html#Jitkrittum2009">bib</a>&nbsp;| -->
<!--<a href="http://dl.acm.org/citation.cfm?id=1697288.1697291">http</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="Haruechaiyasak2008">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--C.&nbsp;Haruechaiyasak, W.&nbsp;Jitkrittum, C.&nbsp;Sangkeettrakarn, and C.&nbsp;Damrongrat.-->
 <!--Implementing news article category browsing based on text-->
  <!--categorization technique.-->
 <!--In <em>Web Intelligence/IAT Workshops</em>, pages 143-146, 2008.-->
<!--[&nbsp;<a href="wjpubs_bib.html#Haruechaiyasak2008">bib</a>&nbsp;]-->

<!--</dd>-->


<!--<dt>-->
<!--<a name="Haruechaiyasak2007">&nbsp;</a>-->
<!--</dt>-->
<!--<dd>-->
<!--C.&nbsp;Haruechaiyasak, C.&nbsp;Sangkeettrakarn, and W.&nbsp;Jitkrittum.-->
 <!--Managing offline educational web contents with search engine tools.-->
 <!--In <em>ICADL</em>, pages 444-453, 2007.-->
<!--[&nbsp;<a href="wjpubs_bib.html#Haruechaiyasak2007">bib</a>&nbsp;]-->

<!--</dd>-->
<!--</dl><hr>-->

<!--</div>-->
