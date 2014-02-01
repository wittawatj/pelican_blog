Title: ใส่ผลงานตีพิมพ์ใน resume โดยใช้ bibtex 
Date: 2012-11-05 04:53:53
Tags: latex 
Slug: ใส่ผลงานตีพิมพ์ใน resume โดยใช้ bibtex 


ปกติ bibtex จะไม่แสดง paper ที่ไม่ได้ถูกอ้างอิงในเนื้อหา แต่บางทีเราอยากให้มันแสดงออกมา เช่นตอนเขียน resume เราอยากให้ bibtex แสดงรายการผลงานของเราทั้งหมด เราสามารถทำได้ด้วย code นี้ สมมติว่าไฟล์ bib ชื่อ mypapers.bib มีผลงานของเราทั้งหมด

[code language="latex"]
\nocite{*}
\bibliographystyle{unsrt}
\bibliography{mypapers}
[/code]

ที่ใช้ style unsrt เพราะคิดว่าดีที่สุดเพื่อการนี้ ถ้าเป็น style อื่นส่วนมากจะแสดง key สำหรับการอ้างอิงมาด้วย ซึ่งไม่จำเป็น คำสั่ง \nocite เอาไว้บอกว่าต้องการให้ key ไหนถูกแสดงออกมา ในที่นี้เราใส่ * เพื่อให้แสดงทุก key

ส่วนใหญ่การแสดงรายการ paper ของตัวเองแบบนี้ มักอยากจะ highlight ชื่อตัวเอง วิธีที่ง่ายที่สุดคือ ตอนเขียนชื่อตัวเองในไฟล์ bib ให้ครอบชื่อด้วย \textbf เพื่อให้มันหนา แต่วิธีนี้เอาการแสดงผลไปรวมกับข้อมูล bib ซึ่งไม่ค่อยสะดวก เพราะทุกครั้งที่อยากเพิ่มรายการใหม่ก็ต้องใส่ \textbf ตลอด และไฟล์ bib นี้เอาไปใช้ในบทความอื่นลำบากด้วย เนื่องจากชื่อตัวเองเป็นตัวหนาอยู่ วิธีที่ดีกว่าคือให้ใส่ code ต่อไปนี้ที่หัวของไฟล์ tex

[code language="latex"]
\usepackage{xstring}

\let\originalbibitem\bibitem
\def\bibitem#1#2\par{%
\noexpandarg
\originalbibitem{#1}
\StrSubstitute{#2}{Your Name}{\textbf{Your Name}}\par}
[/code]

หลักการของ code นี้ง่ายๆ คือแทนที่ Your Name ที่อยู่ใน bibitem (อยู่ในไฟล์ bbl) ด้วย \textbf{Your Name} อย่าลืมแก้ Your Name เป็นชื่อตัวเองด้วย

มีอีกหลายวิธีที่ดีกว่า วิธีที่ตรงตัวที่สุดคือไปแก้ bibliography style (.bst) แต่รู้สึกยุ่งกว่า ดูได้<a href="http://tex.stackexchange.com/questions/33330/make-one-authors-name-bold-every-time-it-shows-up-in-the-bibliography">ที่นี่</a>และ<a href="http://tex.stackexchange.com/questions/18664/underline-my-name-in-the-bibliography">ที่นี่ </a>
