Title: Ubuntu เสียงหาย 
Date: 2010-07-18 05:58:33
Tags: ubuntu 
Slug: Ubuntu เสียงหาย 


ใช้งาน Ubuntu อยู่ดีๆแล้วเสียงก็หายไป กลายเป็นไม่ว่าจะเล่นเพลงอะไรก็ได้ยินแต่ noise ซ่าๆ วิธีแก้ให้ลองใช้คำสั่ง

[bash]sudo /etc/init.d/alsa-utils reset [/bash]

เพื่อ reset ALSA ซะ ทำได้โดยไม่ต้องปิดโปรแกรมที่กำลังใช้งานเสียงอยู่

ที่มา
<ul>
	<li>ht<a href="http://ubuntuforums.org/showthread.php?p=2742327">tp://ubuntuforums.org/showthread.php?p=2742327</a></li>
</ul>
