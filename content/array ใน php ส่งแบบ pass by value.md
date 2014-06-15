Title: array ใน php ส่งแบบ pass by value 
Date: 2011-01-02 14:06:57
Tags: php 
Slug: array ใน php ส่งแบบ pass by value 


จดไว้เตือนความจำตัวเอง ย้ำอีกครั้งว่า php ส่ง array แบบ pass by value (ใช้ php 5.2.15) ถ้าไม่บอกมันว่าให้ส่งแบบ pass by reference ที่มาเขียนนี่เพราะด้วยเหตุผลอะไรบางอย่าง ในสมองตัวเองบอกว่าส่ง array ไปก็น่าจะเป็นแบบ pass by reference ไม่รู้ทำไมถึงคิดแบบนั้นโดยที่ไม่เอะใจอะไรเลย ทำให้เกิด bug และหาอยู่นานมาก

ถ้าทำแบบนี้จะเป็น pass by value

[php]function byvalue($arr){} [/php]

แบบนี้ถึงจะเป็น pass by reference

[php]function byref(&amp;$arr){} [/php]

สังเกตตรงเครื่องหมาย &amp; ที่ argument ดีๆ
