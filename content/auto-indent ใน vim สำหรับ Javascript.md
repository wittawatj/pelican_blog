Title: auto-indent ใน vim สำหรับ Javascript 
Date: 2013-01-04 09:46:08
Tags: javascript, vim 
Slug: auto-indent ใน vim สำหรับ Javascript 


ปกติผู้ใช้ vim สามารถกด == เพื่อย่อหน้าบรรทัดที่อยู่ได้อย่างอัตโนมัติ แต่ถ้าไม่ทำอะไรพิเศษฟังก์ชันนี้จะแย่มากสำหรับ Javascript โดยเฉพาะอย่างยิ่งถ้าใช้ anonymous function เยอะ จะย่อหน้าผิดเพี้ยนหมด

วิธีแก้คือให้ลง plugin manager ชื่อ <a href="https://github.com/gmarik/vundle">vundle</a> ก่อนซึ่งจะทำให้สามารถลง plugin อื่นๆมีประโยชน์ได้อีกเยอะ จากนั้นก็ใช้ vundle นี้ลง plugin ที่ชื่อ <a href="https://github.com/pangloss/vim-javascript">vim-javascript</a> หลังจากทำตามขั้นตอนจบจะพบว่าย่อหน้าอัตโนมัติโดยการกด == ทำงานดีมาก

เทคนิคการย่อหน้าทั้งไฟล์คือให้กด gg ก่อนเพื่อไปจุดเริ่มแล้วตามด้วย =G เพื่อจัดย่อหน้าทั้งหมดจนจบไฟล์

	gg=G
