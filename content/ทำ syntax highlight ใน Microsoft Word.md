Title: ทำ syntax highlight ใน Microsoft Word 
Date: 2012-06-20 02:03:52
Tags: code, windows 
Slug: ทำ syntax highlight ใน Microsoft Word 


มีเหตุให้ต้องกลับมาใช้ Microsoft Word ส่วนตัวไม่ชอบ แต่ช่วยไม่ได้ ต้องพิมพ์ code ใน Word แต่อยากได้ syntax highlight คิดถึง listing package ใน Latex นะ แต่ Word รู้สึกจะไม่มีการทำ highlight ให้แบบนั้น

วิธีทำคือให้เอา code ไปใส่ใน<a href="http://notepad-plus-plus.org/"> Notepad++</a> ก่อน เชื่อว่าหลายคนที่เขียน code ใน Windows คงใช้กันอยู่ แล้วเลือกภาษาให้ถูกต้อง (ไปที่ Language แล้วเลือกภาษา) เพื่อให้ Notepad++ ทำ syntax highlight ได้ถูกต้อง จากนั้นเลือก code ที่อยากได้แล้วไปที่
<blockquote>Plugins --&gt; NppExport --&gt; Copy RTF to clipboard</blockquote>
แล้ว code ที่ทำ highlight แล้วจะถูก copy อัตโนมัติ แล้วก็ไปวางใน Word เสร็จแล้ว

<a href="http://superuser.com/questions/39571/how-do-i-easily-highlight-the-syntax-of-php-code-in-word">ที่มา</a>
