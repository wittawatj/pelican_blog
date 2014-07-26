Title: 
Slug: work


## Projects

* [$\ell_1$-LSMI](l1lsmi.html) -- A supervised feature selection algorithm based on a squared-loss variant of mutual information. 
Implementation is available in Matlab. (03/2013)

* [Classifier-based Thai Word Tokenizer](https://github.com/wittawatj/ctwt) --  Decision tree-based Java library to tokenize Thai text. The project was finished in two months for a competition. **Warning**: Not for production use. Detail is in this [presentation file](files/wordseg_dt.pdf). (02/2010)

* [JTCC](http://code.google.com/p/jtcc/) -- Rule-based Java library to tokenize Thai text into a list of Thai Character Clusters (TCC). (03/2010)

## Publications
<!--https://github.com/vkaravir/bib-publication-list-->
<div id=pubDiv>
<table id="pubTable" class="display"></table>
</div>
<pre id="bibtex" style="display:none;">@ARTICLE{Jitkrittum2013,
  author = {Wittawat Jitkrittum and Hirotaka Hachiya and Masashi Sugiyama},
  title = {Feature Selection via $\ell_1$-Penalized Squared-Loss Mutual Information},
  journal = {IEICE Transactions},
  year = {2013},
  volume = {96-D},
  pages = {1513-1524},
  number = {7},
  bibsource = {DBLP, http://dblp.uni-trier.de},
  ee = {http://search.ieice.org/bin/summary.php?id=e96-d_7_1513}
}
@INPROCEEDINGS{Niu2013,
    author={Gang Niu and Wittawat Jitkrittum and Bo Dai and Hirotaka Hachiya and Masashi Sugiyama},
  title = {Squared-loss Mutual Information Regularization: A Novel Information-theoretic
	Approach to Semi-supervised Learning},
  booktitle = {Proceedings of the 30th International Conference on Machine Learning
	(ICML-13)},
  year = {2013},
  editor = {Sanjoy Dasgupta and David McAllester},
  volume = {28},
  number = {3},
  pages = {10-18},
  month = {May},
  publisher = {JMLR Workshop and Conference Proceedings},
  url = {http://jmlr.org/proceedings/papers/v28/niu13.pdf}
}
@techreport{yamada_high-dimensional_2012,
    author={Makoto Yamada and Wittawat Jitkrittum and Leonid Sigal and Eric P. Xing and Masashi Sugiyama},
	title = {High-Dimensional Feature Selection by Feature-Wise Non-Linear Lasso},
	url = {http://arxiv.org/abs/1202.0515},
	number = {{arXiv}:1202.0515 [cs, stat]},
	year = {2012},
	eprinttype = {arxiv},
    institution={Tokyo Institute of Technology},
    type={Research Note},
}

@INPROCEEDINGS{Jitkrittum2009,
  author = {Wittawat Jitkrittum and  Choochart Haruechaiyasak and Thanaruk Theeramunkong },
  title = {{QAST}: question answering system for {Thai} Wikipedia},
  booktitle = {Proceedings of the 2009 Workshop on Knowledge and Reasoning for Answering
  Questions},
  year = {2009},
  series = {KRAQ '09},
  pages = {11--14},
  address = {Stroudsburg, PA, USA},
  publisher = {Association for Computational Linguistics},
  acmid = {1697291},
  isbn = {978-1-932432-50-3},
  location = {Suntec, Singapore},
  numpages = {4},
  url = {http://dl.acm.org/citation.cfm?id=1697288.1697291}
}
@INPROCEEDINGS{Haruechaiyasak2008,
  author = {Choochart Haruechaiyasak and Wittawat Jitkrittum and Chatchawal Sangkeettrakarn
  and Chaianun Damrongrat},
  title = {Implementing News Article Category Browsing Based on Text Categorization
  Technique},
  booktitle = {Web Intelligence/IAT Workshops},
  year = {2008},
  pages = {143-146},
  bibsource = {DBLP, http://dblp.uni-trier.de},
  ee = {http://dx.doi.org/10.1109/WIIAT.2008.61}
}
@INPROCEEDINGS{Haruechaiyasak2007,
  author = {Choochart Haruechaiyasak and Chatchawal Sangkeettrakarn and Wittawat
  Jitkrittum},
  title = {Managing Offline Educational Web Contents with Search Engine Tools},
  booktitle = {ICADL},
  year = {2007},
  pages = {444-453},
  bibsource = {DBLP, http://dblp.uni-trier.de},
  ee = {http://dx.doi.org/10.1007/978-3-540-77094-7_56}
}
</pre>
<!--<style>@import url('/css/bib-publication-list.css');</style>-->
<link rel="stylesheet" type="text/css" href="/css/bib-publication-list.css"/>
<script src="/js/jquery.dataTables.min.js"></script>
<!--<script src="/js/bib-list-min.js"></script>-->
<script src="/js/bib-list.js"></script>
<script src="/js/bib-publication-list.js"></script>
<script type="text/javascript">
 var init = function() {
   bibtexify("#bibtex", "pubTable", {});
//bibtexify("files/publications.bib", "pubTable", {});
 };
 if (window.addEventListener) {
   window.addEventListener('load', init, false);
 } else if (window.attachEvent) {
   window.attachEvent('onload', init);
 }
</script>
