Title: ไอคอนบน desktop ของ Ubuntu หายไป 
Date: 2010-01-26 11:04:33
Tags: ubuntu 
Slug: ไอคอนบน desktop ของ Ubuntu หายไป 


คิดว่าหลายๆคนคงเคยเจออาการที่ใช้งาน Ubuntu อยู่ดีๆ icon ก็หายไปหมด คลิ๊กขวาที่ desktop ก็ไม่ได้ ทำอะไรไม่ได้เลย แถมเปิด nautilus ไม่ได้ด้วย ลองหาแล้วปัญหาเกิดจากเจ้า nautilus นั่นแหละ วิธีแก้มี 2 วิธี
<ol>
	<li>กด alt+f2 จะมีหน้าต่างเล็กๆขึ้นมาเขียนว่า "Run Application" ใส่ nautilus ลงไปแล้วกด run</li>
	<li>ถ้ามันไม่หาย ใช้คำสั่ง gconf-editor แล้วหาไปที่ apps/nautilus/preferences ทางด้านขวามือให้หาคำว่า show_desktop ปกติมันคงมีติ๊กถูกอยู่ ให้ติ๊กออกแล้วติ๊กใหม่ หวังว่าคงหาย</li>
	<li>ถ้าไม่หาย ลองเปิด terminal พิมพ์ nautilus แล้วกด enter</li>
</ol>
ที่มา<a href="https://bugs.launchpad.net/ubuntu/+bug/375713"> https://bugs.launchpad.net/ubuntu/+bug/375713</a>
