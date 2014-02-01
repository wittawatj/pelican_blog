Title: ใช้ Python แล้วรู้สึกอย่างไร 
Date: 2009-11-24 04:46:36
Tags: python 
Slug: ใช้ Python แล้วรู้สึกอย่างไร 


เร็วๆนี้ได้มีโอกาสเขียน Python แบบยาวๆ ที่ผ่านมามีแต่เล่นกับ interactive shell ของ Python ไม่เคยได้มีเรื่องให้ต้องเขียนเป็น file.py เป็นเรื่องเป็นราวเลย ปกติก็ใช้ Java ทำให้มีอะไรก็เลือก Java ไว้ก่อน

ต่อไปนี้เป็นความเห็นเกี่ยวกับ Python (V. 2.6) จากคนที่เอาแต่เขียน Java อย่างผม
<ul>
	<li><span style="text-decoration: line-through;"><strong>ไม่ใช่ภาษาแบบ strongly typed </strong></span><strong>(ขอขอบคุณคุณวีร์ที่ช่วยแก้ไขให้ครับ Python เป็น strongly typed) แล้วรู้สึกอึดอัด</strong> อันนี้อาจจะกลับกันกับคนอื่นๆที่บอกว่า ไม่ต้องเขียน type ตอนเขียนโปรแกรมก็ดีแล้วมันจะได้ยืดหยุ่นดี ผมกลับมองว่ามันทำให้อ่าน code ยากเพราะไม่รู้ตัวแปรเป็นประเภทอะไร แถมทำให้เกิด runtime error แบบไม่จำเป็นได้ด้วย ทั้งที่ error เกี่ยวกับ type บางกรณีสามารถจับได้ตั้งแต่ compile time แล้ว เช่นใน Java</li>
	<li><strong>เปลี่ยน editor แล้ว code อาจมีปัญหา</strong> อันนี้มาจากว่า Python ใช้วรรคในการแบ่ง block ของ code และอนุญาตให้ใช้วรรคขนาดไหนก็ได้ (แต่ต้องใช้ให้เหมือนกันทั้งโปรแกรม) ปกติผมใช้ 1 tab ในการแบ่ง block ย่อย พอเปลี่ยน editor code ที่เขียนอาจะมี error เพราะ editor บางตัวเปลี่ยน tab เป็น '\t' บางตัวเปลี่ยนเป็น 4 วรรค บางตัวเป็น 8 วรรค แต่อย่างไรก็ตามประเด็นนี้ไม่ใช่ปัญหาใหญ่มาก</li>
	<li><strong>เขียน OOP ต้องส่ง self เสมอ</strong> ผมรู้สึกไม่ชินที่เวลาประกาศ method ของ class ใน Python จะต้องสำรองให้ argument แรกของ instance method เป็น object นั้นๆ อันนั้นอาจเป็นเพราะติด Java มาเพราะ Java ไม่ต้องทำแบบนั้น มีความรู้สึกว่ามันไม่เป็น OOP จริงๆยังไงไม่รู้ เหมือนว่าพยายามเอาภาษา procedural มา simulate ให้เป็น OOP แต่อันนี้แค่ความเห็นส่วนตัว ประมาณว่า [python]a.method1(x)[/python]

จริงๆแล้วก็แค่

[python]method1(a, x)[/python]</li>
	<li><strong>Field ของ object ไม่มี private ?</strong> อันนี้อาจเป็นแค่ความไม่รู้ของผมเอง คือไม่รู้ว่าจะทำยังไงให้ field มันเป็น private แค่นั้นแหละ เดาว่ามีแต่หาไม่เจอซะที เลยช่างมัน</li>
	<li><strong>ทุกอย่างสั้นไปหมดใน Python</strong> อันนี้ถือเป็นข้อดีที่รู้สึกได้เลย รู้สึกว่า Java เป็นคนพูดมากไปเลย Java จะทำอะไรทีจะยาวมาก แต่พอเขียน Python ยิ่งได้ใช้พวก functional construct เช่น map, filter ประกอบกับ lambda ทำให้ทุกอย่างสั้นลงไปมาก loop 10 บรรทัด อาจเหลือบรรทัดเดียวได้ด้วย map (lambda ....) แต่ความสั้นก็ต้องแลกมาด้วยความอ่านยากนะ ยิ่ง lambda เยอะๆนี่ งงตัวเอง เทียบกับ Java (6.0) แล้ว lambda น่าจะเทียบเท่ากับ anonymous class ของ Java แต่ว่า lambda น่าจะเจ๋งกว่าเพราะทำ currying ได้</li>
	<li><strong>Function เป็น first-class value</strong> แปลว่าเราสามารถส่ง function เป็น argument ให้ function อื่นๆได้ เช่น [python]
def g(f, l): return f(l) [/python]

แล้วเราก็เรียก

[python] g(max, [14,6,1]) [/python]

โดยที่ max เป็นชื่อ function ซึ่งจะได้ 14 ถ้าเป็น Java ก็คงต้องสร้าง class ที่มี 1 method แล้วส่ง object ของ class นั้นไปแทน</li>
</ul>
อาจจะมีประเด็นอื่นอีก แต่หลักๆที่รู้สึกทำให้ไม่ถนัดคือเรื่อง type นี่แหละ ไม่มีแล้ว งงๆ

เพิ่มเติม
<ul>
	<li><a href="http://veer66.wordpress.com/2009/11/24/weak-typing/">http://veer66.wordpress.com/2009/11/24/weak-typing/</a></li>
</ul>
[ad#afterpost]]
