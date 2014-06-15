Title: Orchid Corpus 
Date: 2008-06-05 10:47:00
Tags:  
Slug: Orchid Corpus 


ช่วงนี้ได้มีโอกาสลองเล่นกับ Orchid ซึ่งเป็น <a href="http://en.wikipedia.org/wiki/Text_corpus">Corpus</a> ภาษาไทยที่มีมาเป็น 10 ปีกว่าแล้ว ตั้งแต่ 1997  มีการกำกับ POS (part of speech) ไว้ทุกคำ (กำกับเฉพาะคำไทย ไม่กำกับคำอังกฤษ)  Orchid corpus นี้ได้รวบรวมเอกสารไว้มากมาย โดยย่อหน้าและประโยคในแต่ละเอกสารจะถูกกำกับไว้หมด (โดยคน) มีตัวอย่างของเนื้อหาใน corpus ให้ดูด้วย อันนี้เป็นเพียง 1 เอกสารในนั้นนะ
<pre>%TTitle: การประชุมทางวิชาการ ครั้งที่ 1
%ETitle: [1st Annual Conference]
%TAuthor:%EAuthor:
%TInbook: การประชุมทางวิชาการ ครั้งที่ 1, โครงการวิจัยและพัฒนาอิเล็กทรอนิกส์และคอมพิวเตอร์, ปีงบประมาณ 2531, เล่ม 1
%EInbook: The 1st Annual Conference, Electronics and Computer Research and Development Project, Fiscal Year 1988, Book 1
%TPublisher: ศูนย์เทคโนโลยีอิเล็กทรอนิกส์และคอมพิวเตอร์แห่งชาติ, กระทรวงวิทยาศาสตร์ เทคโนโลยีและการพลังงาน
%EPublisher: National Electronics and Computer Technology Center, Ministry of Science, Technology and Energy
%Page:
%Year: 1989
%File:
#P1
#1
การประชุมทางวิชาการ ครั้งที่ 1//
การ/FIXN
ประชุม/VACT
ทาง/NCMN
วิชาการ/NCMN
&lt;space&gt;/PUNC
ครั้ง/CFQCที่ 1/DONM//
#2
ประโยคต่อไป............</pre>
ใน corpus ก็จะมีข้อความลักษณะนี้ซ้ำๆกันไปเรื่อยๆ ทุกครั้งที่ขึ้นต้นเอกสารใหม่ ก็จะมีพวก %TTitle, %ETitle,.. พวกนี้ขึ้นนำ tag พวกนี้คิดว่าสื่อความหมายตรงตัวอยู่แล้ว
<ul>
	<li>%TTitle แปลว่าหัวเรื่องภาษาไทย</li>
	<li>%ETitle หัวเรื่องภาษาอังกฤษ</li>
	<li>%TAuthor ชื่อผู้แต่งภาษาไทย</li>
	<li>%EAuthor ชื่อผู้แต่งภาษาอังกฤษ</li>
	<li>%TInbook ชื่อหนังสือของบทความนี้ (ภาษาไทย)</li>
	<li>%EInbook ชื่อหนังสือของบทความนี้ (ภาษาอังกฤษ)</li>
	<li>%TPublisher ชื่อสำนักพิมพ์เป็นภาษาไทย</li>
	<li>%EPublisher ชื่อสำนักพิทพ์เป็นอังกฤษ</li>
	<li>%Page หน้าในหนังสือ</li>
	<li>%Year ปีที่ตีพิมพ์</li>
	<li>%File อะไรซักอย่าง ?</li>
</ul>
ต่อจาก metadata พวกนี้ก็จะเป็นย่อหน้าของเนื้อหา จากตัวอย่างข้างต้น #P1 แปลว่าย่อหน้าที่ 1 ต่อไปก็จะเป็นประโยค #1 แปลว่า ประโยคที่ 1 #2 ก็ประโยคที่ 2 จะเป็นแบบนี้ไปเรื่อยๆ ทุกครั้งที่ขึ้นย่อหน้าใหม่ประโยคในย่อหน้าจะนับใหม่เริ่มที่ #1

บรรทัดต่อจากหมายเลขประโยคก็จะเป็น เนื้อความของประโยคนั้นๆ // ด้านหลังแปลว่าจบประโยคแล้ว ในบางกรณีอาจมี \\ ด้วย ซึ่งแปลว่าขึ้นบรรทัดใหม่ หลังจากบอกเนื้อความของประโยคแล้ว (หลังจาก //) ก็จะเป็น การแจงคำและหน้าที่ของคำในประโยคนั้น จากตัวอย่าง คำว่า "ทาง" เป็น NCMN หรือ common noun , คำว่า "ประชุม" เป็น VACT เป็น active verb นั่นเอง

&lt;space&gt; ไม่ใช่คำ แต่หมายถึงวรรค ที่ใช้ &lt;space&gt; นี่เพื่อไม่ให้เกิดความกำกวม และยังมีเครื่องหมายอื่นๆอีกที่ต้องเปลี่ยน เช่น / จะใช้เป็น &lt;slash&gt;

หน้าที่ของคำใน Orchid มีทั้งสิ้น 47 แบบ และยังมีรายละเอียดย่อยอื่นๆอีก ถ้าอยากรู้ก็ดูได้ที่
<ul>
	<li><a href="http://www.blogger.com/www.tcllab.org/virach/paper/virach/thai-l-resource.pdf"><span class="a">www.tcllab.org/virach/paper/virach/thai-l-resource.pdf</span></a></li>
	<li><a href="http://www.blogger.com/www.hlt.nectec.or.th/Publications/Conferences/Thai%20Corpora%20Toolkit.pdf"></a><a>www.hlt.nectec.or.th/Publications/</a><a>Conferences/Thai%20Corpora%20Toolkit.pdf</a></li>
</ul>
