Title: ย่อขนาดตารางใน Latex 
Date: 2012-02-02 07:14:43
Tags: beamer, latex 
Slug: ย่อขนาดตารางใน Latex 


การใส่ตารางใน Latex ปกติก็ใช้ tabular ร่วมกับ floating environment table คำสั่ง tabular นี้ไม่มี option ให้ย่อขนาดของตารางได้ เท่าที่หาได้มีหลายวิธีที่สามารถย่อขนาดได้

วิธีแรกคือใช้คำสั่ง tiny หรือ small เพื่อย่อตารางแบบนี้

[codesyntax lang="latex"]
<pre>\tiny
%\small
\begin{tabular}{...}
%....
\end{tabular}</pre>
[/codesyntax]

แต่มันคุมขนาดไม่ได้ อีกวิธีที่ดีกว่าคือใช้ scalebox ซึ่งสามารถกำหนด ratio ที่ต้องการได้ เช่นถ้าอยากย่อให้เหลือ 60% ก็ทำแบบนี[codesyntax lang="latex"]
<pre>\usepackage{graphicx}
%...
\scalebox{0.6}{
 \begin{tabular}{..}
  %...
 \end{tabular}
}</pre>
[/codesyntax]

หรือจะใช้ resizebox ก็ได้ ซึ่งคุมได้ทั้งความกว้าง ความยาว

สำหรับคนใช้ beamer อีกวิธีที่สามารถย่อ table ได้คือใช้ option shrink แบบนี้

[codesyntax lang="latex"]
<pre>\begin{frame}[shrink=10]{frame title}
%...
\end{frame}</pre>
[/codesyntax]

แต่ถ้าใช้วิธีนี้จะทำให้ทุกอย่าง (ไม่ใช่แค่ table) ใน frame ถูกย่อเพื่อให้อยู่ใน frame ได้

ที่มา
<ul>
	<li><a href="http://tex.stackexchange.com/questions/5067/shrinking-tables-for-presentations">http://tex.stackexchange.com/questions/5067/shrinking-tables-for-presentations</a></li>
	<li><a href="http://en.wikibooks.org/wiki/LaTeX/Tables">http://en.wikibooks.org/wiki/LaTeX/Tables</a></li>
</ul>
