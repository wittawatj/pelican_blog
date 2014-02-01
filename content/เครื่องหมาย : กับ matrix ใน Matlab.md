Title: เครื่องหมาย : กับ matrix ใน Matlab 
Date: 2012-06-01 05:59:44
Tags: matlab 
Slug: เครื่องหมาย : กับ matrix ใน Matlab 


เครื่องหมาย : (colon) ใน Matlab ใช้ได้หลายที่ ที่ใช้บ่อยก็เพื่อสร้าง array ของตัวเลขที่เรียงกัน เช่นแบบนี้

[matlab]1:5[/matlab]

ก็จะได้
<pre>ans =

     1     2     3     4     5</pre>
ต่อไปคือการใช้กับ matrix สมมติมี matrix A ขนาด r x c แบบนี้

[matlab] [r c] = size(A)[/matlab]

เราสามารถใช้ : เพื่อเลือกทั้งแถวหรือทั้งคอลัมน์ได้ เช่นอยากได้คอลัมน์ที่ 3 ของ A ก็แค่

[matlab]A(:, 3)[/matlab]

ที่พูดมานี่เป็นอะไรที่ใครๆก็น่าจะใช้บ่อยอยู่แล้ว ต่อไปคืออะไรไม่ค่อยพบเห็น ถ้าทำแบบนี้ล่ะ

[matlab]A(:)[/matlab]

อันนี้จะได้ column vector ขนาด rc x 1 โดยที่ค่าใน vector นี้มาจาก A อ่านตามแนวตั้ง คืออ่านตามแนวที่ matlab เก็บนั่นเอง (ลองดู<a title="Matlab เก็บ matrix อย่างไร" href="http://wittawat.com/blog/?p=936">โพสนี้</a>ว่า Matlab เก็บ matrix อย่างไร)

มีอีกคือ สมมติมี matrix B ขนาด r x c x d คือแบบนี้ [matlab][r c d] = size(B)[/matlab]

แล้ว [matlab]B(:)[/matlab]

จะได้อะไร ? คำตอบก็เหมือนเดิมคือ จะได้ column vector ขนาด rcd x 1 โดยที่ค่าใน vector นี้มาจาก B อ่านตามแนวตั้งจนหมด B(:,:,1) แล้วก็ต่อด้วยอ่านตามแนวตั้งจนหมด B(:,:,2) ทำไปจนถึง B(:,:,d)

แล้วถ้า [matlab]B(:,:)[/matlab]

ล่ะ? ปกติถ้า B เป็น matrix 2 มิติ ก็ไม่น่ามีอะไรให้สงสัยเพราะจะได้ B ตามเดิม แต่นี่ B เป็น 3 มิติ ผลลัพธ์คือจะได้ matrix 2 มิติขนาด r x cd ซึ่งเกิดจากการเอามิติที่ 3 มาต่อที่มิติที่ 2 ให้หมด ดูภาพดีกว่า จาก B ที่หน้าตาแบบนี้

<img class="aligncenter size-full wp-image-986" title="3dmatrix" src="http://wittawat.com/blog/wp-content/uploads/2012/06/3dmatrix.png" alt="" width="75" height="74" />

จะได้แบบนี้

<img class="aligncenter size-full wp-image-987" title="flatten3dmatrix" src="http://wittawat.com/blog/wp-content/uploads/2012/06/flatten3dmatrix.png" alt="" width="198" height="51" />

ความหมายของ : จึงสรุปได้ว่าถ้าเขียน : x ที จะทำให้มิติที่ 1 ถึงมิติ x-1 มีโครงสร้างตามเดิม ส่วนมิติที่เหลือจะมาต่อที่มิติ x ที่นี้กลับมาที่ A ซึ่งมี 2 มิติ แล้วถ้าเขียน [matlab]A(:,:,:)[/matlab]

อะ? ก็จะได้ A ตามเดิมนั่นแหละ เพราะจริงๆแล้วของ 2 มิติ จะมองให้เป็น 3 มิติก็ได้ โดยที่มิติที่ 3 "เรียบ" คือมีขนาดแค่ 1 (เรียกว่า singleton dimension)

ปิดท้ายสำหรับคนที่รู้เรื่อง reshape คือ

[matlab]
A(:) == reshape(A, [r*c 1]);
B(:,:) == reshape(B, [r, c*d]);
[/matlab]
