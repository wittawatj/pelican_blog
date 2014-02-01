Title: การใช้ disk quota บน Linux 
Date: 2011-08-28 03:55:56
Tags: disk quota, linux, ubuntu 
Slug: การใช้ disk quota บน Linux 


มีโอกาสได้ลองใช้ disk quota บน Linux เป็นครั้งแรก เลยมาจดไว้หน่อย (อาจจะมั่วบ้าง)
<h1>Disk quota คือ ?</h1>
disk quota คือนโยบายจำกัดเนื้อที่การใช้งาน disk ของผู้ใช้ สามารถตั้งเป็นรายคนหรือเป็น group ก็ได้ ที่ใช้อยู่คือเป็นแบบรายคน คือกำหนดไปเลยว่าใครใช้ได้มากเท่าไหร่ สำหรับแบบ group นี่ไม่เข้าใจว่าความหมายคืออะไร หมายถึงผลรวมของคนในกลุ่ม หรือหมายถึงแต่ละคนในกลุ่ม แล้วถ้าใช้ 2 แบบจะเป็นอย่างไร ไม่ได้ลองเพราะตั้งรายคนเพียงพอกับที่อยากได้

ปกติการจำกัดเนื้อที่มี  2 แบบคือ soft limit กับ hard limit
<ul>
	<li>Hard limit หมายถึง ปริมาณเนื้อที่ที่ใช้งานได้จริงๆ หากเกิน limit นี้จะไม่สามารถเขียน disk ได้</li>
	<li>Soft limit หมายถึง ปริมาณเนื้อที่ที่ผู้ใช้ไม่ควรเกิน หากเกินก็ยังสามารถใช้งานได้ตามปกติ แต่สิ่งที่เรียกว่า "grace period" จะเริ่มขึ้น grace period คือช่วงเวลาที่ผู้ใช้ควรจะทำให้เนื้อที่ที่ตัวเองใช้ ไม่เกิน limit ที่กำหนดไว้ ปกติ grace period จะถูกตั้งไว้ที่ 7 วัน (สามารถเปลี่ยนได้) แปลว่าหากผู้ใช้ใช้เนื้อที่เกินที่กำหนด เกินกว่า 7 วันแล้ว soft limit จะกลายเป็น hard limit แปลว่าผู้ใช้จะไม่สามารถเขียน disk ได้ ถ้าอยากเขียนได้อีกก็ต้องลบอะไรบางอย่างทิ้งเพื่อให้การใช้งานต่ำกว่า limit แล้ว grace period ก็จะหายไป</li>
</ul>
ขั้นตอนการติดตั้งสามารถดูได้ที่เว็บอ้างอิงข้างล่าง เมื่อติดตั้งเสร็จแล้วตอนรัน quotacheck จะใช้เวลาค่อนข้างนาน เตรียมเวลาไว้ให้พร้อม จากนั้นต่อด้วย

[bash]quotaon -av [/bash]

เพื่อเปิดการใช้การ quota หลังจากนี้สามารถเช็คการใช้งานและ quota ของผู้ใช้ทุกคนได้ด้วย

[bash]sudo repquota -as[/bash]

ซึ่งจะ update แบบ real-time โดยอัตโนมัติ
<h1>Disk Quota กับ NFS</h1>
disk quota สามารถใช้กับ NFS ได้ ตัวอย่างเช่น มีเครื่องหนึ่งชื่อ nas ทำหน้าที่เป็น harddisk เก็บ /home และมีเครื่องอื่นๆ com1, com2 ที่ mount /home บน nas ด้วย NFS แล้วเราอยากกำหนด disk quota กรณีนี้ให้กำหนด disk quota ที่ nas คือตอน mount /home บน nas (หรืออาจจะเป็น / บน nas) ให้ใส่ option usrquota (quota สำหรับ user), และ/หรือ grpquota (quota สำหรับ group) ที่ fstab ดังนี้

[code]/dev/sda1 /home ext2 defaults,usrquota,grpquota 1 1[/code]

หรือถ้าใช้ <a href="http://en.wikipedia.org/wiki/Journaling_file_system">Journaling file system </a>เช่น ext3, ext4 อาจใส่ option แบบนี้ก็ได้

[code]/dev/sda1 /home ext2 defaults,usrjquota=aquota.user,jqfmt=vfsv0 1 1[/code]

ผู้ใช้สามารถเช็คการใช้งานของตัวเองได้ด้วย

[bash]quota -s[/bash]

ปกติคำสั่งนี้จะใช้ได้บน nas เท่านั้น หากอยากใช้บน com1, com2 ด้วยก็ให้ติดตั้ง quota package บน com1, com2 แล้วรัน RPC daemon บน nas เพื่อทำหน้าที่รับ RPC จาก com1, com2 เวลาที่คำสั่ง quota ถูกใช้งาน วิธีเริ่ม daemon ของ quota ให้รันคำสั่ง

[bash]rpc.rquotad[/bash]

บน nas แค่นี้ก็ใช้ได้แล้ว

อ้างอิง
<ul>
	<li><a href="https://wiki.archlinux.org/index.php/Disk_Quota#Journaled_quota">https://wiki.archlinux.org/index.php/Disk_Quota#Journaled_quota</a></li>
	<li><a href="http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch28_:_Managing_Disk_Usage_with_Quotas">http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch28_:_Managing_Disk_Usage_with_Quotas</a></li>
</ul>
[ad#afterpost]
