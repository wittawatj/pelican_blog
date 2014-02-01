Title: เปลี่ยน mapping ของคีย์บอร์ดด้วย xmodmap 
Date: 2012-05-09 05:26:59
Tags: keyboard, linux, ubuntu, xmodmap 
Slug: เปลี่ยน mapping ของคีย์บอร์ดด้วย xmodmap 


<h1>xmodmap คืออะไร</h1>
xmodmap เป็นโปรแกรมใช้กับ X Windows เพื่อเปลี่ยน mapping ของปุ่มบนคีย์บอร์ด ปกติแล้วทุกๆปุ่มบนคีย์บอร์ดจะมีหมายเลขประจำตัวอยู่ เรียกว่า keycode เวลากดปุ่มลงไป keycode นั้นๆก็จะถูกส่งไปให้ระบบเพื่อเปลี่ยนเป็น action ต่างๆที่นิยามไว้ เจ้า action พวกนี้เรียกว่า keysym ส่วนใหญ่ action ที่ว่านี้ก็ไม่มีอะไรมากไปกว่าแค่พิมพ์ตัวอักษรออกมา แต่ก็มีบางปุ่มที่ทำอะไรมากกว่าแค่พิมพ์ตัวอักษร เช่นพวกปุ่ม multimedia ต่างๆ เช่น ลดความสว่างหน้าจอ เพิ่มเสียง เป็นต้น เนื่องจากระบบ Linux ได้ทำ mapping มาให้อยู่แล้ว (กดปุ่ม a ให้พิมพ์ a, กด b ให้พิมพ์ b) เราจึงใช้งานได้แบบไม่ต้องคิดอะไร

เหตุผลที่ทำให้อยากเปลี่ยน mapping มีหลายอย่าง
<ul>
	<li>ตรงปุ่ม Fn, Ctrl, Alt ด้านซ้ายล่างของคีย์บอร์ดเรียงกันไม่เหมือนกับที่เคยใช้งาน กรณีนี้อาจจะสลับ Ctrl กับ Alt เพื่อให้ใช้ได้อย่างที่ชินมา</li>
	<li>กด backspace เป็น delete แทน</li>
	<li>ตั้งปุ่มที่ไม่เคยได้ใช้ เช่น Capslock ให้เป็นปุ่มอื่นที่มีประโยชน์กว่า</li>
	<li>เปลี่ยน a เป็น b เวลาไม่มีอะไรทำ</li>
</ul>
<h1>หา keycode และ keysym</h1>
ก่อนจะเปลี่ยน mapping ได้อันดับแรกต้องรู้ keycode ของปุ่มที่อยากเปลี่ยน วิธีหาคือให้รันคำสั่ง

[code lang="bash"]xev[/code]

แล้วจะได้หน้าต่างสีขาวขึ้นมา xev ทำหน้าที่รายงาน event ทั้งหมดที่จับได้ ซึ่งรวมไปถึง key event ด้วย ถ้าลองกด a ก็จะได้ประมาณนี้
<blockquote>KeyPress event, serial 30, synthetic NO, window 0x3c00001,
root 0xac, subw 0x0, time 6206663, (718,654), root:(744,656),
state 0x0, keycode 38 (keysym 0x61, a), same_screen YES,
XLookupString gives 1 bytes: (61) "a"
XmbLookupString gives 1 bytes: (61) "a"
XFilterEvent returns: False</blockquote>
จุดสำคัญคือบรรทัดที่ 3 ที่บอกว่า
<blockquote>keycode 38 (keysym 0x61, a)</blockquote>
หมายความว่าปุ่มนี้มี keycode 38 แล้ว map ไปที่ keysym ที่ชื่อว่า a
<h1>เปลี่ยน mapping</h1>
ก่อนเริ่มเปลี่ยน mapping ให้ทำ backup ของ mapping ตัวปัจจุบันไว้ก่อนด้วยคำสั่ง

[code lang="bash"]xmodmap -pke &gt; xmodmap.default [/code]

จะได้ไฟล์ xmodmap.default ที่เก็บการตั้งค่า mapping ทั้งหมด ถ้าทำ mapping พังแล้วต้องโหลดกลับไปใหม่ก็ใช้

[code lang="bash"]xmodmap xmodmap.default[/code]

ขั้นตอนการเปลี่ยนคือ
<ol>
	<li>หา keycode ของปุ่มที่อยากเปลี่ยน (ขอแทนด้วย x)</li>
	<li>หา keysym ที่อยากได้ (แทนด้วย y)</li>
</ol>
แล้วใช้คำสั่ง

[code lang="bash"]xmodmap -e &quot;keycode x = y&quot;[/code]

แค่นี้ ตอนกดปุ่มที่มี keycode x ก็จะทำ keysym y
