Title: Java Regular Expression 
Date: 2008-04-07 03:47:00
Tags:  
Slug: Java Regular Expression 


ช่วงนี้อ่านเรื่อง <a href="http://java.sun.com/docs/books/tutorial/essential/regex/">regular expression ใน java</a> อยู่ ปกติที่ผ่านมาก็ไม่เคยได้ใช้ในโปรแกรมเลย ได้แต่เรียนๆเป็นทฤษฏี (วิชาเดียวกับ automata)<br /><br />อ่านจบก็รู้สึกไม่่ clear เพราะเขาไม่ได้พูดเรื่องภาษาอื่นเลย เอาแต่อธิบายภาษาอังกฤษ เราก็เลยต้องหาต่อไปเพื่อจะเอา regular expression(RE) มาใช้กับไทยด้วย ก็เลยไปเจอ <a href="http://www.regular-expressions.info/unicode.html">ที่นี่</a> ตรงหัวข้อ Unicode Character Properties มีพูดเกี่ยวกับการเขียน RE ให้ match อักษร unicode ได้<br /><br />อ่านแล้วสรุปได้ความว่า:<br /><ul><li>\p{L}  จะ matchตัวอักษรของทุกภาษา หมายความว่าถ้าใช้กับภาษาไทยจะ match ตัวอักษร ก, า , โ, ต เป็นต้น L ใน \p{L} หมายถึง letter </li><li>\p{M} จะ match พวกเครื่องหมาย เช่น ไม้เอก, สระอู แต่จะไม่ match พวก ก, สระอา ส่วน M ใน \p{M} หมายถึง mark </li><li>\p{N} จะ match ตัวเลขซึ่งรวมไปถึงเลขไทยด้วย เช่น ๒, ๕ เป็นต้น N ใน \p{N} หมายถึง number</li><li>\p{S} จะ match พวกสัญลักษณ์รวมไปถึงเครื่องหมายทางคณิตศาสตร์ เช่น < เป็นต่น S คือ symbol</li><li>\p{P} จะ match เครื่องหมายวรรคตอน เช่น _ เป็นต้น P คือ punctuation<br /></li></ul>เขียนไว้เฉพาะอันที่น่าจะได้ใช้ จริงๆแล้วยังมีอย่างอื่นอีก แต่พอแล้ว ไว้เดี๋ยวค่อยเขียนต่อ
