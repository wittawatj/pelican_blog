Title: สร้าง recovery microSD card ให้กับ Sharp pc-z1 
Date: 2012-03-14 09:07:07
Tags: linux, netwalker 
Slug: สร้าง recovery microSD card ให้กับ Sharp pc-z1 


มีเครื่อง netbook Sharp pc-z1 (netwalker) ซื้อมานานแล้วแต่ boot ไม่ขึ้น จำไม่ได้ว่าเล่นอะไรไป การ recover คืน ดูจาก<a href="http://www.sharp.co.jp/support/mit/doc/install.html">เว็บของ Sharp</a> มีบอกวิธีทำ recover microSD card ด้วย pc-z1 แต่ไม่ make sense เพราะตอนนี้มันพัง ทำไม่ได้ เลยต้องสร้างด้วยเครื่องอื่น

หาไปหามาได้ความว่าจริงๆแล้วที่ทำ recovery microSD เป็น shell script อันหนึ่งโหลดได้จาก<a href="http://www.sharp.co.jp/support/ex-data/recovery.sh.tar.gz">ที่นี่</a>เจ้า script นี้จะ download และสร้าง recovery microSD ให้เอง แต่ต้องแก้อะไรนิดหน่อยคือ ให้เปลี่ยน SDNODE, SDNODE_VALID, SDDEVICE และ SDMOUNT ให้ถูกต้อง ค่าพวกนี้หาได้ด้วย

[code lange="bash"]mount -l[/code]

แล้วรัน script แล้วก็ทำตามที่มันขึ้นมา (ภาษาญี่ปุ่น) ก็ได้แล้ว

เผื่อมีคนไทยเข้ามาอ่าน
<ul>
	<li>リカバリー用microSDカードを作成しますか？ แปลว่า "จะสร้าง recovery microSD มั้ย" ตอบ yes</li>
	<li>USB端子には何も接続しないでください。แปลว่า "อย่าเสียบอะไรที่ port USB" ถอด microSD ออกก่อนแล้วตอบ yes</li>
	<li>microSDを挿入してください。แปลว่า "กรุณาใส่ microSD" ใส่แล้วตอบ yes</li>
	<li>microSDのフォーマットを実行します。แปลว่า "จะเริ่ม format microSD นะ" กด ok (<strong>คำเตือน: ข้อมูลบน microSD หายหมด</strong>)</li>
</ul>
ตอนใช้งาน microSD เพื่อ recover ก็ให้ใส่การ์ดแล้วกดปุ่มเม้าส์ซ้ายขวาพร้อมกันข้างไว้ แล้วเปิดเครื่องกดค้างไปเรื่อยๆจนมันขึ้นหน้าจอดำๆเป็นภาษาญี่ปุ่นให้กด Y แล้วก็รอจนมัน recover เสร็จ

ที่มา
<ul>
	<li><a href="http://ameblo.jp/yamjp/entry-10693037658.html">http://ameblo.jp/yamjp/entry-10693037658.html</a></li>
	<li><a href="http://www.tanimoto.to/PC_DIY/UbuntuJA/index.html">http://www.tanimoto.to/PC_DIY/UbuntuJA/index.html</a> (อันนี้คนเขียน เขียนไปบ่นไป)</li>
</ul>
