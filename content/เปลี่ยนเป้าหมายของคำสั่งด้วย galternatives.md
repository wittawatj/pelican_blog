Title: เปลี่ยนเป้าหมายของคำสั่งด้วย galternatives 
Date: 2009-09-19 12:01:21
Tags: linux, ubuntu 
Slug: เปลี่ยนเป้าหมายของคำสั่งด้วย galternatives 


ใน Ubuntu (หรือ Linux อื่นๆด้วย) คำสั่งหนึ่งคำสั่งอาจมีโปรแกรมที่สามารถถูกเรียกใช้ได้อยู่หลายอัน ยกตัวอย่างเช่นคำสั่ง java โปรแกรมที่ใช้รันคำสั่งนี้จริงๆอาจเป็น JRE ของ Sun เอง, GCJ หรือ OpenJDK ก็ได้  การเลือกว่าจะให้ใช้อันไหนสามารถทำได้โดยใช้คำสั่งต่อไปนี้ [bash]sudo update-alternatives --config some_command_here[/bash]

จะมีเมนูขึ้นมาให้เลือก

อีกวิธีหนึ่งคือทำผ่าน GUI โดยลงโปรแกรมชื่อ galternatives ด้วยคำสั่งนี้ก่อน [bash]sudo apt-get install galternatives[/bash]

จากนั้นเลือกเมนู Applications -&gt; System Tools จะมีโปรแกรมชื่อ Alternatives Configurator เพิ่มขึ้นมา กดเพื่อเปิดขึ้นมาจะมีหน้าตาแบบนี้

<img class="aligncenter size-full wp-image-280" title="Screenshot-G Alternatives" src="http://wittawat.com/blog/wp-content/uploads/2009/09/Screenshot-G-Alternatives.png" alt="Screenshot-G Alternatives" width="598" height="510" />ด้านซ้ายเป็นคำสั่งต่างๆที่มีอยู่ เมื่อเลือกคำสั่งแต่ละอันด้านขวาจะมีโปรแกรมตัวเลือกที่เป็นไปได้เพื่อใช้กับคำสั่งที่เลือก ในตัวอย่างเป็นตัวเลือกของคำสั่ง java

ที่มา
<ul>
	<li><a href="http://groups.google.com/group/Google-Web-Toolkit/browse_thread/thread/f75ed85162639b32">http://groups.google.com/group/Google-Web-Toolkit/browse_thread/thread/f75ed85162639b32</a></li>
</ul>
[ad#afterpost]
