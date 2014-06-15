Title: lacheck 
Date: 2008-10-25 06:02:39
Tags: latex 
Slug: lacheck 


ปกติหลังจากที่เราเขียน Tex ไฟล์ (.tex) เสร็จแล้วก็จะเรียกคำสั่ง latex something.tex ถึงใช้โปรแกรม GUI ช่วยเขียน Latex อย่างเช่น Texmaker, LEd คิดว่าโปรแกรมพวกนี้ก็ไปเรียก latex จาก command line อยู่ดี ก็ไม่มีปัญหาอะไร

ปัญหาจะเกิดเวลาที่ .tex ที่เราเขียนมีอะไรผิด เช่น เปิดปีกกาแล้วลืมปิด output จาก latex ไม่ค่อยบอกอะไรเลย บางทีก็บอกไม่ตรงจุด บอกไม่ถูกบรรทัด ทำให้ต้องมานั่งหาอยู่นานว่าที่ผิดอยู่ตรงไหน

โปรแกรม lacheck เป็นโปรแกรมช่วยเช็ค Tex ไฟล์ที่เราเขียนแล้วบอกว่ามีอะไรที่ผิดหรือน่าจะผิดบ้าง ที่บอกว่าน่าจะผิดเพราะ output บางอันของ lacheck เป็นแค่ warning ไม่แก้ก็ไม่เป็นไร ถ้าเราคิดว่าดีแล้ว lacheck แนะนำเฉยๆ วิธีใช้ก็แค่เรียก
<blockquote>lacheck myfile.tex</blockquote>
แล้วมันก็จะ output ออกมาประมาณนี้

"myfile.tex", line 235: possible unwanted space at "{"
"myfile.tex", line 236: Whitespace before punctation mark in " ?"
"myfile.tex", line 236: Whitespace before punctation mark in " ."

ตัวอย่างนี้ไม่มี error มีแต่คำเตือน
