Title: ปัญหา Eulerian path 
Date: 2011-11-23 05:46:29
Tags: graph 
Slug: ปัญหา Eulerian path 


เมื่อเร็วๆนี้มีเพื่อนคนจีนคนหนึ่งมาตั้งคำถาม (ลองภูมิ?) เกี่ยวกับเรื่อง undirected graph เลยต้องไปรื้อฟื้นความรู้ที่เรียนมา เลยเอามาจดไว้หน่อย ก่อนเข้าเรื่องคำถาม ขอเริ่มด้วยนิยาม 2 อันนี้ก่อน

<strong>1. Complete graph </strong>-- complete graph คือกราฟที่ node ทุกคู่มี edge เชื่อมถึงกัน เขียนแทนด้วย [latex]K_n[/latex] เมื่อ n เป็นจำนวน node มีตัวอย่างมาให้ดูด้วย (รูปพวกนี้สร้างด้วย <a href="http://www.graphviz.org/">Graphviz</a>)

[caption id="attachment_763" align="alignnone" width="180" caption="K_2"]<img class="size-full wp-image-763" title="k2" src="http://wittawat.com/blog/wp-content/uploads/2011/11/k2.png" alt="" width="180" height="77" />[/caption]

[caption id="attachment_766" align="alignnone" width="182" caption="K_3"]<img class="size-full wp-image-766" title="k3" src="http://wittawat.com/blog/wp-content/uploads/2011/11/k3.png" alt="" width="182" height="146" />[/caption]

[caption id="attachment_767" align="alignnone" width="276" caption="K_5"]<img class="size-full wp-image-767" title="k5" src="http://wittawat.com/blog/wp-content/uploads/2011/11/k5.png" alt="" width="276" height="249" />[/caption]

[latex]K_1[/latex] ก็ถือเป็น complete graph เช่นกัน (มีอยู่ node เดียว และไม่มี edge เลย)

<strong>2. Eulerian path </strong>-- Eulerian path คือ เส้นทางเดินบน graph ที่ผ่านทุกๆ edge แค่ครั้งเดียว (ผ่าน node ซ้ำได้ เริ่มจาก node ใดก็ได้ และไม่จำเป็นต้องกลับมาที่ node เริ่มต้น)

<strong>คำถาม</strong>: ใน [latex]K_2, K_3, \ldots, K_{10}[/latex] มีกี่อันที่มี Eulerian path ? ตัวอย่างเช่น จากรูปข้างบน [latex]K_2, K_3[/latex] มี Eulerian path [latex]K_4[/latex] ไม่มี (เอาไปคิดก่อนอ่านต่อนะ)

<strong>คำตอบ</strong>: วิธีตรงตัวที่สุดก็คงจะเป็นการวาด graph แล้วลองลากเส้นดูว่าไปได้ครบทุก edge หรือเปล่า แต่เดาว่าคงจะยอมแพ้กันที่ประมาณ [latex]K_6[/latex]

ต่อไปนี้เป็นข้อสุงเกตที่ทำให้เราหาคำตอบได้โดยไม่ต้องลากเส้น
<ul>
	<li>ทุกครั้งที่เราเดินเข้ามาและเดินออกจาก node ใดๆ เราต้องใช้ 2 edges (edge หนึ่งเอาไว้เดินเข้า อีกอันเอาไว้เดินออก) ยกเว้นจะเป็น node เริ่มต้นซึ่งไม่ต้องใช้ edge เข้าจึงใช้แค่ edge เดียว เช่นกัน node สุดท้ายก็ไม่ต้องใช้ edge ออก</li>
	<li>แปลว่า node ที่ไม่ใช่ node เริ่มหรือ node สุดท้ายจะต้องมีจำนวน edge เป็นเลขคู่ เช่น 2 edges (เข้า, ออก), 4 edges (เข้า, ออก, เข้า, ออก)</li>
	<li>ส่วน node ที่เป็น node เริ่มหรือ node สุดท้ายจะมีจำนวน edge เป็นเลขคู่หรือคี่ก็ได้ กรณีที่เป็นเลขคู่ลองดูรูป [latex]K_3[/latex] ส่วนกรณีคี่ลองดู [latex]K_2[/latex]
เพิ่มเติมคือจริงๆแล้วถ้า node เริ่มหรือ node สุดท้ายมี edge เป็นเลขคู่ทั้งคู่ จะทำให้เราเดินกลับมาที่ node เริ่มได้โดยใช้ทุก edge แค่ครั้งเดียว (เรียกว่า Eulerian circuit)</li>
</ul>
จากข้อสังเกตข้างต้นทำให้เราสร้างกฎเพื่อเช็ค Eulerian path ได้ ดังนี้ (กฎนี้ใช้กับ graph อะไรก็ได้ ไม่จำเป็นต้อง complete)
<ul>
	<li>ถ้าทุก node มี edge เป็นเลขคู่ graph นั้นมี Eulerian path (เข้าทุก node ได้และออกจากทุก node ได้)</li>
	<li>ถ้ามี 2 nodes ที่มี edge เป็นเลขคี่และ node อื่นๆมีจำนวน edge เป็นเลขคู่หมด graph นั้นมี Eulerian path (ให้ 2 nodes ที่มี จำนวน edge เป็นเลขคี่เป็นจุดเริ่มและจุดจบซะ) ตัวอย่างเช่น</li>
<p style="text-align: left;"><img class="size-full wp-image-773 aligncenter" title="k4_1" src="http://wittawat.com/blog/wp-content/uploads/2011/11/k4_1.png" alt="" width="200" height="200" />จะต้องเริ่มที่ 1 ไม่ก็ 3 เท่านั้น เริ่มที่ 1 จะจบที่ 3 เริ่มที่ 3 จะจบที่ 1 ถ้าเริ่มที่ 2 หรือ 4 จะสร้าง Eulerian path ไม่ได้</p>

	<li>นอกเหนือจากนี้ไม่มี Eulerian path เพราะสุดท้ายจะเจอกับปัญหาทำนองว่า เข้า node หนึ่งได้แต่ออกไม่ได้ เนื่องจาก edge อื่นๆเดินไปหมดแล้ว ...</li>
</ul>
คำถามมุ่งประเด็นไปที่ complete graph ข้อสังเกตของ complete graph คือ
<ul>
	<li>ทุกๆ node ใน [latex]K_n[/latex] มี [latex]n-1[/latex] edges เพราะนิยามบอกว่าทุก node เชื่อมกับ node อื่นทุกอัน</li>
	<li>แปลว่าถ้า n เป็นเลขคู่ ทุก node ใน [latex]K_n[/latex] จะมีจำนวน edge เป็นเลขคี่ (n-1 เป็นคี่) ซึ่งจะไม่มี Eulerian path (ยกเว้น [latex]K_2[/latex])</li>
	<li>พูดง่ายๆคือ ถ้า n เป็นเลขคู่  [latex]K_n[/latex] ไม่มี Eulerian path (ยกเว้น [latex]K_2[/latex]) ถ้า n เป็นคี่ [latex]K_n[/latex] มี Eulerian path</li>
</ul>
ใน [latex]K_2, K_3, \ldots, K_{10}[/latex] จาก 2 ถึง 10 มีเลขคี่ 4 ตัวบวกกับ [latex]K_2[/latex] ซึ่งเป็นข้อยกเว้น <strong>คำตอบคือ 5</strong> ([latex]K_2, K_3, K_5, K_7, K_9[/latex] มี Eulerian path)

ที่มา
<ul>
	<li><a href="http://en.wikipedia.org/wiki/Eulerian_path">http://en.wikipedia.org/wiki/Eulerian_path</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg">http://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Complete_graph">http://en.wikipedia.org/wiki/Complete_graph</a></li>
</ul>
