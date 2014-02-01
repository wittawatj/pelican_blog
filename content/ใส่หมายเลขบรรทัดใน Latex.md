Title: ใส่หมายเลขบรรทัดใน Latex 
Date: 2012-02-09 05:00:13
Tags: latex 
Slug: ใส่หมายเลขบรรทัดใน Latex 


การเขียนบทความที่มีผู้เขียนหลายคนบางทีมีความจำเป็นต้องแลกเปลี่ยนส่วนที่แต่ละคนเขียน จะคุยกันสะดวกถ้าบรรทัดมีหมายเลขกำกับ (ได้ไอเดียนี้มาจาก template ของ ICML) วิธีใส่หมายเลขบรรทัด อันดับแรกให้หาโหลด lineno.sty ใครใช้ Ubuntu ให้ทำ

[code lang="bash"]sudo apt-get install texlive-humanities[/code]

จากนั้นเปิดหมายเลขบรรทัดด้วย

[code lang="latex"]
\usepackage{lineno}
\linenumbers
[/code]

แค่นี้ก็ได้แล้ว แต่มีประเด็นนิดหน่อย คือปกติเลขบรรทัดตัวเล็กมาก และเป็นสีดำเหมือนตัวอักษรปกติ อยากได้สีเทา วิธีแก้คือ

[code lang="latex"]
\renewcommand{\linenumberfont}{\normalfont\color{gray}}
[/code]

อีกประเด็นคือ ปกติเลขบรรทัดจะแสดงที่ด้านซ้าย แต่สำหรับเอกสาร 2 คอลัมน์ มันควรแสดงด้านขวาสำหรับคอลัมน์ขวา วิธีแก้คือตอนสั่ง usepackage ให้ใช้แบบนี้แทน

[code lang="latex"]
\usepackage[switch]{lineno}
[/code]

ที่มา:
<ul>
	<li><a href="http://www.ctan.org/tex-archive/macros/latex/contrib/lineno">http://www.ctan.org/tex-archive/macros/latex/contrib/lineno</a></li>
</ul>
