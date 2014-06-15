Title: ทำ server ที่บ้านผ่าน dynamic dns 
Date: 2009-09-13 03:04:43
Tags: dynamic dns, server 
Slug: ทำ server ที่บ้านผ่าน dynamic dns 


อยากได้ Linux  server ซักตัวที่เราสามารถควบคุมได้ทุกอย่าง พูดง่ายๆคืออยาก ssh เข้าไปได้แล้วมีสิทธิ์แบบ root ครับ เช่น อยากใช้ JSP ก็ลงเองได้เลย เป็นต้น แต่มันต้องจ่ายแพง หาเว็บไปมาและถามใครต่อใครหลายคนเลยได้คำตอบว่าใช้ <a href="http://en.wikipedia.org/wiki/Dynamic_DNS">Dynamic DNS</a> ช่วยได้ครับ

สิ่งที่ต้องใช้
<ol>
	<li>Account เพื่อเชื่อมต่อ Internet  ของผมเป็น ADSL และคิดว่าหลายๆคนก็คงเป็น ADSL เหมือนกัน</li>
	<li>Router คิดว่าหลายๆคนนอกจากจะมี ADSL modem แล้วคงมี router ในบ้านครับ (รึป่าว ?) หรือจะเป็น router ที่มี modem แบบ built-in ก็ได้</li>
	<li>สิทธิ์การแก้ไขค่าต่างๆของ router</li>
	<li>คอมหนึ่งเครื่องตั้งไว้เป็น server</li>
	<li>Account ของผู้ให้บริการ dynamic DNS ซึ่งผมจะใช้ของ <a href="http://www.dyndns.com/">http://www.dyndns.com/</a> (ฟรี)</li>
</ol>
สิ่งที่จะทำต่อไปนี้คือ ใช้คอมหนึ่งเครื่องมาทำเป็น server ซึ่งคอมเครื่องนี้เชื่อมต่อกับ router ในบ้านเราและสามารถเข้าอินเตอร์เน็ตได้ เราจะตั้งค่า router ให้ forward port ต่างๆที่เราจะใช้มาที่เครื่องคอมเครื่องนี้ เช่น อยากได้ web server ก็ต้อง forward port 80 ผมอยากได้ ssh ด้วยก็ port 22 ด้วย เป็นต้น

เหตุที่ต้อง forward port เพราะว่าหากเรามองจากโลกภายนอก เราจะเห็นว่าคอมทุกเครื่องในบ้านรวมถึงเจ้า server ด้วย เป็น IP เดียว นั่นคือ WAN IP ที่ได้รับแจกจาก ISP นั่นเอง (<a href="http://wittawat.com/tools/myip.php">คลิกเพื่อดู WAN IP ของคุณ</a>) จึงมีความจำเป็นที่จะต้องบอก router ว่าหากมีการร้องขอหน้าเว็บผ่าน port 80 ให้ส่งคำร้องนั้นมีที่ server ซะ ถ้าไม่บอก router ไว้ก่อน ปกติมันก็จะ block ครับ นั่นคือเรียกเว็บมาที่ WAN IP บ้านเราก็จะไม่ขึ้นอะไรนอกจาก "... not found ..."

ประเด็นก็คือว่า WAN IP ที่แจกมาให้บ้านเรานั้นมันเปลี่ยนไปเรื่อยๆ วิธีหนึ่งก็คือใช้ Dynamic DNS อย่างที่บอกครับ คือเราจะสร้าง domain name ขึ้นมาหนึ่งอัน domain name นี้ map มาที่ WAN IP จากนั้นใช้ domain name นี้เพื่อเข้าถึง server ที่บ้านแทนที่จะเรียก WAN IP ตรงๆ เมื่อ WAN IP ของเราเปลี่ยน ก็ให้ router บอกไปที่ domain name ว่า IP เปลี่ยนแล้ว ให้แก้การ mapping ซะ จะเห็นว่าการทำแบบนี้ผู้ใช้ไม่รู้เรื่อง IP mapping หรือเรื่อง WAN IP เปลี่ยนเลย รู้แต่ว่าเรียก domain name แล้วใช้งานได้ก็พอ

การสมัครใช้ Dynamic DNS ผมสมัครที่<a href="http://www.dyndns.com/"> http://www.dyndns.com/</a> ซึ่งฟรี ขั้นตอนสมัครก็เหมือนเว็บทั่วๆไป กรอกรายละเอียด ส่งเมล์มายืนยัน กด activate แล้วก็เริ่มใช้งานได้โดย login เข้า account ของเรา

การสร้าง domain name ให้ชี้มาที่ WAN IP ที่บ้าน ทำโดย login เข้าไปที่ dyndns ก่อน หาหมวด Host Serviceห แล้วเลือก Add Hostname ดังภาพ

<img class="aligncenter size-full wp-image-270" title="Screenshot" src="http://wittawat.com/blog/wp-content/uploads/2009/09/Screenshot.png" alt="Screenshot" width="659" height="332" />

เข้ามาแล้วให้เลือก Hostname ตามใจครับ domain ด้านหลังก็มีให้เลือกเยอะอยู่ ตรงช่อง IP Address กด "Use auto detected IP Address" เพื่อบอกว่าให้ domain name ชี้มาที่ WAN IP ของเรา

<img class="aligncenter size-full wp-image-271" title="Screenshot-DynDNS.com - My Account -- Host Services -- Settings - Mozilla Firefox" src="http://wittawat.com/blog/wp-content/uploads/2009/09/Screenshot-DynDNS.com-My-Account-Host-Services-Settings-Mozilla-Firefox.png" alt="Screenshot-DynDNS.com - My Account -- Host Services -- Settings - Mozilla Firefox" width="644" height="428" />ทำเสร็จกดปุ่ม "Add To Cart" ครับ ย้ำอีกครั้งว่าไม่เสียเงินครับ มันจะขึ้นว่าคุณต้องจ่าย 0.00$ ทีหลัง ถ้าทำสำเร็จเมื่อกลับไปหน้าก่อนหน้าตรง Host Services จะมี ชื่อ domain และ IP ของเราขึ้นมาแล้ว

ขั้นต่อไปคือตั้งให้ระบบของเราแจ้ง dyndns ทุกครั้งที่ WAN IP เปลี่ยน ผมเข้าใจว่าสำหรับคนที่มี Router แต่ไม่สนับสนุน Dynamic DNS สามารถใช้โปรแกรม Dynamic DNS Client ให้รันบน server ของเราแล้วคอยแจ้งเตือนได้ แต่พอดี Router ผมแจ้งเตือนได้เอง เลยไม่ได้ใช้โปรแกรมนะครับ ไม่รู้รายละเอียด สำหรับการตั้ง Router ให้แจ้งไปที่ dyndns อันนี้พูดยากเนื่องจาก router แต่ละยี่ห้อมีเมนูและวิธีตั้งค่าไม่เหมือนกัน ของผมใช้ Router ของ SMC หลายปีมากแล้ว มีหน้าตาแบบนี้

<img class="aligncenter size-full wp-image-272" title="Screenshot-Mozilla Firefox" src="http://wittawat.com/blog/wp-content/uploads/2009/09/Screenshot-Mozilla-Firefox.png" alt="Screenshot-Mozilla Firefox" width="616" height="374" />

จากที่เห็นก็ใส่ domain name ที่สมัครลงไป ตรง account ก็ใส่ username ของ dyndns แล้วก็ password ถึงตรงนี้ระบบเราสามารถแจ้งเตือน dyndns ได้เองแล้วหาก WAN IP เปลี่ยนไป

เรื่องสุดท้ายคือการ forward port ตอนนี้หากใส่ชื่อ domain ที่เพิ่งสมัครไปที่ web browser อาจจะยังใช้ไม่ได้เพราะ router ไม่รู้จะส่งคำร้องไปให้เครื่องไหนในบ้านเรา ก็ให้ทำการ forward port 80 (สำหรับ web server) ครับ หน้าตาการทำ port forwarding ของ router ผมเป็นแบบนี้ (router ของผมมันใช้คำว่า Virtual Server)

<img class="aligncenter size-full wp-image-273" title="Screenshot-Mozilla Firefox-1" src="http://wittawat.com/blog/wp-content/uploads/2009/09/Screenshot-Mozilla-Firefox-1.png" alt="Screenshot-Mozilla Firefox-1" width="627" height="160" />

จากภาพบอกว่าถ้ามีการร้องขอ port 80 มาที่ router (Public Port) ให้ส่งไปที่ port 80 (LAN port) ของเครื่อง 192.168.2.103 โดยที่ 192.168.2.103 เป็น IP ภายในของเครื่อง server ครับ

ลืมบอกว่า เครื่อง server นี้ต้อง Fix LAN IP นะ ปกติเครื่องในบ้านคนมักใช้ DHCP เพื่อแจก IP แต่สำหรับ server นี้ต้อง Fix ตายตัวเพราะไม่งั้นวันดีคืนดี 192.168.2.103 อาจกลายเป็นเครื่องอื่นในบ้านที่ไม่ใช่ server

จบครับสำหรับการทำ server ไว้ที่บ้าน แนะนำให้ forward port 22 ด้วยจะได้ ssh เข้ามาที่ server จากที่อื่นได้

[ad#afterpost]
