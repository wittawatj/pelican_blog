Title: ขีดเส้นใต้หัวเรื่องในทุก slide ของ beamer 
Date: 2013-03-03 06:18:33
Tags: beamer, latex 
Slug: ขีดเส้นใต้หัวเรื่องในทุก slide ของ beamer 


slide ที่สร้างจาก beamer โดยปกติหัวเรื่องในทุกๆ slide จะไม่มีการขีดเส้นใต้ ถ้าจะใส่เส้นใต้ให้ทำดังนี้

[code lang="latex"]
\usepackage{ulem}
[/code]

แล้วต่อด้วย

[code lang="latex"]
\newcommand\oruline{\bgroup\markoverwith
{\textcolor{orange}{\rule[-0.5ex]{2pt}{0.8pt}}}\ULon}

\setbeamertemplate{frametitle}{\vspace{2mm} \hspace*{-2mm}  \mbox{\oruline{\insertframetitle}} }
[/code]
<ul>
	<li>บรรทัดแรกเราสร้างคำสั่งใหม่ชื่อ \oruline เพื่อขีดเส้นใต้เป็นสีส้ม 0.8pt คือความหนาของเส้น</li>
	<li>บรรทัดที่สองตั้งให้ frametitle (หัวเรื่องของทุก slide) มีเส้นใต้โดยใช้คำสั่ง \setbeamertemplate ซึ่งเอาไว้เปลี่ยนแม่แบบใน beamer</li>
	<li>ค่าของ \vspace และ \hspace* เอาไว้เลื่อนตำแหน่งของหัวเรื่อง สามารถปรับได้ตามความเหมาะสม</li>
</ul>
\setbeamertemplate ยังสามารถเปลี่ยนจุดอื่นๆได้อีกมากม<cite></cite>าย ลองดู cheat sheet สำหรับ beamer template <a href="http://www.cpt.univ-mrs.fr/~masson/latex/Beamer-appearance-cheat-sheet.pdf">ที่นี่</a>
