Title: Matlab: คูณแต่ละคอลัมน์ด้วย scalar 
Date: 2011-01-10 01:58:01
Tags: matlab 
Slug: Matlab: คูณแต่ละคอลัมน์ด้วย scalar 


วันนี้จะมาพูดเรื่องการคูณแต่ละคอลัมน์ใน matrix ด้วยตัวเลข แต่ก่อนอื่นขอพูดเรื่องสัญลักษณ์ที่จะใช้ก่อน ในบทความนี้และต่อๆไปจะใช้
<ul>
	<li>A(:,j) เพื่อหมายถึงคอลัมน์ j ของ A</li>
	<li>A(i,:) เพื่อหมายถึงแถว i ของ A</li>
	<li>a, b, c หรือตัวอักษรตัวเล็กใช้เป็นตัวแปรสำหรับ scalar</li>
	<li>A,B,C ตัวใหญ่แบบนี้ใช้สำหรับ matrix หรือ vector</li>
	<li>บางทีอาจใช้คำสั่งของ Matlab ตรงๆ เช่น diag(V) เพื่อหมายถึง diagonal matrix ที่สร้างจากตัวเลขใน V</li>
	<li>ถ้า A เป็น matrix จะใช้สัญลักษณ์ [latex]a_{i,j}[/latex] เพื่อหมายถึง ตัวเลขในแถว i และคอลัมน์ j ของ A หรืออาจใช้ [latex]A(i,j) [/latex] บางที</li>
</ul>
เข้าเรื่องเลย สมมติเรามี vector [latex]V \in \mathbb{R}^n[/latex] และ matrix [latex]A \in \mathbb{R}^{m \times n}[/latex] เราอยากได้ matrix [latex]B \in \mathbb{R}^{m \times n}[/latex] ที่ [latex]B(:,j) = A(:,j)*v_j, 1 \leq j \leq n[/latex] พูดง่ายๆคืออยากเอาเลขใน V คูณแต่ละคอลัมน์ของ A

อย่างน้อยๆเราสามารถทำใน Matlab ได้ 4 วิธี (เท่าที่คิดออก)
<h3>1. ใช้ loop ทำ</h3>
วิธีนี้ไม่ขอพูดถึงเพราะไม่ค่อยสนับสนุนเท่าไหร่ แต่ก็สามารถทำได้
<h3>2. ใช้ diagonal matrix</h3>
ตามนิยามการคูณของ matrix ถ้าเราคูณ diagonal matrix D เข้าทางซ้ายของ matrix A ผลที่ได้คือ matrix B ซึ่ง

[latex]B(:,j) = A(:,j) * d_{j,j}[/latex]

เขียนใน Matlab ได้ว่า

[matlab]B = A*diag(V)[/matlab]

คำสั่ง diag จะสร้าง diagonal matrix จาก vector V ซึ่งคำสั่งข้างบนจะให้ผลที่เราอยากได้และตรงกับความหมายทางคณิตศาสตร์ด้วย เข้าใจง่าย แต่เราสามารถทำได้ดีกว่านี้โดยการใช้ sparse matrix ใน Matlab ถ้าเราใช้

[matlab]diag(V)[/matlab]

ตรงๆ Matlab จะเก็บ diagonal matrix ที่ได้มาเสมือนว่ามันคือ matrix ทั่วๆไป แต่ลักษณะเด่นของ diagonal matrix คือมันมีเลขแค่ตรงแนวทแยงที่เหลือเป็น 0 หมด ฉะนั้นเราไม่จำเป็นต้องเก็บทุกตำแหน่งให้เปลืองเนื้อที่ ยังไงซะส่วนใหญ่ก็เป็น 0 เก็บแค่แนวทแยงก็พอ matrix ที่ส่วนใหญ่เป็น 0 มีแค่บางตำแหน่งที่ไม่ใช่ 0 แบบนี้เราเรียกว่า sparse matrix ใน Matlab เราสามารถสร้าง sparse matrix ด้วยคำสั่ง sparse

กลับมาเรื่องเดิมเราต้องการสร้าง sparse diagonal matrix จาก vector V เราสามารถทำได้ดังนี้

[matlab] B = A*sparse(1:length(V), 1:length(V), V )[/matlab]

คำสั่งนี้จะให้ผลเหมือน

[matlab]B = A*diag(V)[/matlab]

แต่จะใช้เนื้อที่เก็บ diagonal matrix น้อยกว่า สำหรับใครที่อยากดูเนื้อที่จริงๆลองรันคำสั่งนี้

[matlab]E = diag( ones(1,10) ); F = sparse(1:10,1:10, ones(1,10) ); whos[/matlab]

คำสั่งนี้จะสร้าง identity matrix ขึ้นมา 2 อันคือ E (แบบไม่ sparse) และ F (แบบ sparse) คำสั่ง whos ท้ายสุดจะแสดงเนื้อที่ของแต่ละตัวแปร จะเห็นว่า F ใช้เนื้อที่น้อยกว่า E
<h3>3. ใช้ repmat</h3>
ก่อนพูดเรื่อง repmat ขออธิบายนิยามอะไรหน่อย การคูณ matrix มีหลายแบบ การคูณ matrix แบบที่เรียกว่า <a href="http://en.wikipedia.org/wiki/Matrix_multiplication#Hadamard_product">Hadamard product</a> เขียนได้แบบนี้ [latex]E = C \circ D[/latex] เมื่อ C และ D คือ matrix ที่มีขนาดเท่ากัน ผลที่ได้คือ [latex] e_{i,j} = c_{i,j} * d_{i,j}[/latex] พูดสั้นๆคือคูณช่องต่อช่องนั่นแหละ ใน Matlab เราสามารถเขียนได้ด้วย

[matlab]E = C .* D[/matlab]

สังเกตตรง . ให้ดีๆ

ที่พูดเรื่อง Hadamard product เพราะมันเกี่ยวกับที่เราจะทำนี่แหละ ที่เราจะทำคือ [latex]B(:,j) = A(:,j)*v_j, 1 \leq j \leq n[/latex] ซึ่งมันก็เท่ากับ [latex]B(:,j) = A(:,j) \circ repmat(v_j, m , 1), 1 \leq j \leq n[/latex] เมื่อ [latex]repmat(v_j, m , 1)[/latex] หมายถึง column vector ขนาด m ที่มีแต่ [latex]v_j[/latex] สรุปว่าปัญหาเดิมสามารถเขียนใน Matlab ได้อีกแบบเป็น

[matlab] B = A .* repmat(V, m, 1)[/matlab]

คำสั่งข้างบน V ต้องเป็น row vector เท่านั้น

คำสั่ง repmat(M, a, b) หมายถึง copy M ลงมา a แถวและ b คอลัมน์ ต้องบอกว่าวิธีที่ 3 นี้ทำไปก็ไม่ทำให้อะไรดีขึ้นมีแต่จะช้าลง แค่เพื่อการศึกษา
<h3>4. ใช้ bsxfun</h3>
อันนี้จะเขียนในโอกาสหน้า
