Title: break ตอนเกิด exception ใน PyDev 
Date: 2012-06-02 07:27:39
Tags: eclipse, python 
Slug: break ตอนเกิด exception ใน PyDev 


ใครใช้ PyDev+Eclipse ในการเขียน Python แล้วอยากให้โปรแกรม break หรือหยุดรัน ณ จุดที่เกิด exception ให้เปลี่ยน perspective เป็น debug ก่อนโดย Window -&gt; Open perspective เลือก debug แล้วต่อด้วย Run -&gt; Manage Python Exception Breakpoints (เมนูนี้จะไม่แสดงให้เห็นถ้าไม่อยู่ในโหมด debug) จะเห็นหน้าต่างแบบนี้

<img class="aligncenter  wp-image-992" title="Screenshot from 2012-06-02 14:24:56" src="http://wittawat.com/blog/wp-content/uploads/2012/06/Screenshot-from-2012-06-02-142456.png" alt="" width="340" height="482" />

ให้เลือก exception ที่อยากได้ แล้วเลือกข้างล่าง 2 ช่องนั่นด้วย (Suspen on...) แค่นี้ แล้วเวลารัน debug มันจะหยุดตรงที่มี exception

ที่มา: <a href="http://stackoverflow.com/questions/455552/break-on-exception-in-pydev">http://stackoverflow.com/questions/455552/break-on-exception-in-pydev</a>
