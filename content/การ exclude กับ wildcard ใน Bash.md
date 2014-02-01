Title: การ exclude กับ wildcard ใน Bash 
Date: 2011-04-06 08:05:06
Tags: bash, linux 
Slug: การ exclude กับ wildcard ใน Bash 


ปกติเวลาเราใช้ wildcard บน Bash ส่วนใหญ่จะเป็น * เพื่อเลือกทุกไฟล์ เช่นเราต้องการลบทุกไฟล์ที่ลงท้ายด้วย .mat เราก็ใช้

[bash]rm *.mat[/bash]

แต่ก็มีบาทีที่เราอยากจะลบทุกไฟล์ยกเว้นแค่บางไฟล์ (อาจมากกว่า 1 ไฟล์) เช่นอยากลบทุกๆไฟล์ที่ลงท้ายด้วย .mat แต่ไม่ต้องลบ a.mat, b.mat หรือ c.mat (อยากให้เหลือเฉพาะ 3 ไฟล์นี้)

วิธีคือ อันดับแรกต้องเปิดการทำงานของ exclude ก่อนด้วยคำสั่ง

[bash] shopt -s extglob[/bash]

เพื่อให้ใช้ความหมาย "ไม่" ได้ จากนั้นต่อด้วยคำสั่งลบไฟล์ ในที่นี้คือ

[bash]rm !(a|b|c).mat[/bash]

ตรงเครื่องหมาย ! แปลว่า "ไม่" ซึ่งก็คือลบทุกอย่างที่ไม่ใช่ (a|b|c).mat นั่นเอง พอเสร็จแล้วก็ปิดด้วย

[bash]shopt -u extglob[/bash]

ที่มา:
<ul>
	<li><a href="http://stackoverflow.com/questions/216995/how-can-i-use-negative-wildcards-in-a-unix-linux-shell">http://stackoverflow.com/questions/216995/how-can-i-use-negative-wildcards-in-a-unix-linux-shell</a></li>
</ul>
