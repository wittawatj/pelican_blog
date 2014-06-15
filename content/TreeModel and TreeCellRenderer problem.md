Title: TreeModel and TreeCellRenderer problem
Date: 2008-04-22 10:59:00
Tags: java
Slug: TreeModel and TreeCellRenderer problem 


หลังจากที่นั่งงมกับ bug จนเบื่อมาก กินเวลาไปหลายชั่วโมง ก็เจออะไรบางอย่าง คือ JTree จะมี constructor รับ TreeModel เพื่อสร้าง Tree โดยใช้ model นั้น แล้ว JTree ก็จะมี method ชื่อ setModel ด้วยซึ่งจะรับ TreeModel แล้วเปลี่ยน model ของ tree นั้น<br /><br />ตามความเข้าใจแล้วการสร้าง tree โดยใส่ model ไปที่ constructor หรือสร้าง tree เฉยๆ แล้วเรียก setModel ทีหลัง ควรจะให้ผลเหมือนกัน (อันนี้คือที่เข้าใจมา และ class อื่นๆก็เป็นคล้ายๆแบบนี้เหมือนกันหมด) แต่มันไม่เหมือนอะสิ....<br /><br />tree ที่ใช้อยู่ใส่ node renderer ที่ทำขึ้นเอง ซึ่งถ้า tree ถูกสร้างโดยใส่ model ไปที่ constructor เจ้า renderer นี้มันจะยิง event เมื่อ node มีอะไรเปลี่ยน และ paint tree ให้ใหม่เอง แต่ถ้า tree ที่มี model แบบสร้างขึ้นผ่านทาง setModel แล้ว renderer มันก็ยิง event นะ แต่มันไม่ paint ใหม่ให้ ทำไมก็ไม่รู้? หรือว่าไม่เกี่ยว ? แต่เข้าไปอ่าน code ของ JTree แล้วที่ constructor มันก็เรียก setModel เหมือนกันนั่นแหละ.... แล้วทำไมผลจาก renderer ไม่เหมือนกัน ? คงมีอะไรบางอย่างที่เรายังไม่เข้าใจแน่นอน<br /><br />ตอนนี้เนื่องจากเสียเวลาไปมากแล้ว จะไม่เรียก setModel อีกแล้ว เปลี่ยนมันใหม่ทั้ง JTree เลย มันก็ใช้ได้ แต่โปรแกรมคงจะช้าลงนิดๆ แล้วก็ encapsulation ของเราก็แตกนิดๆด้วย แต่เอาเหอะ เต็มทนละ.... ว่างๆต้องหาต่อให้ได้ว่าทำไม
