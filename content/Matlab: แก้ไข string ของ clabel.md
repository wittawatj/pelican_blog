Title: Matlab: แก้ไข string ของ clabel 
Date: 2011-08-02 11:17:35
Tags: matlab 
Slug: Matlab: แก้ไข string ของ clabel 


ใน Matlab มีหลายครั้งที่ต้องใช้ function clabel ควบกับ contour เพื่อกำกับค่าของ contour ปัญหาคืออยากแก้ข้อความที่ถูกนำไปกำกับค่า contour เช่น อยากใช้ทศนิยมแค่ 1 ตำแหน่ง เป็นค้น วิธีคือ [matlab] R = clabel(....) [/matlab]

R จะเป็น double array ของ handles ของข้อความ ถ้าจะแก้ข้อความก็แค่ไล่ทีละ handle ใน R แล้วใช้คำสั่งประมาณนี้ [matlab] set(r(i), 'String', 'new value') [/matlab]

ก็ได้แล้ว
