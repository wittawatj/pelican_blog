Title: สร้าง symbolic link ใน Windows และ Linux 
Date: 2012-06-18 06:18:39
Tags: linux, windows 
Slug: สร้าง symbolic link ใน Windows และ Linux 


มีเหตุให้ต้องกลับมาใช้ Windows ชั่วคราว แล้วคิดถึง symbolic link ที่ใช้ใน linux หาแล้ว Windows ก็มีเหมือนกัน ทำแบบนี้

[bash]mklink /D LinkName Target[/bash]

โดยที่
<ul>
	<li>LinkName คือชื่อ link ที่อยากได้</li>
	<li>Target คือ path ปลายทางที่จะ link ไปหา</li>
</ul>
ตรง /D นี่ใส่เพราะจะทำ link สำหรับ directory ถ้าเป็นไฟล์ธรรมดาก็ไม่ต้องใส่ ถ้าเป็นแบบ linux ก็จะแบบนี้

[bash]ln -s Target LinkName [/bash]

สังเกตว่า Target กับ LinkName สลับที่กับ Windows เอะใจว่ามันอันเดียวกับ shortcut ใน Windows หรือเปล่า ลองสร้าง shortcut แล้วเทียบดู ดูเหมือนจะไม่ใช่นะ
