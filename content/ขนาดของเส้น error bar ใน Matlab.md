Title: ขนาดของเส้น error bar ใน Matlab 
Date: 2012-03-16 08:07:19
Tags: matlab, plot 
Slug: ขนาดของเส้น error bar ใน Matlab 


ปกติเวลา plot กราฟที่มี error bar เพื่อแสดงค่า SD ก็ใช้คำสั่ง errorbar ถ้าตอนเรียกใช้ errorbar มีการเปลี่ยนขนาดของเส้นด้วยคำสั่งประมาณนี้ [code lang="matlab"]errorbar(x, y, sd, 'LineWidth', 3)[/code]

ค่านี้ก็จะมีผลไปถึงเส้นของ error bar ด้วย แต่มีบางทีอยากได้ขนาดของเส้น plot กับเส้น error bar ไม่เท่ากัน เช่น อยากให้เส้น plot หนา แต่ error bar บางหน่อย วิธีคือทำแบบนี้

[code lang="matlab"]
eh = errorbar(x, y, sd, 'LineWidth', 3);
C = get(eh, 'Children');
set(C(2), 'LineWidth', 1);
[/code]



เท่าที่เข้าใจคือ Children เป็น sub handle ของ plot โดยรวม C เป็น list มีขนาด 2 อันแรกคืออะไรไม่รู้ อันที่ 2 คือของ error bar
