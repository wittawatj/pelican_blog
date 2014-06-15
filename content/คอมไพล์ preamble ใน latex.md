Title: คอมไพล์ preamble ใน latex 
Date: 2012-03-02 11:11:30
Tags: beamer, latex 
Slug: คอมไพล์ preamble ใน latex 


ช่วงนี้กำลังหาวิธีทำให้การคอมไพล์ไฟล์ latex เร็วขึ้น วิธีหนึ่งก็คือการคอมไพล์ preamble ของ latex เตรียมไว้ก่อน ซึ่งทำให้เวลาใช้คำสั่ง latex หรือ pdflatex จะไม่มีการประมวลผลพวก usepackage ทั้งหลาย ช่วยลดเวลาคอมไพล์ได้ (แต่ประมาณ 2 วินาทีเอง จากที่วัดดู) อันนี้มีประโยชน์สำหรับคนใช้ beamer เพราะ header เยอะมาก วิธีคือให้ทำดังนี้ เรียกชื่อไฟล์ latex ว่า main.tex ละกัน
<ol>
	<li>สร้างไฟล์ใหม่ชื่อ preamble.tex แล้วแยกส่วนที่ต้องการคอมไพล์เตรียมไว้ก่อนไปไว้ที่นั่น ควรเป็นส่วนที่ไม่มีการเปลี่ยนแปลงบ่อยเช่น พวก usepackage ทั้งหลาย</li>
	<li>สำหรับคนใช้ pdflatex รัน[code lang="latex"]pdflatex -ini &quot;&amp;pdflatex preamble.tex\dump&quot;[/code]

แล้วจะได้ไฟล์ชื่อ preamble.fmt มา ถ้าใช้ latex ให้เปลี่ยน pdflatex ให้เป็น latex</li>
	<li>ที่ main.tex ใส่ <code>%&amp;preamble</code> ไปที่บรรทัดแรก</li>
	<li>คอมไพล์เอกสารตามปกติ ถ้าไม่ผ่านให้ลองใช้[code lang="latex"]pdflatex -parse-first-line[/code]

แทน</li>
</ol>
ก็จะได้ทุกอย่างเหมือนเดิม เพียงแค่ตอนคอมไพล์จะไม่มีการประมวลผล preamble วิธีนี้พูดสั้นๆก็คือการคอมไพล์ preamble แบบ manual นั่นเอง แน่นอนว่าถ้า preamble มีอะไรเปลี่ยนก็ต้องคอมไพล์เองใหม่ด้วย

ที่มา
<ul>
	<li><a href="http://magic.aladdin.cs.cmu.edu/2007/11/02/precompiled-preamble-for-latex/">http://magic.aladdin.cs.cmu.edu/2007/11/02/precompiled-preamble-for-latex/</a></li>
	<li><a href="http://www.physics.hmc.edu/latex.php">http://www.physics.hmc.edu/latex.php</a></li>
</ul>
