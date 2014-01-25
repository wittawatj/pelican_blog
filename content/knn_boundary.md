Title: Knn Boundary Visualization with Processing.js
Date: 2013-07-09
Slug: knn_boundary
Tags: knn, visualize


<script src="/js/processing.js" type="text/javascript"></script>
<script type="text/javascript">
// convenience function to get the id attribute of generated sketch html element
function getProcessingSketchId () { return 'knn'; }
</script>

I have known [Processing](http://www.processing.org/) for quite a while as a programming language
for quick prototyping graphically interactive programs. But not until recently that I realized
it is also capable of exporting into a Javascript program through [Processing.js](http://processingjs.org/) 
(already built into the Processing IDE). What this means is that you can write a Processing program
once and have it run on the usual Java platforms as well as web browsers supporting Javascript (provided that
no external Processing library is used). 

Here is my little implementation of [Knn](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) boundary visualizer. 
I did this just to get a feel of Processing.js.

* The number of neighbours k is adjustable using --/++ buttons. 
* Clicking anywhere in the canvas will produce a new point. 
* The class to which the produced points belong can be selected with the red/blue rectangles at the top.

<p>
<canvas id="knn" style="border: 1px solid black" data-processing-sources="upload/knn.pde" width="500" height="400">
<!-- Note: you can put any alternative content here. -->
</canvas>
</p>
        
I found the process of composing the code to be pleasant. This is perhaps partially because of the similarity
to Java which I am already familiar. One thing worth mentioning though is that, TBOMK, without an external library, Processing.js
does not support any UI component (i.e., button, combo box). Everything above was achieved by drawing, which is a bit painful
if you have many buttons; as you need to manually specify the coordinates to draw. 
This will pose an even more serious problem if the effect of a text field is desired.
The only thing provided is the facility to capture keys. Then, you are on your own for the rest.
Apparently it takes a lot of patience to write code to simulate the blinking
cursor of a text field.
Optimistically I am pretty sure someday there will be a library for UI components in Processing.js.

Download: [Source code](/upload/knn.pde)

