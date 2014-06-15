Title: Executable Jar กับ Netbeans 6.x 
Date: 2010-03-19 03:15:03
Tags: java, netbeans 
Slug: Executable Jar กับ Netbeans 6.x 


ปกติหากใช้ Netbeans ในการเขียน Java จะเห็นว่าทุกครั้งที่ build จะมีโฟลเดอร์ชื่อ dist เกิดขึ้นมาในโฟลเดอร์โปรเจค ซึ่งในนั้นจะมี jar ที่เกิดจากการ compile code ในโปรเจคของเรา และจะสามารถ double click เพื่อรันได้เลย (หรือใช้ java -jar บน command line) หากมีการตั้ง main class ไว้

ปัญหาคือว่าบางทีถึงแม้มีการตั้ง main class ใน Netbeans ไว้แล้ว แต่เจ้า jar ที่มันสร้างให้ดันไม่สามารถรันได้ นั่นคือ double click ก็ไม่ได้ ใช้ java -jar ก็บอกหา main class ไม่เจอ หากลองเปิดไฟล์ manifest ใน jar ดูจะพบว่ามันไม่ได้เขียน entry "Main-Class" ไว้ จึงไม่แปลกที่มันรันไม่ได้

เหตุผลที่มันไม่ใส่ไว้ให้มีหลายกรณี
<ul>
	<li>import project มาจาก Eclipse มีที อาจมี config อะไรบางอย่างไม่ตรง</li>
	<li>ตอนสร้างโปรเจคใน Netbeans เลือกเป็น Java library ไม่ได้เลือก Java application</li>
</ul>
<h1>วิธีแก้</h1>
เปิดไฟล์ PROJECTPATH/nbproject/project.properties เพิ่ม [code]manifest.file=manifest.mf[/code]

ลงไป แค่นี้ก็จะมี entry "Main-Class" ขึ้นมาใน manifest แล้ว jar ก็จะรันได้
<h1>อ้างอิง</h1>
<ul>
	<li><a href="http://wiki.netbeans.org/FaqNoMainClass">http://wiki.netbeans.org/FaqNoMainClass</a></li>
</ul>
