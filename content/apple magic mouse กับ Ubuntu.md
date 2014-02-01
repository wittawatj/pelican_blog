Title: apple magic mouse กับ Ubuntu 
Date: 2011-09-17 05:04:11
Tags: apple, ubuntu 
Slug: apple magic mouse กับ Ubuntu 


Ubuntu (Linux รุ่นอื่นๆด้วย?) เวอร์ชั่นหลังๆสามารถใช้งาน apple magic mouse ได้เลยโดยไม่มีอะไรต้องทำให้ยุ่งยาก แต่อาจจะใช้ gesture recognition ไม่ได้เท่านั้นเอง ปัญหาที่เจอคือ mouse เร็วๆเกินไป ถึงแม้จะเข้าไปตั้งใน Preferences -&gt; Mouse ให้ Acceleration ต่ำสุดก็ยังเร็วอยู่ดี วิธีแก้คือ รันคำสั่ง

[bash]xinput --list[/bash]

จะเห็นเป็นรายการอุปกรณ์ต่างๆ ให้หา Apple magic mouse แล้วจำ id ไว้ สมมติว่า id=13 จากนั้นตั้ง deceleration เพื่อให้มันช้าลงด้วยคำสั่ง

[bash]xinput --set-prop 13  &quot;Device Accel Constant Deceleration&quot; 1.5 [/bash]

ตรง 1.5 สามารถเปลี่ยนให้มากขึ้นได้ จะยิ่งช้าลง

จาก <a href="http://numberformatdata.wordpress.com/2011/05/08/apple-magic-mouse-works-with-ubuntu/">http://numberformatdata.wordpress.com/2011/05/08/apple-magic-mouse-works-with-ubuntu/</a>
