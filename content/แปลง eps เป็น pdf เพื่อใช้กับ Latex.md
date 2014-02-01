Title: แปลง eps เป็น pdf เพื่อใช้กับ Latex 
Date: 2010-11-15 12:56:30
Tags: beamer, latex 
Slug: แปลง eps เป็น pdf เพื่อใช้กับ Latex 


ปกติคนใช้ Latex ส่วนใหญ่ใช้เพื่อสร้างเป็น PDF หรือนั่นก็คือใช้คำสั่ง pdflatex นั่นเอง ประเด็นคือเจ้า pdflatex นี่เท่าที่เข้าใจมันไม่รับภาพพวก eps ถ้าอยากได้ eps ก็ใช้ latex เฉยๆใช้คำสั่ง pdflatex ไม่ได้ ที่นี้ปัญหาเลยเกิดเมื่ออยากใช้ eps กับ PDF เช่นกรณีใช้ beamer ทำ slide แล้วอยากใส่ภาพ eps ที่ได้มาจาก Matlab

วิธีหนึ่งคือให้ save ภาพจาก Matlab เป็น eps แล้วแปลงด้วยคำสั่ง

[bash]ps2pdf  -dEPSCrop  somefile.eps[/bash]

ตรง option -dEPSCrop  นี่งมอยู่นาน คือถ้าไม่ใส่ option นี้จะทำให้ภาพที่ได้บางครั้งโดนตัดเหมือนกับเนื้อที่กระดาษไม่พอเวลา print น่ะเมื่อได้ pdf แล้วก็ใช้คำสั่งใน \includegraphics ใน Latex เหมือนปกติ
