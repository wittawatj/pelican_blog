Title: โปรแกรม Java บน Linux ไม่รับ input จาก keyboard 
Date: 2011-02-18 06:25:14
Tags: java, linux, netbeans, scim, ubuntu 
Slug: โปรแกรม Java บน Linux ไม่รับ input จาก keyboard 


ผู้ที่รันโปรแกรม Java บน Linux น่าจะเคยเจอปัญหาที่อยู่ดีๆก็ไม่สามารถใช้งาน keyboard ได้ ยกตัวอย่างเช่น เวลาใช้งาน Netbeans หลังจากสลับหน้าจอไปดูโปรแกรมอื่นแล้วสลับกลับมาที่ Netbeans ใหม่ จะไม่สามารถพิมพ์อะไรไปที่ editor ของ Netbeans ได้ ปัญหานี้บางทีก็เกิดกับโปรแกรม GUI เก่าที่เขียนด้วย Tcl เก่าๆเหมือนกัน

วิธีแก้ที่ลองแล้วได้ผล (Ubuntu 10.10, Gnome Desktop, SCIM input) คือ ให้รันคำสั่งนี้ (3 คำสั่ง) ที่ shell

[bash]

XMODIFIERS=&quot;&quot;
export XMODIFIERS
bash

[/bash]

ความหมายคือ เคลียร์ค่า XMODIFIERS (ซึ่งผู้เขียนก็ไม่ทราบว่ามันเอาไว้ทำอะไร) แล้วเปิด bash shell อันใหม่ จากนั้นจึงค่อยเปิด Netbeans ใหม่ใน shell นั้น (ในกรณีนี้ใช้ shortcut บน Desktop ไม่ได้ ต้องเริ่ม Netbeans จาก shell นี้) วิธีนี้จะส่งผลให้ไม่สามารถใช้ input method อย่าง SCIM บน Netbeans ได้ แปลว่าจะพิมพ์ไทยไม่ได้
