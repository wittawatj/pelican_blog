Title: รัน shell command จาก Latex 
Date: 2011-03-25 04:59:38
Tags: git, latex, linux, shell 
Slug: รัน shell command จาก Latex 


มีบางกรณีที่เราต้องการผลจากคำสั่ง shell บางอย่างเพื่อเอาไปใส่ในเอกสาร Latex เท่าที่ลองทำดูใช้ code ต่อไปนี้แล้วได้ผล มี comment ที่เกิดจากการเดาล้วนๆประกอบ

[code]
% รันคำสั่ง somecommand แล้วเขียนผลลงไฟล์ file.out
\immediate\write18{somecommand &gt; file.out}
\newread\myinput

% เดาว่าคล้ายๆเปิด file pointer ชื่อ \myinput
\immediate\openin\myinput=file.out

% อ่านค่าในไฟล์ลงตัวแปร \localline
\immediate\read\myinput to \localline

% เก็บค่า \localline ลงตัวแปร \myout ซึ่งเป็น global
\global\let\myout\localline

% ปิด input ที่เปิดไว้
\immediate\closein\myinput
[/code]

ต่อจากนี้ก็เรียก \myout เพื่อเอาผลไปใช้

จริงๆแล้วที่อยากทำคือพยายามจะเอาเลข commit ของ Git ไปใส่ในเอกสารเพื่อจะได้รู้ว่าตอนนี้ commit ไปกี่ทีแล้ว แล้วก็เป็นตัวเลข version ไปในตัว เวลาส่งให้คนอื่นจะได้รู้ว่ามีการอัพเดทหรือไม่ แต่ก่อนเคยเห็น Latex package อยู่ตัวหนึ่งชื่อ svn-multi (มั้ง) สามารถทำอย่างที่บอกได้เลย ไม่ต้องมารันคำสั่งอะไรเองแบบนี้ วิธีของเจ้า package นั้นคือ เขียน string พิเศษอะไรบางอย่างตามที่ svn-multi นิยามไว้แล้ว แล้วมันจะ replace ให้เป็นหมายเลข revision ให้ แต่วิธีนี้รู้สึกว่าต้องมาศึกษากันยาว ยุ่งยาก เลยคิดว่าเขียนเองนิดหน่อยน่าจะเข้าใจง่ายกว่า

code ที่ใช้คือตัวนี้

[code]
\def \revf {rev.txt}
\immediate\write18{git log --pretty=format:'..' | wc -w &gt; \revf}
\newread\myinput
\immediate\openin\myinput=\revf
\immediate\read\myinput to \localline
\global\let\rev\localline
\immediate\closein\myinput
[/code]

จากนั้นเอา \rev ไปใช้เพื่อบอกหมายเลข commit ตรง

[code]git log --pretty=format:'..' | wc -w[/code]

นี่เอาไว้หาว่า commit ไปแล้วกี่ที ชัดเจนว่ามันเป็นการ hack แบบลวกๆ แต่คิดว่าไม่น่ามีปัญหานะ

สุดท้าย เท่าที่เข้าใจคือปกติแล้ว Latex จะไม่อนุญาตให้รันคำสั่ง shell เพราะอาจเป็นไปได้ที่เราไปโหลดไฟล์ tex ของคนอื่นมาแล้วในนั้นมีการรันคำสั่ง shell แบบที่สร้างความเสียหาย วิธีทำให้ใช้ได้คือเพิ่ม

[code]--shell-escape[/code]

เป็น argument ของคำสั่ง latex หรือ pdflatex ตอน compile ซะ แบบนี้

[code] pdflatex --shell-escape doc.tex [/code]

หรือ

[code] latex --shell-escape doc.tex [/code]

สำหรับคนที่ใช้ Latex editor แบบที่กดปุ่มเดียว compile ให้หมดก็สามารถเพิ่ม argument แบบนี้ได้เช่นกัน เพราะปกติปุ่มแต่ละปุ่มที่ใช้ compile เอกสารจะไปเรียกคำสั่ง command line พวกนี้อยู่แล้ว editor ส่วนใหญ่จะให้แก้คำสั่งเองได้ เช่นในรูปต่อไปนี้มาจากโปรแกรม Winefish
<p style="text-align: center;"><a href="http://wittawat.com/blog/wp-content/uploads/2011/03/Screenshot.png"><img class="size-full wp-image-670 aligncenter" title="Screenshot" src="http://wittawat.com/blog/wp-content/uploads/2011/03/Screenshot.png" alt="" width="491" height="126" /></a></p>
อ้างอิง
<ul>
	<li><a href="http://www.texdev.net/2009/10/06/what-does-write18-mean/">http://www.texdev.net/2009/10/06/what-does-write18-mean/</a></li>
	<li><a href="http://stackoverflow.com/questions/3252957/how-to-execute-shell-script-from-latex">http://stackoverflow.com/questions/3252957/how-to-execute-shell-script-from-latex</a></li>
	<li><a href="http://stackoverflow.com/questions/2671079/how-can-i-save-shell-output-to-a-variable-in-latex">http://stackoverflow.com/questions/2671079/how-can-i-save-shell-output-to-a-variable-in-latex</a></li>
</ul>
