Title: Matlab: bsxfun 
Date: 2011-08-16 10:08:57
Tags: matlab 
Slug: Matlab: bsxfun 


bsxfun เป็น function ที่มากับ Matlab รุ่นหลังๆ รูปแบบการใช้งานคือ

[matlab]C = bsxfun(func, A, B) [/matlab]

เมื่อ func คือ function handle ของ function อะไรบางอย่างที่รับ 2 arguments (เป็นตัวเลข) และ A, B คือ vector หรือ matrix ที่มีขนาดเดียวกัน หน้าที่ของ bsxfun คือเรียก func ที่ส่งเข้ามาโดยใช้ตัวเลขใน A และ B เป็น argument ของ function พูดง่ายๆคือ

[matlab]C(i,j) = func(A(i,j), B(i,j))[/matlab]

ทุกๆ i,j C จะเป็น matrix ที่มีขนาดเท่า A, B การใช้งานแบบนี้จะให้ผลคล้ายกับ arrayfun

จริงๆแล้วประโยชน์ที่แท้จริงของ bsxfun จะเกิดเมื่อ A มีขนาดของ dimension หนึงเล็กกว่าใน B เช่น ให้ B เป็น mxn matrix และ A มีขนาด mx1 แล้วเราอยากให้ C มีผลลัพธ์แบบนี้

[matlab] C(i,j) = func(A(i), B(i,j)) [/matlab]

ในกรณีนี้สามารถใช้ bsxfun  แบบข้างบนได้เลย เพราะ bsxfun จะ "ยืด" A ให้มีขนาดเท่า B โดยอัตโนมัติ ตัวอย่างที่ใช้บ่อยคือการหักค่าเฉลี่ยออกจากข้อมูล ให้ X เป็น mxn matrix เมื่อ m เป็นจำนวน feature และ n เป็นจำนวนตัวอย่างของข้อมูล ถ้าเราอยากหักค่าเฉลี่ยออกจากทุกๆตัวอย่างใน X สามารถทำได้แบบนี้

[matlab] NX = bsxfun(@minus, X, mean(X,2))[/matlab]

แค่นี้ NX ก็จะเป็น matrix ของข้อมูลโดยที่ค่าเฉลี่ยเป็น 0 ปกติคนส่วนใหญ่มักไม่ใช้คำัสั่งข้างบน แต่จะใช้ repmat แบบนี้

[matlab] NX = X - repmat(mean(X,2), 1, n) [/matlab]

ซึ่งให้ผลเหมือนกัน แต่ repmat กิน memory โดยไม่จำเป็นเพราะต้อง copy vector ค่าเฉลี่ย n ครั้ง เข้าใจว่า bsxfun ไม่น่าจะ copy ข้อมูลใดๆ น่าจะเร็วและกิน memory น้อยกว่า
