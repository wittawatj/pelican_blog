Title: equals() และ hashCode() ใน Java 
Date: 2009-03-26 06:15:25
Tags: java 
Slug: equals() และ hashCode() ใน Java 


ช่วงนี้ต้องเขียนโปรแกรมบางอย่างที่ต้องสน performance แบบสุดๆ ต้องใช้พวก hashtable เยอะ การ hash ใน Java ก็จะต้องยุ่งกับ method 2 อัน คือ equals() และ hashCode()

equals(Object obj) เป็น method หนึ่งใน class Object ในภาษา Java ใช้เพื่อเปรียบเทียบว่า obj นี่ส่งเข้าเป็นเป็น argument นี้เท่ากับ object ที่ equals() ถูกเรียกรึป่าว ปกติจะจำเป็นต้องใช้เวลาจะเปรียบเทียบ String 2 อันว่าเหมือนกันมั้ย ใช้ str1 == str2 ไม่ได้ เพราะทำแบบนี้แค่เปรียบเทียบ reference ต้องใช้ str1.equals(str2) ถึงจะ work

ส่วน hashCode() เป็น method สำหรับหาค่า hash ของ object ใดๆ เพื่อเอาไปใช้กับ hashing algorithm ต่างๆ โดย Java Doc API กำหนดไว้ว่า ถ้า obj1.equals(obj2) แล้ว obj1.hashCode() == obj2.hashCode(). แปลว่าถ้า obj1 เท่ากับ obj2 แล้ว ค่า hash ของทั้งสอง object ต้องเท่ากัน แต่ถ้าค่า hash ของ 2 object เท่ากัน ไม่จำเป็นว่า obj1.equals(obj2) ต้องเป็นจริง

รายละเอียดยังมีอีกเยอะ เช่น
<ul>
	<li>hashCode() ที่ดีควรจะไม่ทำให้เกิด collision บ่อย (ซึ่งจะทำให้ performance ของ hash table แย่ลง)</li>
	<li>equals() ต้องเป็น reflexive, symmetric และ transitive (ถ้ามอง equals() เป็น binary relation แล้ว equals() ต้องเป็น equivalence relation)</li>
	<li>obj.hashCode() ต้องคืนค่าเดิมตลอดการ run ครั้งหนึ่ง ถ้า state ของ obj ข้างในไม่มีอะไรเปลี่ยนแปลง</li>
	<li>และอื่นๆอีก</li>
</ul>
มีเว็บดีๆอันหนึ่งที่ไปเจอมาพูดเรื่องนี้ละเอียดมาก อยู่ที่นี่ <a href="http://www.geocities.com/technofundo/tech/java/equalhash.html">http://www.geocities.com/technofundo/tech/java/equalhash.html</a>

[ad#afterpost]
