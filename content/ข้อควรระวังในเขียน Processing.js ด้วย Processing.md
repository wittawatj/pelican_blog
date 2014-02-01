Title: ข้อควรระวังในเขียน Processing.js ด้วย Processing 
Date: 2013-05-13 02:44:44
Tags: Processing 
Slug: ข้อควรระวังในเขียน Processing.js ด้วย Processing 

เราสามารถเขียน Processing ทีเดียวแล้วได้ทั้งโปรแกรมบนเครื่องและโปรแกรมบนเว็บโดยการ export แต่จากประสบการณ์ที่ลองใช้ Processing 2.0b8 และ Processing.js 1.4.1  แล้ว ยังมีเรื่องที่แปลกๆอยู่บ้างถ้าไม่ระวัง ดังนี้
<ul>
	<li><span style="line-height: 12.997159004211426px;"><strong>method ใน class ชื่อ length()</strong> ใน Processing ดูเหมือนว่าการตั้งใช้ method จะไม่มีข้อจำกัดอะไร แต่ถ้าคิดจะ export ก็ควรคิดด้วยว่าชื่อที่ใช้จะไปตรงกับอะไรใน Javascript หรือไม่ ในตัวอย่างนี้คือ length() ซึ่งไปตรงกับอะไรบางอย่าง ก็ต้องเลี่ยงไปใช้ชื่ออื่น</span></li>
	<li><strong>event</strong> การเขียนโปรแกรม visualization แบบนี้ มักมี loop ใหญ่หนึ่งอันเป็นตัว update การ draw ปัญหาเกิดเมื่อ semantic ของการ update นี้ต่างกันนิดหน่อย  ตัวอย่างเช่น เราจะทำให้ลูกบอลเด้งผนังซ้าย เลยเช็คว่าถ้า x ติดลบแล้วให้กลับเครื่องหมายของทิศทางของ x ตรงนี้ใน Processing อาจใช้งานได้ดี แต่พอ export แล้วตอน x&lt;0 ทิศทางกลับโดน update หลายครั้ง ทำให้ใช้ไม่ได้ เป็นต้น ตรงนี้อธิบายให้เห็นภาพยาก</li>
	<li><strong>type coercion</strong> เรื่องแปลง float/int อย่างอัตโนมัติควรเลี่ยงเพื่อความแน่นอน ควรใส่ (int) , (float) เพื่อ cast ให้ชัดๆดีกว่า</li>
	<li><strong>this</strong> ไม่ได้เจอกับตัวแต่ในอินเตอร์เน็ตบอกว่าถ้าจะอ้างอิงตัวแปร local ใน class ให้ใส่ this เสมอ</li>
	<li><strong>library</strong> Processing มี library มากมาย แต่ถ้าคิดจะ export ห้ามใช้ library ที่ไม่รองรับใน Processing.js  ถ้าอยากรู้ว่าใช้ class/function อะไรที่มีอยู่แล้วได้บ้างให้ดูที่<a href="http://processingjs.org/reference/">หน้า reference ของ Processing.js</a> (ที่สำคัญคือ ArrayList ใช้ได้)</li>
	<li><strong>ตัวแปร global</strong> ใน Processing เราสามารถสร้างตัวแปร global ได้ ชื่อของตัวแปรพวกนี้เข้าใจว่าไม่ต้องเป็นห่วงว่าจะชนกับใน Javascript หรือไม่ เพราะตอนรันทั้งโปรแกรมเราจะอยู่ใน scope ของ function นึงใน Javascript</li>
</ul>
ข้อแนะนำ
<ul>
	<li><span style="font-size: 13px; line-height: 19px;">วิธี debug ง่ายๆคือใช้คำสั่ง println(...) ซึ่งจะ print ออกมาทั้งตอนรันใน Processing และบนเว็บ</span></li>
	<li>มีหลาย class ที่ Processing เอามาจาก Java เลย เช่น ArrayList กรณีนี้ถ้าอยากใช้ method ที่เคยใช้ใน Java ก็ลองเปิด reference ของ Java ดู อาจจะใช้ได้ก็ได้</li>
</ul>
