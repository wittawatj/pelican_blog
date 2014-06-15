Title: บันทึกเกี่ยวกับ CSS  
Date: 2012-06-21 06:03:34
Tags: css, web 
Slug: บันทึกเกี่ยวกับ CSS  


ต่อไปนี้เป็นรายละเอียดปลีกย่อย (หรืออาจจะธรรมดาไปก็ได้) ของ CSS ที่น่าจะใช้ได้
<h3>ทำให้เนื้อหาอยู่ตรงกลาง</h3>
ใช้ &lt;div&gt; แล้วใส่ style อย่างน้อย 2 อย่างนี้

[css]
margin: 20px auto;
width: 60%;
[/css]

ประเด็นคือ margin ซ้าย ขวา ต้องเป็น auto ซึ่งจะทำให้กลาง ส่วน width ต้องน้อยกว่าขนาดของหน้ามากๆ ไม่งั้นมันจะถือว่า width เต็ม container แปลว่ามันกลางแล้ว ใช้ div นี้เป็น wrapper ใหญ่สุดในหน้า
<h3>Nested Selectors</h3>
[css]
.marked p {
  color: white;
}
[/css]

แปลว่า style เฉพาะ &lt;p&gt; ที่อยู่ใน tag อื่นที่เป็น class marked แต่จะ<strong>ไม่ style</strong> ให้กับ

[html]&lt;p class=&quot;marked&quot;&gt;[/html]

นะ ถ้าจะเอาอันหลังต้องใช้ selector

[css]
p.marked {
  color: white;
}
[/css]
<h3>จัดตำแหน่งด้วย position</h3>
สรุปจาก<a href="http://www.w3schools.com/css/css_positioning.asp">หน้านี้</a> ปกติ element ต่างๆจะมีค่า position: static เป็นปกติ แปลว่าเรียงไปแบบปกติ ซ้ายไปขวา บนลงล่าง และการตั้งค่า top, right, bottom, left ก็ไม่มีผล แต่ position สามารถเป็นค่าอื่นได้ เช่น

[css]
p.pos_fixed{
  position:fixed;
  top:30px;
  right:5px;
}
[/css]

แปลว่า p.pos_fixed จะคงที่ไม่ไปไหน scroll ก็ไม่ไป ตำแหน่งคือที่ top, right กำหนด (คิดจากมุมซ้ายบนของหน้าต่าง)

position:relative คือเหมือน static แหละ แต่จะเลื่อนด้วย top, right, bottom, left ได้ ถึงมันจะเลื่อนไปทับอะไรอย่างอื่น แต่ HTML จะถือว่า element นั้นยังกินที่เดิมอยู่

position:absolute จะยึด parent ที่ไม่เป็น static เป็นหลักในการเลื่อน (ถ้าไม่มีก็น่าจะเหมือน fixed ) เจ้า parent ที่ว่าอาจจะมี position:relative เป็นต้น ถ้าใช้ position:absolute จะทำให้ element นั้นหลุดออกจาก flow ไปเลย คือเหมือนไม่มีตัวตนในหน้าและไม่กินที่ ณ จุดที่มันอยู่

แน่นอนว่าการจัดตำแหน่งใหม่แบบนี้อาจมีอะไรทับกัน การกำหนดว่าอะไรควรอยู่บนให้ใช้ z-index ถ้าค่ามากก็อยู่บน ถ้าไม่มี z-index อันไหนมาหลังจะอยู่บน
<h3>การวัดความกว้างของ element</h3>
การกำหนด width ไม่ได้ทำให้ element มีขนาดเท่านั้นเป๊ะ แต่ความกว้างของ element คือ width+margin+padding เช่น

[css]
div.ex{
  width:220px;
  padding:20px;
  border:5px solid gray;
  margin:0px;
}
[/css]

div.ex อันนี้จะกว้าง 250px <a href="http://www.w3schools.com/css/css_boxmodel.asp">ดู box model</a> จริงๆมีเรื่อง outline อีกแต่ไม่ค่อยเข้าใจว่าจะมีไปทำไม ไม่อยู่ใน box model ด้วย
