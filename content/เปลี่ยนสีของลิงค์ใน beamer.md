Title: เปลี่ยนสีของลิงค์ใน beamer 
Date: 2012-01-30 13:00:33
Tags: beamer, latex 
Slug: เปลี่ยนสีของลิงค์ใน beamer 


&nbsp;

ปกติใน Latex หากต้องการใส่สีให้กับลิงค์ต่างๆเช่น URL หรือลิงค์ที่เกิดจากการอ้างอิง แค่ใส่ code

[code lang="latex"]
\usepackage{hyperref}
\hypersetup{colorlinks}
[/code]

ก็ได้แล้ว ถ้าจะเปลี่ยนสีก็ใช้

[code lang="latex"]
\hypersetup{linkcolor=red,citecolor=green}
[/code]

linkcolor คือลิงค์ทั่วไปในเอกสาร (ปกติสีแดง) ส่วน citecolor คือลิงค์ที่เกิดจากการอ้างอิง (ปกติสีเขียว)

ที่อยากทำคืออยากได้ citecolor=gray แต่ปัญหาเกิดเมื่อใช้ hyperref ร่วมกับ beamer เพราะไม่รู้ทำไมเปลี่ยน citecolor แล้วไม่มีผล ดูเหมือนว่าสีของลิงค์ทุกชนิดจะถูกคุมด้วย linkcolor หมดเลย ซึ่งเป็นปัญหา วิธีแก้แบบ hack ก็แน่นอน ใช้

[code lang="latex"]
\hypersetup{linkcolor=gray}
[/code]

ไปก่อน แต่ประเด็นคือมันไปกระทบกับสารบัญ เพราะสารบัญก็เป็นลิงค์เหมือนกัน ก็เลยไปตามแก้ด้วยการทำข้อยกเว้นตอนใส่สารบัญ แบบนี้

[code lang="latex"]
\begin{frame}{Outline}
 \begingroup
  \hypersetup{linkcolor=black}
  \tableofcontents
 \endgroup
\end{frame}
[/code]

ส่วนตัวแล้วไม่ชอบวิธีนี้แต่ไม่รู้จะแก้ยังไง ถ้าจะให้สารบัญแสดงขึ้นมาตอนเปลี่ยน section ใหม่ก็ให้ทำคล้ายๆกัน ประมาณนี้

[codesyntax lang="latex"]
<pre> \AtBeginSection[]
 {
   \begin{frame}&lt;beamer&gt;{Outline}
     \begingroup
     \hypersetup{linkcolor=black}
     \tableofcontents[currentsection]
     \endgroup
   \end{frame}
 }</pre>
[/codesyntax]

ที่มา
<ul>
	<li><a href="http://www.tug.org/applications/hyperref/manual.html">http://www.tug.org/applications/hyperref/manual.html</a></li>
	<li><a href="http://groups.google.com/group/comp.text.tex/browse_thread/thread/f112d57202c9caa9">http://groups.google.com/group/comp.text.tex/browse_thread/thread/f112d57202c9caa9</a></li>
</ul>
