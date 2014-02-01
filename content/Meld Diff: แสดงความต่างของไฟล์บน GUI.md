Title: Meld Diff: แสดงความต่างของไฟล์บน GUI 
Date: 2010-01-27 02:55:43
Tags: ubuntu 
Slug: Meld Diff: แสดงความต่างของไฟล์บน GUI 


meld เป็นโปรแกรมที่สามารถแสดงความต่างของไฟล์ 2 ไฟล์ได้ คล้ายๆกับคำสั่ง diff แต่ meld มี GUI ให้ดูสวยๆ วิธีใช้คือ อันดับแรกติดตั้ง meld ก่อน

[bash]sudo apt-get install meld[/bash]

เมื่อติดตั้งเสร็จโปรแกรมนี้จะขึ้นมาที่เมนู Applications-&gt;Programming-&gt;Meld Diff Viewer การใช้งานก็กดปุ่ม New แล้วเลือกไฟล์ที่ต้องการเปรียบเทียบ

แต่เพื่อเป็นการเพิ่มความสะดวก ให้ลง diff-ext อีกอันด้วยจะดี

[bash]sudo apt-get install diff-ext[/bash]

เจ้าโปรแกรมอันหลังนี่จะทำให้มีเมนูเพิ่มขึ้นเวลาเราคลิ๊กขวาที่ไฟล์ใน nautilus นั่นคือเราสามารถเลือกไฟล์ 2 ไฟล์แล้วสั่ง compare โดยการคลิ๊กขวาเลือก compare ได้เลย

เนื่องจาก diff-ext เป็นแค่ตัวที่ทำให้มี context menu เพิ่ม ไม่ได้เกี่ยวกับ meld แต่อย่างใด ฉะนั้นก่อนที่จะใช้งานปุ่มคลิ๊กขวานั่นได้เราต้องตั้งโปรแกรมที่จะเอาไว้ใช้ compare ก่อน (ทำแค่ครั้งแรกครั้งเดียว) ในที่นี้จะเลือกใช้ meld นี่แหละเป็นตัวเปรียบเทียบไฟล์ วิธีตั้งให้ไปที่ Applications-&gt;Programming-&gt;Diff-ext จะมีหน้าต่างเล็กๆขึ้นมาให้เลือกใช้ meld ซึ่งบน Ubuntu จะอยู่ที่ /usr/bin/meld ดังภาพ

<img class="aligncenter size-full wp-image-320" title="Screenshot-Diff-ext Setup" src="http://wittawat.com/blog/wp-content/uploads/2010/01/Screenshot-Diff-ext-Setup.png" alt="Screenshot-Diff-ext Setup" width="336" height="164" />

กด ok แล้วก็สามารถใช้งานโดยการเลือก 2 ไฟล์แล้วกด compare ได้เลย หรือจะเลือกที่ละไฟล์โดยกด compare later ก็ได้ แล้วค่อยไปเลือกอีกไฟล์ทีหลัง

ปกติพวก diff tool จะถูกเอามาใช้กับ source code บ่อย แต่เอามาใช้กับอย่างอื่นก็ได้ผลดีนะ เช่น เทียบผลการตัดคำ ดังภาพด้านล่าง

<a href="http://wittawat.com/blog/wp-content/uploads/2010/01/Screenshot-article_00161_ans.txt-tok3_article_00161.txt-Meld2.png"><img class="aligncenter size-medium wp-image-325" title="Screenshot-article_00161_ans.txt : tok3_article_00161.txt - Meld" src="http://wittawat.com/blog/wp-content/uploads/2010/01/Screenshot-article_00161_ans.txt-tok3_article_00161.txt-Meld2-300x157.png" alt="Screenshot-article_00161_ans.txt : tok3_article_00161.txt - Meld" width="323" height="168" /></a>
