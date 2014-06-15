Title: Matlab: หา min บน matrix 3 มิติ 
Date: 2012-05-30 04:57:26
Tags: matlab 
Slug: Matlab: หา min บน matrix 3 มิติ 


สมมติเรามี matrix E ซึ่งมีขนาดดังนี้

[matlab] [a b c] = size(E)[/matlab]

แล้วเราอยากหา min ใน E รวมไปถึง index (i, j, k) เพื่อเข้าถึงค่า min นั้นด้วย อันนี้ใช้บ่อยตอนทำ cross validation เช่น 3 มิตินี้อาจจะมาจากว่าเรามี parameter ที่ต้องปรับอยู่ 3 ตัว เราเลยลองหา error โดยใช้ parameter candidate ที่เตรียมไว้ก็เลยได้ matrix มา 3 มิติที่เก็บค่า error ที่นี้ก็เลยอยากรู้ error ที่น้อยที่สุด รวมไปถึง index (i, j, k) ด้วย จะได้รู้ว่าจะต้องใช้ parameter ตัวไหนให้ได้ error น้อยที่สุด

วิธีคือ

[matlab][m, li] = min(E(:));
[i, j, k] = ind2sub(size(E), li);[/matlab]

อธิบายได้ว่า E(:) คือการทำให้ E กลายเป็น array 1 มิติ (ซึ่งจริงๆ matrix ใน Matlab ก็เป็น array 1 มิติอยู่แล้ว ลองอ่านโพสเรื่อง "<a title="Matlab เก็บ matrix อย่างไร" href="http://wittawat.com/blog/?p=936">Matlab เก็บ matrix อย่างไร</a>") เมื่อได้ array 1 มิติแล้วก็หา min ก็ได้ค่า error ที่น้อยที่สุดเป็น m แล้วก็ได้ li (linear index) เป็นตำแหน่งแบบ 1 มิติบน E ที่ให้ค่า min นั้น บรรทัดที่ 2 ก็คือการแปลงเจ้า linear index li ให้เป็น index แบบ 3 มิติตามเดิม ซึ่งจะได้ i, j, k มา แล้วก็จะรู้ว่าตำแหน่งไหนใน matrix E ให้ค่า min

จริงๆแล้วมีวิธีทั่วไปที่คนชอบใช้ คือใช้ min ดื้อๆบน matrix 3 มิติเลย ไม่แปลงเป็นแบบ 1 มิติ แต่เนื่องจาก min ทำได้แค่การหาค่าต่ำสุดทีละมิติ ทำให้ต้องใช้ min หลายที ทีละมิติ อ่าน code แล้วจะงง ไม่ขอกล่าวถึงวิธีนั้น
