Title: กู้ข้อมูลที่ลบไปแล้วจาก iphone โดยใช้ Ubuntu 
Date: 2010-05-23 05:07:10
Tags: iphone 
Slug: กู้ข้อมูลที่ลบไปแล้วจาก iphone โดยใช้ Ubuntu 


<strong>UPDATE (มิ.ย. 2555): บทความนี้เขียนขึ้นนานมากแล้ว ผู้เขียนใช้ iphone รุ่นแรก เนื่องจากผู้เขียนไม่มี iphone รุ่นใหม่ๆให้ลองทำ จึงไม่สามารถช่วยอะไรได้หากติดปัญหา และมีความเป็นไปได้สูงมากที่วิธีนี้จะใช้กับรุ่นใหม่ๆไม่ได้ แต่ถ้าอยากลองก็เชิญครับ</strong> <strong>ผู้เขียนไม่ขอรับผิดชอบต่อความเสียหายที่เกิดขึ้นนะ</strong>

เรื่องนี้เคยเขียนไปครั้งหนึ่งแล้วที่ <a href="http://wittawat.com/blog/?p=84">http://wittawat.com/blog/?p=84</a> แต่ไม่ค่อยละเอียด เลยเอามาขยายความที่นี่อีกครั้ง ครั้งนี้มีรูปประกอบเพื่อให้เป็นประโยชน์มากขึ้น

ต้องขอบอกก่อนว่าผมไม่ใช่ผู้เชี่ยวชาญ iPhone แต่อย่างใด ไม่รู้ว่าเขามีวิธีกู้ข้อมูลด้วย iTune หรือโปรแกรมอื่นๆอะไรรึป่าว แต่ผมค่อนข้างมั่นใจว่าวิธีที่ใช้นี้สามารถใช้ได้กับ iPhone ทุกรุ่น เพราะวิธีนี้เป็นวิธีที่ไม่ต้องการอะไรพิเศษจากเครื่อง iphone เลย เป็นวิธีค่อนข้างจะโบราณ แต่อาจจะยุ่งยากซักหน่อยครับ บทความนี้จะกล่าวถึงการกู้ข้อมูลโดยใช้ Ubuntu มาช่วย (<strong>ผู้ใช้ Linux รุ่นอื่นก็สามารถทำได้เช่นกัน</strong>) สิ่งที่ต้องการสำหรับการกู้ข้อมูลด้วยวิธีนี้คือ
<ol>
	<li>iPhone ที่มี terminal (สำหรับผู้ไม่คุ้นเคย Terminal ก็คือโปรแกรมบน iphone ที่เปิดมาแล้วเห็นแต่หน้าจอดำๆมีปุ่ม keyboard ให้พิมพ์คำสั่ง เหมือน dos บน Windows ) โปรแกรมชื่อ vterminal หรือ MobileTerminal</li>
	<li>สาย USB กับปลั๊กไฟเพื่อชาร์จไฟ อันนี้จำเป็นครับเพราะต้อง copy ข้อมูลนาน เดี๋ยวแบตหมดกลางทาง (copy ผ่าน wireless LAN)</li>
	<li>คอมอีกหนึ่งเครื่องที่มีสิ่งต่อไปนี้
<ol>
	<li>Wireless LAN เพื่อติดต่อกับ iPhone (จะเป็นคอมตั้งโต๊ะแล้วเชื่อมกับ Wireless router ก็ได้ ขอแค่ wireless กับคอม)</li>
	<li>เนื้อที่บนเครื่องนั้นอย่างน้อยเท่ากับความจุของ iPhone คุณ (ของผมใช้ iPhone รุ่นเก่าจุ 8GB ฉะนั้นเครื่องคอมอีกเครื่องต้องเตรียมไว้ 8 GB) รุ่นใหม่อาจต้องใช้ 32 GB</li>
	<li>SSH Server ซึ่งเป็นโปรแกรมที่ผู้ใช้สามารถ login เข้าไปเพื่อรันคำสั่งได้ SSH Server นี้ต้องอยู่บนคอมเครื่องนั้น เพราะเราจะให้ iPhone login เข้าไปแล้วถ่ายข้อมูลเก็บไว้</li>
	<li>โปรแกรม Photorec (<a href="http://www.cgsecurity.org/wiki/PhotoRec">http://www.cgsecurity.org/wiki/PhotoRec</a>) สามารถโหลดได้ฟรี มีทั้ง Windows และ Linux</li>
</ol>
</li>
	<li>เวลาหลายชั่วโมง</li>
</ol>
<strong>เรากำลังจะทำอะไรกัน?</strong>

หลักการของการกู้ข้อมูลนี้คือเราจะทำการคัดลอกข้อมูลทั้งหมดใน disk ของ iphone ออกมา การคัดลอกนี้ไม่ใช่ copy ทุกไฟล์ แต่เราจะต้องคัดลอกทุกส่วนทุกมุมของ disk เลยเพื่อจะได้เอามาวิเคราะห์ทีหลังว่าส่วนไหนมุมไหนของ disk มีร่องรอยไฟล์เหลืออยู่บ้าง การทำแบบนี้มีข้อดีคือเรามีโอกาสกู้ไฟล์คืนมาได้แม้ format ไปแล้ว ที่ทำแบบนี้ได้ผลเพราะโดยปกติเวลาเรากดลบไฟล์ ไฟล์หรือข้อมูลนั้นๆไม่ได้หายไปจริงๆ แต่ระบบแค่บันทึกไว้บน disk ว่าส่วนนี้ได้ถูกสั่งลบแล้ว สามารถถูกแทนที่ด้วยข้อมูลอื่นๆได้ ก็หมายความว่าถ้าเราสั่งลบอะไรบางอย่าง แล้วเราไม่ได้บันทึกอะไรเพิ่มเลย ก็มีโอกาสที่ disk ส่วนนั้นยังไม่ได้โดนแทนที่ด้วยอะไรใหม่ๆ เราเลยสามารถกู้ได้ ฉะนั้นหากต้องการจะกู้สิ่งที่ลบแล้ว ก็ไม่ควรใช้งานเครื่องจนกว่าจะถึงเวลากู้ เพราะส่วนเก็บข้อมูลอาจโดนอย่างอื่นทับแล้วจะกู้ของเก่าไม่ได้อีก

กลับมาเรื่องการคัดลอก disk ของ iPhone แน่นอนว่าเราไม่สามารถคัดลอกไปใส่ disk เดิมได้ เพราะการคัดลอกนี้เราจะได้ไฟล์ 1 ไฟล์ซึ่งมีขนาดเท่า disk เดิมเลย เป็น raw image ของ disk (เหมือนตอน burn image ของ CD ) นั่นเอง ฉะนั้นเราต้องคัดลอกไปที่อื่นซึ่งก็คือคอมอีกเครื่องที่เตรียมไว้

การคัดลอก disk image ไปอีกเครื่องเราจะใช้ SSH (Secure Shell) บน iPhone โดยใช้ Terminal แล้ว login ไปที่อีกเครื่องหนึ่งซึ่งมี SSH server ลงไว้แล้ว ทำผ่าน wireless LAN เมื่อเชื่อมต่อกันได้แล้วที่เหลือก็แค่รอให้ข้อมูลทั้ง disk ของ iPhone ไปอยู่อีกเครื่องหนึ่ง ขั้นตอนนี้จะนานมาก จากนั้นก็ค่อยใช้โปรแกรม PhotoRec มาหาร่องรอยของไฟล์จาก disk image ที่ได้มาซึ่งอยู่บนคอมอีกเครื่อง PhotoRec เป็นโปรแกรมที่เขียนมาค่อนข้างดี สามารถใช้กู้ไฟล์ได้หลายชนิดมาก รวมถึง รูป เพลง และหนังด้วย ถึงตรงนี้คิดว่าผู้อ่านคงได้ไอเดียแล้วว่าเรากำลังทำอะไร

<strong>เตรียมโปรแกรม</strong>
<ol>
	<li>เตรียม terminal บน iPhone วิธีลงก็ลงเหมือนที่ลงโปรแกรมอื่นๆบน iPhone ครับ ขอไม่กล่าวถึง ลองหาด้วยคำว่า terminal, MobileTerminal, vterminal ดู เมื่อลงเสร็จแล้วเปิดโปรแกรมขึ้นมาจะได้แบบนี้
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/iphone_terminal.png"><img class="aligncenter size-full wp-image-370" title="iphone_terminal" src="http://wittawat.com/blog/wp-content/uploads/2010/05/iphone_terminal.png" alt="" width="320" height="480" /></a></li>
	<li>เนื่องจากเราจะใช้คำสั่ง ssh บน iPhone ซึ่งผมไม่แน่ใจว่ามันมีมาให้กับ terminal หรือยัง วิธีเช็คก็เปิด terminal ขึ้นมาแล้วพิมพ์คำสั่ง[bash]ssh -V[/bash]

(V ตัวใหญ่) ถ้าได้คล้ายๆรูปข้างล่างนี้ก็แปลว่าใช้ได้แล้ว ให้ข้ามไปข้อต่อไปได้เลย
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/ssh_ver.png"><img class="aligncenter size-full wp-image-372" title="ssh_ver" src="http://wittawat.com/blog/wp-content/uploads/2010/05/ssh_ver.png" alt="" width="480" height="320" /></a>แต่ถ้ามันขึ้นคำว่า "command not found" แทนแสดงว่ายังไม่มีคำสั่ง ssh <strong>ให้ลงโปรแกรมชื่อ OpenSSH</strong> วิธีลงก็แบบเดียวกับที่ลง terminal เมื่อลงเสร็จแล้ว กลับมาลองคำสั่งนี้อีกครั้ง มันควรขึ้นเหมือนภาพด้านบนครับ</li>
	<li>เช็คว่ามี SSH Server บนเครื่องคอมมั้ย เนื่องจากบนความนี้เขียนสำหรับคอมที่เป็น Linux วิธีเช็คว่ามี SSH Server มั้ย ก็ให้เปิด terminal ขึ้นมา (ผู้ใช้ Ubuntu ให้ไปที่ Application -&gt; Accessories-&gt; Terminal) แล้วพิมพ์คำสั่ง[bash]netstat -an | less[/bash]

จะได้ประมาณรูปข้างล่าง
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/ssh_port1.png"><img class="aligncenter size-full wp-image-375" title="ssh_port" src="http://wittawat.com/blog/wp-content/uploads/2010/05/ssh_port1.png" alt="" width="650" height="231" /></a>ให้เล็งบรรทัดที่ด้านขวาเป็นคำว่า LISTEN ถ้าเห็น 0.0.0.0:22 แปลว่าเครื่องคอมมี SSH Server แล้ว พร้อมที่จะให้ iPhone login เข้ามา แต่ถ้าหา 22 ไม่เจอแปลว่าเครื่องคอมยังไม่มี SSH Server ให้กด q เพื่อกลับมาที่ terminal เหมือนเดิมแล้วพิมพ์ (สำหรับ Ubuntu )

[bash]sudo apt-get install  openssh-server[/bash]

กด Enter จะให้ใส่ password ของ root ก็ใส่ไปรอซักพักจนมันติดตั้งเสร็จแล้วลงพิมพ์คำสั่งด้านบนเพื่อเช็คใหม่อีกครั้ง ครั้งนี้ควรเห็นเลข 22</li>
	<li>ลงโปรแกรม photorec โดยพิมพ์[bash]sudo apt-get install testdisk[/bash]

หากติดตั้งเสร็จให้ลอง

[bash]photorec -v[/bash]

ถ้าเห็นคล้ายๆรูปข้างล่างแปลว่า photorec ใช้ได้แล้ว (ตัวเลข version ไม่เหมือนกัน ไม่เป็นไร)
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/photorec_ver.png"><img class="aligncenter size-full wp-image-377" title="photorec_ver" src="http://wittawat.com/blog/wp-content/uploads/2010/05/photorec_ver.png" alt="" width="690" height="176" /></a></li>
</ol>
<strong>ขั้นตอนการกู้ข้อมูล</strong>

ถึงขั้นตอนนี้คิดว่าคงเตรียมโปรแกรมต่างๆพร้อมแล้ว เราจะเริ่มโดยการเชื่อมต่อคอมกับ iPhone ผ่าน wireless LAN กันก่อน สำหรับผู้ที่มี router ที่บ้านก็ง่ายหน่อย ก็ให้เข้าไปที่หน้าเลือก wi-fi ของ iPhone แล้วเลือกชื่อ network ของที่บ้านตัวเองก็เสร็จแล้ว สำหรับผู้ใช้คอมที่มี wireless แต่ไม่มี router ก็ให้สร้าง ad-hoc network (ไม่ค่อยถูกแต่พูดแบบง่ายๆ คือ network ที่ไม่มี router ครับ ) ขึ้นมา โดยทำตามขั้นตอนนี้
<ol>
	<li>คลิกที่รูปคอมสองเครื่องด้านขวาบน ดังภาพ
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/nm_start.png"><img class="aligncenter size-full wp-image-378" title="nm_start" src="http://wittawat.com/blog/wp-content/uploads/2010/05/nm_start.png" alt="" width="454" height="81" /></a></li>
	<li>จะมีเมนูขึ้นมา ให้เลือกอันสุดท้าย น่าจะประมาณว่า Create a new network ...</li>
	<li>ใส่ชื่อ network ที่ต้องการลงไป เช่น iphonerec</li>
	<li>เข้าไปที่หน้าเลือก network ของ iPhone แล้วเลือก wi-fi network ที่ชื่อ iphonerec ขั้นตอนนี้บางทีอาจจะมองไม่เห็น iphonerec ขอให้ลองทำเร็วๆ คือสร้าง network ใหม่เสร็จแล้วรีบเปิด iPhone แล้ว connect</li>
	<li>เมื่อเชื่อมต่อสำเร็จ รูปคอมสองเครื่องจะเปลี่ยนเป็นรูปสัญญาณ wi-fi แบบนี้
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/wiki_connected.png"><img class="aligncenter size-full wp-image-379" title="wiki_connected" src="http://wittawat.com/blog/wp-content/uploads/2010/05/wiki_connected.png" alt="" width="388" height="53" /></a></li>
</ol>
<strong>เช็คการเชื่อมต่อไร้สายของคอมกับ iPhone</strong>

อันดับแรกไปที่ terminal <strong>ของคอม</strong> แล้วลองพิมพ์

[bash]ifconfig[/bash]

จะมีรายการของอุปกรณ์การเชื่อมต่อขึ้นมาพรอ้ม IP address ของแต่ละอัน โดยปกติแล้ว wireless LAN card ของคอมจะชื่อ wlan0 ส่วน LAN card แบบสายจะชื่อ eth0 เครื่องคอมส่วนใหญ่จะขึ้นมาแค่ 2 อันนี้ ก็ให้ลองดูส่วนของ wlan0 ซึ่งจะเห็นประมาณนี้
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/ifconfig.png"><img class="aligncenter size-full wp-image-380" title="ifconfig" src="http://wittawat.com/blog/wp-content/uploads/2010/05/ifconfig.png" alt="" width="738" height="161" /></a>ถ้าตรงคำว่า inet address มีเลข IP adress แสดงว่าการเชื่อมต่อฝั่งคอมใช้ได้แล้ว (ad-hoc network บางทีจะเป็น 10.42.43.xx หรือบางทีก็ 169.245.xxx.xx ก็ไม่ได้สำคัญอะไร เป็นแค่เลข IP) <strong>ให้จดเลข IP นี้เอาไว้</strong> ต่อไปนี้จะเรียกว่า <strong>IP ของคอม</strong>

มาลองดูการเชื่อมต่อฝั่ง iPhone บ้าง ให้ไปที่ terminal ของ iPhone แล้วลองพิมพ์

[bash]ping 192.168.1.21[/bash]

แน่นอนให้เปลี่ยน 192.168.1.21 เป็น IP ของคอม ที่จดไว้นะครับ ถ้าได้แบบภาพข้างล่าง
<a href="http://wittawat.com/blog/wp-content/uploads/2010/05/iphone_ping.png"><img class="aligncenter size-full wp-image-382" title="iphone_ping" src="http://wittawat.com/blog/wp-content/uploads/2010/05/iphone_ping.png" alt="" width="480" height="320" /></a>แปลว่า iPhone สามารถมองเห็นเครื่องคอมแล้ว การเชื่อมต่อสมบูรณ์

<strong>เริ่มคัดลอก disk image</strong>

เริ่มคัดลอก disk image ของ iPhone โดยไปที่ terminal ของ iPhone แล้วพิมพ์ (เปลี่ยนบางจุดตามคำอธิบายด้านล่าง)

[bash]dd if=/dev/disk0 | ssh nook@192.168.1.21 'dd of=/home/nook/Desktop/iphonedisk.img'[/bash]

คำสั่งด้านบนมีจุดที่ต้องระวังดังนี้
<ul>
	<li>คำว่า nook คือ username ที่ใช้ login เข้า Linux ให้เปลี่ยนเป็น user ของตัวเอง</li>
	<li>192.168.1.21 คือ IP ของคอม ให้เปลี่ยนเป็น IP ของคอมตัวเองที่จดไว้</li>
	<li><code>/home/nook/Desktop/iphonedisk.img</code> คือตำแหน่งของ disk image ที่อยากได้ ให้เปลี่ยนตรงคำว่า nook เป็น user ตัวเอง ตำแหน่งที่ใช้นี้คือ Desktop แปลว่าเมื่อคัดลอง disk image เสร็จแล้ว จะมีไฟล์ชื่อ iphonedisk.img ปรากฏขึ้นบน Desktop ของคอม และมีขนาดใกล้เคียงกับความจุของ iPhone (ไฟล์ใหญ่ โปรดเตรียมเนื้อที่ไว้ให้พร้อม)</li>
	<li>อย่าลืมเครื่องหมาย ' ที่ท้ายคำสั่ง สั่งเกตุได้จากถ้ากด Enter แล้วมีเครื่องหมาย &gt; ขึ้นมาแปลว่าลืมปิด ' ที่ท้ายคำสั่ง</li>
	<li>ถ้ามีคำถามขึ้นมาว่า "Are you sure you want to continue connecting (yes/no)?" ให้พิมพ์ yes แล้ว Enter</li>
</ul>
ถ้าทำถูกมันจะถาม password ก็ให้พิมพ์ password ที่ใช้ login เข้า Linux ตัวเองลงไป แล้วมันจะนิ่งไปเฉยๆ ซึ่งถือว่าปกติ ถ้าที่ Desktop ของคอมมีไฟล์ชื่อ iphonedisk.img ขึ้นมา ถือว่ามาถูกทางแล้ว ไฟล์นี้จะใหญ่ขึ้นเรื่อยๆเมื่อมัน copy ไปเรื่อยๆ และจะใช้เวลานานมาก (หลายชั่วโมง)

<strong>เริ่มกู้ข้อมูลจาก iphonedisk.img ด้วย photorec</strong>

เมื่อมี disk image ของ iPhone แล้ว ก็สามารถเริ่มขุดคุ้ยร่องรอยของไฟล์ได้ ขั้นตอนกู้ข้อมูลนี้<strong>สามารถทำได้แม้ตอนที่ไฟล์ disk image ยัง copy ไม่เสร็จ</strong> ข้อดีคือถ้าเรากู้ข้อมูลจาก disk image ที่ยัง copy ไม่เสร็จ แล้วเราได้ไฟล์ที่เราต้องการครบแล้ว เราก็สามารถยกเลิกการ copy disk image ได้เลย เพราะเราได้ของครบแล้ว

รัน photorec ด้วยคำสั่ง

[bash]sudo photorec /home/nook/Desktop/iphonedisk.img[/bash]

ขั้นตอนการใช้งาน photorec สามารถดูได้จาก <a href="http://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step">http://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step </a>สำหรับใครที่ทำ photorec จบแล้วได้ folder และไฟล์ออกมาเยอะแยะ ให้ดูหน้า<a title="การหาและกรองไฟล์ด้วยคำสั่ง find" href="http://wittawat.com/blog/?p=1022">วิธีใช้ find</a> เพื่อกรองเอาไฟล์ที่เราอยากได้

เพิ่มเติม
<ul>
	<li><a href="http://smart-mobile.com/forum/viewtopic.php?f=88&amp;t=198542">http://smart-mobile.com/forum/viewtopic.php?f=88&amp;t=198542</a> ผมเองก็ไม่รู้ว่า iPhone รุ่นใหม่ๆทำขั้นตอนไหนได้ไม่ได้ ที่นี่คิดว่ามีคำตอบ</li>
	<li>หลายท่านบอกเข้ามาว่าอ่านแล้วก็ งง ผมก็คงต้องเรียนว่าผมก็พยายามเขียนเป็นขั้นตอนเต็มที่แล้ว จะบอกความเป็นมาของทุก step หรือจะให้บอกดักแก้ error ที่เป็นไปได้ทั้งหมดก็คงจะทำให้บทความยืดเยื้อ เอาไว้จะค่อยๆปรับปรุงครับ</li>
</ul>
