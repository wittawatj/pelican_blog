Title: สร้าง graph ที่มีตัวอักษรกรีกด้วย Graphviz + Tikz 
Date: 2010-10-18 14:03:55
Tags:  
Slug: สร้าง graph ที่มีตัวอักษรกรีกด้วย Graphviz + Tikz 


วันนี้ทำการบ้านวิชา Advanced Data Engineering ซึ่งจำเป็นต้องเขียน query tree โปรแกรมที่สร้าง tree แล้ว export เป็นภาพได้มีเยอะแยะ แต่ประเด็นคือเจ้า tree ที่จะเขียนนี่ดันมีตัวอักษรกรีกอยู่ด้วย คนเรียนวิชา database น่าจะเคยเห็นสัญลักษณ์ของ relational algebra ซึ่งจะมีตัวอักษรเช่น [latex]\pi[/latex] และ [latex]\bowtie[/latex] อยู่ ตอนแรกก็ว่าจะใช้ Openoffice วาดๆเอาให้จบๆไป เรื่องยาวเพราะแต่ดันอยากเท่ห์ใช้ Graphviz

หาไปหามาได้ความว่า Graphviz สนับสนุนตัวอักษรพวก ampersand characters เหมือนที่ใช้ใน HTML ด้วย ดูได้ที่นี่ <a href="http://www.w3.org/TR/REC-html40/sgml/entities.html">http://www.w3.org/TR/REC-html40/sgml/entities.html</a> แน่นอนตัวอักษรในนั้นมีตัวอักษรกรีกที่อยากได้เช่นตัว pi อยู่ แต่คิดไปคิดมาเราต้องใช้ตัว [latex]\bowtie[/latex] ด้วย ไม่รู้มีรึป่าว เลยลองอีกวิธีหนึ่ง

วิธีที่ทำคือใช้ Graphviz นั่นแหละ แต่ตรงจุดที่เป็นตัวอักษรแปลกๆ จะใช้วิธีพิมพ์เป็น code name เอาเช่น sigma11, pi12 เป็นต้น จากนั้นใช้โปรแกรม dot2tex

[bash]sudo apt-get install dot2tex[/bash]

แปลง dot ไฟล์ที่ใช้กับ Graphviz มาเป็นคำสั่งของ Tikz ซะ ซึ่งคำสั่งที่ได้สามารถ copy ไปใส่ Latex ได้เลย ค่อนข้างสะดวก ขั้นตอนสุดท้ายคือเมื่อคำสั่งของ Tikz มาอยู่ใน Latex แล้วที่เหลือก็แทนที่ code name แปลกๆพวก sigma11 ให้เป็นตัวอักษรใน Latex จริงๆเช่น $\sigma$ แค่นี้ก็เสร็จแล้ว

อ้อมโลกไปหน่อยแต่วิธีนี้ไม่ยุ่งมากถ้า Graph ไม่ใหญ่มากนัก หรือว่าถ้าใส่ label="$\sigma$" เลยใน dot ไฟล์อาจจะใช้ได้เหมือนกันก็ได้ ใครมีวิธีตรงๆดีกว่านี้กรุณาบอกกันด้วย

<img class="aligncenter size-full wp-image-479" title="qtree_tikz" src="http://wittawat.com/blog/wp-content/uploads/2010/10/qtree_tikz.png" alt="" width="584" height="438" />
