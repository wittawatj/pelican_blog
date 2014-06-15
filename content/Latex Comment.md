Title: Latex Comment 
Date: 2008-11-01 11:42:49
Tags: latex 
Slug: Latex Comment 


ปกติเวลาจะเขียน comment ใน Latex เราก็แค่พิมพ์ % ไว้หน้าบรรทัด แล้วทั้งบรรทัดนั้นก็จะกลายเป็น comment ทันที วิธีนี้คล้ายๆกับ // ในภาษา Java แต่มักจะเกิดความไม่สะดวกเมื่อต้องการ comment หลายๆบรรทัด

วิธีหนึ่งที่ทำได้ก็ใช้ package ที่ชื่อ verbatim (ใส่ \usepackage{verbatim} ไว้ก่อน \begin{document}) แล้วก็ใช้คำสั่ง
<blockquote>\begin{comment}
....พิมพ์ comment หลายๆบรรทัดไว้ตรงนี้ได้
\end{comment}</blockquote>
แต่ปัญหาก็คือขี้เกียจมานั่งพิมพ์คำว่า \begin{comment} อะไรพวกนี้เพราะมันยาว อีกวิธีที่ทำได้ก็คือสร้างคำสั่งใหม่ขึ้นมาโดยที่คำสั่งนี้รับหนึ่ง argument ก็คือ comment นั่นเอง แล้วคำสั่งนี้ก็ไม่ทำอะไรเลย สมมติว่าอยากได้คำสั่งใหม่ชื่อ C เราก็ทำแบบนี้
<blockquote>\newcommand{\C}[1]{}</blockquote>
คำสั่งนี้รับหนึ่ง argument แต่ไม่ทำอะไรเลย ประโยชน์ก็คือเอาไว้ใช้ทำเป็น comment ได้ เช่น
<blockquote>\C{เอา comment ใส่ไว้ในนี้ หลายบรรทัดก็ได้}</blockquote>
ถ้าทำแบบนี้เราก็จะได้ที่เอาไว้เขียน comment หลายๆบรรทัดได้
