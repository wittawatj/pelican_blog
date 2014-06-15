Title: Matlab: Inter-Point Distance Matrix 
Date: 2011-03-16 04:08:46
Tags: distance, matlab 
Slug: Matlab: Inter-Point Distance Matrix 


มีหลาย algorithms ใน machine learning ที่ต้องหา distance ระหว่างตัวอย่างทุกๆคู่ใน dataset ตัวอย่างเช่น kNN ที่ต้องหาระยะห่างของตัวอย่างหนึ่งกับตัวอย่างที่อยู่รอบๆ หรือการสร้าง Gram matrix ด้วย kernel บางตัวก็ต้องใช้หา distance ลักษณะนี้เช่นกัน เช่นถ้าใช้ Gaussian kernel ก็จะมี Euclidean distance กำลังสองเป็นส่วนประกอบ

เร็วๆนี้ไปเจอ code Matlab ชุดหนึ่ง<a href="http://www.mathworks.com/matlabcentral/fileexchange/18937">ที่นี่</a> ชื่อ IPDM เขียนไว้ดี เอาไว้หา distance ระหว่างแต่ละตัวอย่างโดยเฉพาะ วิธีใช้เขียนไว้ดีมาก<a href="http://www.mathworks.com/matlabcentral/fx_files/18937/1/content/IPDM/html/demo_ipdm.html">ที่นี่</a>

คำสั่งง่ายสุดคือ

[matlab] D = ipdm(A) [/matlab]

เมื่อ A เป็น matrix โดยที่แต่ละ row เป็น 1 instance ตัวอย่างเช่นถ้า A เป็น matrix ขนาด 10x3 D จะเป็น symmetric matrix ขนาด 10x10 โดยที่ [latex]D_{i,j} = \|A(i,:) - A(j,:)\|_2[/latex]

แน่นอนว่าถ้าใครมี statistics toolbox ใน Matlab จะใช้

[matlab] D=squareform(pdist(A)) [/matlab]

ก็ได้ให้ผลเหมือนกัน (ไม่ได้ลอง เพราะตอนเขียน post นี้ไม่มีให้ลองพอดี) แต่ถ้าไม่มี toolbox นี้ก็ใช้ ipdm ไปก่อนได้

สุดท้าย ipdm นี้มี option สำหรับเปลี่ยนให้ใช้ norm ตัวอื่นได้เช่น 1-norm และสำหรับผู้ที่ใช้ Gaussian kernel อย่าลืมยกกำลังสองที่ matrix D ด้วยนะ เพื่อให้เป็น Euclidean distance กำลังสอง
