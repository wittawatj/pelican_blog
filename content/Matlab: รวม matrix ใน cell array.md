Title: Matlab: รวม matrix ใน cell array 
Date: 2012-05-24 06:34:40
Tags: matlab 
Slug: Matlab: รวม matrix ใน cell array 


มีบางกรณีที่เราจำเป็นต้องใช้ cell array ที่เก็บ matrix 3 มิติ (หรือมิติมากกว่าหรือน้อยกว่านี้ก็ได้) สมมติว่า cell array ชื่อ C มีหน้าตาแบบนี้
<p style="text-align: center;"><img class="size-full wp-image-909 aligncenter" title="def" src="http://wittawat.com/blog/wp-content/uploads/2012/05/def.png" alt="" width="343" height="89" /></p>
<p style="text-align: left;">C มีความยาวเท่าไหร่ก็ได้แต่ในที่นี้ขอแสดงแค่ 2 พอ ส่วน matrix ข้างในมีขนาด mxnxp ตามรูป ที่อยากทำคืออยากรวม matrix เหล่านี้เข้าด้วยกันเป็นอันเดียว อาจจะเพื่อความสะดวกในการคำนวณในขั้นต่อไป เช่น หา mean ตามแนวมิติที่ 3 เป็นต้น วิธีรวมก็มีหลายแบบ วิธีแรกคือใช้ [matlab]cell2mat(C)[/matlab]

ซึ่งจะให้ผลแบบนี้</p>
<p style="text-align: center;"><img title="hcat" src="http://wittawat.com/blog/wp-content/uploads/2012/05/hcat.png" alt="" width="140" height="81" /></p>
<p style="text-align: left;">แนวคิดของ cell2mat คือเอา matrix ใน cell มาต่อกัน โดยดูจากขนาดของ cell เช่น cell C ในที่นี้มีขนาด 1x2 ก็เลยรวมแบบ 1x2 คือเอามาต่อตามแนวนอนแบบที่เห็น โดยทั่วไป cell2mat ไม่ได้ต่อแบบแนวนอนเสมอ ทั้งนี้ขึ้นอยู่กับขนาดของ C แต่ถ้าอยากบังคับให้ต่อแบบแนวนอนเสมอก็ให้ใช้ [matlab]horzcat(C{:})[/matlab]

หรือ [matlab][C{:}][/matlab]

ก็ได้ จะได้ผลเหมือนเดิม</p>
<p style="text-align: left;">แล้วถ้าอยากได้แบบแนวตั้งหละ? ในเมื่อมี horz ก็คงมี vert ฉะนั้นต่อแบบแนวตั้งจึงใช้ [matlab]vertcat(C{:})[/matlab]

แล้วจะได้</p>
<img class="aligncenter" title="vcat" src="http://wittawat.com/blog/wp-content/uploads/2012/05/vcat.png" alt="" width="82" height="131" />

แล้วถ้าจะต่อแบบแนวลึกล่ะ? ในกรณีนี้ให้ใช้ function แบบที่ใส่มิติได้เอง คือใช้ function ชื่อ cat เนื่องจากแนวลึกคือมิติที่ 3 ก็ใช้ cat แบบนี้ [matlab]cat(3, C{:})[/matlab]

แล้วจะได้
<p style="text-align: center;"><img class="alignnone size-full wp-image-908" title="3cat" src="http://wittawat.com/blog/wp-content/uploads/2012/05/3cat.png" alt="" width="112" height="100" /></p>
ที่นี้ถ้าลองคิดดีๆจะเห็นว่าจริงๆแล้ว [matlab]vertcat(C{:}) == cat(1, C{:})[/matlab]

เพราะว่าแนวตั้งคือมิติที่ 1 ใน Matlab เช่นเดียวกัน [matlab]horzcat(C{:}) == cat(2, C{:})[/matlab]

ปิดท้ายโพสนี้ด้วยหมายเหตุนิดหน่อยคือ จริงๆแล้ว matrix ทุกอันไม่จำเป็นต้องมีขนาด mxnxp เท่ากันหมด ถ้าเราต้องการต่อแบบมิติที่ x ขนาดของมิติอื่นต้องเท่ากันหมดแต่มิติ x ไม่จำเป็นต้องเท่า เช่น ถ้าเราอยากต่อแนวลึก ในกรณีนี้ matrix ขนาด mxnxp กับ matrix ขนาด mxnxr ต่อกันได้
