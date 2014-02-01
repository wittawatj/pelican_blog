Title: xmonad กับโปรแกรม java (2) 
Date: 2012-10-01 14:25:24
Tags: java, xmonad 
Slug: xmonad กับโปรแกรม java (2) 


เคยเขียนไปแล้วที่ใช้ xmonad แล้ว<a title="xmonad กับโปรแกรม Java" href="http://wittawat.com/blog/?p=618">โปรแกรม java จอโล่งๆ </a>

กลับมาอีกครั้งเรื่อง window focus คือเวลาเปลี่ยน window ไปที่โปรแกรม java ด้วย keyboard กรอบ focus (กรอบแดงรอบๆ window) ก็เลื่อนไปเหมือนปกติ แต่ cursor จะไม่ไปจับที่ text editor หรือ textbox ต่างๆในหน้าต่างทำให้ต้องใช้ mouse คลิกอีกที ซึ่งน่ารำคาญ คือทุกครั้งที่เปลี่ยนกลับมาต้องใช้ mouse วิธีแก้ให้เพิ่ม

[code]logHook = takeTopFocus[/code]

ที่ xmonad.hs อันนี้อ่านจาก<a href="http://code.google.com/p/xmonad/issues/detail?id=177">หน้า issue ของ xmonad</a> ยาวดี ประมาณ comment 56 มีบอก แต่รู้สึกใช้กับ Java 7 ไม่ได้ แต่ตอนนี้ยังใช้ Java 6 อยู่ ไม่ค่อยสนใจ
