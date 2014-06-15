Title: Ubuntu 9.04 กับ Lenovo Y450 P8700 
Date: 2009-08-04 03:39:44
Tags: laptop, ubuntu 
Slug: Ubuntu 9.04 กับ Lenovo Y450 P8700 


โพสนี้เขียนขึ้นเพื่อรวมปัญหาที่พบหลังจากลง Ubuntu 9.04 บน Lenovo Y450 P8700 ต่อไปนี้เป็นปัญหา
<ol>
	<li><strong>แรม 4 GB เห็น 2.9 GB </strong>ประเด็นนี้หลายๆที่บอกว่าเป็นเรื่องปกติสำหรับระบบ 32 bits เนื่องจาก OS ดึงพื้นที่แรมบางส่วนไปใช้สำหรับ MMIO (Memory-Mapped IO) ดังนั้นแรมจึงเหมือนถูกขโมยไปแบบช่วยไม่ได้ แต่ก็ยังมีวิธีแก้คือให้ลง Kernel ที่มี PAE (Physical Address Extension) ก็จะทำให้ระบบเห็นแรมได้มากขึ้น โดยใช้คำสั่งนี้ [bash] sudo apt-get install linux-headers-server linux-image-server linux-server[/bash]

จากนั้น reboot หนึ่งครั้ง ก่อนเลือกเข้า Ubuntu จะเห็นว่ามี menu เพิ่มขึ้นมา เป็น Kernel อันใหม่นั่นเอง ให้เลือกอันนั้น (ปกติจะเพิ่มขึ้นมาเป็นแถวแรก) boot เสร็จก็จะเห็นแรม 3.9 GB (คาดว่าอีก 100 MB OS คงต้องใช้จริงๆ ให้มันไปเถอะ)</li>
	<li><strong>ปรับความสว่างของหน้าจอไม่ได้</strong> ปัญหานี้จริงๆแล้วไม่เกิดแต่ต้น ตอนลง Ubuntu เสร็จจะเห็นว่า key ลัดทั้งหลายบน keyboard จะใช้ได้ดี (ปรับเสียง, ปรับความสว่าง) แต่ภาพจะไม่ค่อยลื่น เช่นเวลา scroll mouse อ่านเว็บจะเห็นว่ามันกระตุกๆเล็กน้อย วิธีแก้ก็คือเปิดใช้ driver ของ nVidia ซะ โดยใช้คำสั่ง [bash]sudo nvidia-xconfig[/bash]

แต่ที่นี้พอเปิดแล้วเนี่ยปุ่มความสว่างดันทำงานไม่ได้ คือกดปุ่มแล้วจะมีหน้าต่างขึ้นมาเหมือนกับว่ากำลังปรับความสว่างให้อยู่แต่จริงๆความสว่างไม่เปลี่ยนเลย ใช้ Brightness Applet ของ GNome ก็ไม่มีผลเหมือนกัน เว็บส่วนใหญ่จะบอกว่าให้ลองใส่

[source]acpi_backlight=vendor[/source]

ด้านหลังของ Kernel parameter (ใส่ก่อน boot น่ะ) แต่วิธีนี้ก็ไม่ช่วยแต่อย่างใด วิธีแก้ก็มี 2 วิธี (เท่าที่รู้ตอนนี้)
<ol>
	<li>ปิด nVidia driver ซะแล้วก็ใช้ปุ่มปรับบน keyboard ตามปกติ แต่ว่าภาพจะไม่ลื่น</li>
	<li>ปรับความสว่างผ่าน UI ของ nVidia แทนโดยไปที่ System -&gt; Administration -&gt; NVIDIA X Server Settings ตรงแทบด้านซ้ายเลือก X Server Color Correction แล้วปรับ scrollbar ที่เขียนว่า brightness ก็เรียบร้อย</li>
</ol>
</li>
	<li><strong>ภาษาไทยกับ Openoffice Writer </strong>อันนี้ไม่ใช่ประเด็นอะไรเกี่ยวกับ Lenovo เลย แต่เป็นเรื่องของ Openoffice Writer ที่ใช้ Style ภาษาไทยไม่ได้ ปกติเวลาพิมพ์งานเรามักจะตั้งค่า style ของส่วนของเอกสารได้ เช่น heading 1, heading 2, text body เป็นต้น style แต่ละอันเหล่านี้จะคู่กับภาษาด้วย เช่นเราอาจตั้ง text body สำหรับภาษาไทยเป็น Tahoma 10 เป็นต้น ปัญหาก็คือตรงที่ตั้ง style มันไม่มีภาษาไทยให้เลือก ผลก็คือ style ที่มีอยู่ ไม่ว่าจะตั้ง font ตั้งขนาดอย่างไรก็ไม่เป็นผลกับข้อความภาษาไทย วิธีแก้คือ ไปที่ Tools -&gt; Options คลิกด้านซ้าย Language Settings -&gt; Languages  ตั้ง CTL ให้เป็น Thai ดังภาพ
<img class="aligncenter size-full wp-image-188" title="Screenshot-Options - Language Settings - Languages" src="http://wittawat.com/blog/wp-content/uploads/2009/08/Screenshot-Options-Language-Settings-Languages2.png" alt="Screenshot-Options - Language Settings - Languages" width="462" height="221" />
จากนั้นจะมีภาษาไทยขึ้นมาให้เลือกตอนเราแก้ไข Style วิธีนี้มั่วเอาเองแล้วมันได้</li>
</ol>
ที่มา:
<ol>
	<li><a href="http://www.cyberciti.biz/faq/ubuntu-linux-4gb-ram-limitation-solution/">http://www.cyberciti.biz/faq/ubuntu-linux-4gb-ram-limitation-solution/</a></li>
	<li><a href="http://patchwork.kernel.org/patch/35312/">http://patchwork.kernel.org/patch/35312/</a></li>
</ol>
[ad#afterpost]
