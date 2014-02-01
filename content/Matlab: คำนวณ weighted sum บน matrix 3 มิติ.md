Title: Matlab: คำนวณ weighted sum บน matrix 3 มิติ 
Date: 2011-09-11 03:51:40
Tags: matlab 
Slug: Matlab: คำนวณ weighted sum บน matrix 3 มิติ 


มีคนที่แล็บถามมาว่าจะคำนวณ weighted sum บน matrix 3 มิติได้อย่างไร ตอบเสร็จเลยมาเขียนไว้ซะหน่อย

สมมติว่ามีข้อมูลเก็บอยู่ใน matrix 3 มิติ A ขนาด m x n x p (ถ้านึกไม่ออก ตัวอย่างเช่น m x n อาจเป็นขนาดของรูป แล้วเรามี p รูป เป็นต้น) และมี vector V ขนาด p ซึ่งอาจจะเป็น weight อะไรบางอย่าง ตามรูปนี้

<img class="aligncenter size-full wp-image-715" title="text3179" src="http://wittawat.com/blog/wp-content/uploads/2011/09/text3179.png" alt="" width="442" height="193" />

คำถามคือ จะหาผลรวมของ A (ในมิติที่ 3) แบบถ่วงน้ำหนักด้วย V (ผลลัพธ์จะเป็น matrix ขนาด m x n) ใน Matlab ควรทำอย่างไร ปกติใน Matlab การหาผลรวมในมิติที่ 3 ก็แค่ใช้คำสั่ง [matlab]sum(A,3)[/matlab]

ก็ได้แล้ว แต่ถ่วงน้ำหนักด้วยอาจจะวุ่นวายนิดหน่อย

ก่อนจะพูดเรื่อง 3 มิติ ลองคิดแบบ 2 มิติก่อน สมมติมีข้อมูลเก็บอยู่ใน matrix D ขนาด m x p แล้วมี vector W ขนาด p แล้วเราอยากหาผลรวมในมิติที่ 2 ของ D โดยถ่วงน้ำหนักด้วย W (ผลลัพธ์เป็น vector ขนาด m) กรณีนี้ง่ายมาก ใช้คำสั่ง [matlab]D*W[/matlab]

ก็ได้แล้ว

กลับมาที่ 3 มิติ แนวคิดคือ เปลี่ยน A ให้เป็น matrix ขนาด mn x p ก่อน (เรียก matrix ใหม่ว่า B) แล้วหาผลรวมแบบถ่วงน้ำหนักแบบ 2 มิติบน B  จะได้ผลลัพธ์เป็น vector ขนาด mn จากนั้นค่อยเปลี่ยนเป็น matrix ขนาด m x n ซึ่งเขียนได้แบบนี้

[matlab] B = reshape(A, m*n, p); C = reshape(B*V, m, n) [/matlab]

C คือ matrix ขนาด m x n ที่เราอยากได้

[ad#afterpost]
