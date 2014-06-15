Title: โอกาสเสมอเมื่อ n คนเป่ายิงฉุบกันและ n เข้าสู่อนันต์ (2) 
Date: 2013-01-17 07:06:04
Tags:  
Slug: โอกาสเสมอเมื่อ n คนเป่ายิงฉุบกันและ n เข้าสู่อนันต์ (2) 


<a title="โอกาสเสมอเมื่อ n คนเป่ายิงฉุบกันและ n เข้าสู่อนันต์ (1)" href="http://wittawat.com/blog/?p=1260">โพสต์ก่อนหน้านี้</a> ยังไม่ได้บอกวิธีหาความน่าจะเป็นที่ถูกต้อง คราวนี้มาดูวิธีที่ถูกต้อง

คราวที่แล้วกล่าวไว้ว่าการนับด้วย
<pre> _ | _ | _  _</pre>
จะนับกรณีตัวอย่างแบบนี้
<pre>RPSS, RSPS, SRPS, PSRS ....</pre>
เป็นแบบเดียวกัน และไม่นับซ้ำ คือเหมารวมว่า 1 ครั้ง ซึ่งผิด วิธีที่ถูกคือทุกๆรูปแบบการวาง | 2 อัน เราต้องนับด้วยว่ามีการออกมือที่ตรงกับรูปแบบนั้นได้กี่แบบ เช่น
<pre> _ | _ | _</pre>
มีการออกมือทั้งหมดที่ตรง 6 แบบ (หรือ \(3!\)) คือ
<pre>RPS, RSP, PRS, PSR, SRP, SPR</pre>
สำหรับรูปแบบนี้
<pre> _ | _ _ | _</pre>
ก็จะมีการออกมือที่ตรงทั้งสิ้น \( \frac{4!}{1! 2! 1!} \) แบบ กำหนดให้ตำแหน่งซ้ายสุดคือ 0 และตำแหน่งขวาสุดที่วาง | ได้คือ n และเปลี่ยน | ทั้งสองอันเป็น i, j จะได้ภาพนี้
<pre>0 _ i _ 2 _ j _ 4</pre>
จากภาพ i อยู่ในตำแหน่งที่ 1 และ j อยู่ตำแหน่งที่ 3 ที่เราต้องทำคือ ให้ i วิ่งจาก 1 ไปถึง n-1 แล้วให้ j วิ่งตามหลัง i (\(j&gt;i\)) จากนั้นนับการออกมือที่ตรงกับรูปแบบนั้นๆ เรารู้ว่าจำนวนค้อนคือ i จำนวนกระดาษคือ \(j-i\) และจำนวนกรรไกรคือ \(n-j\)

ฉะนั้นจำนวนการออกมือทั้งหมดที่ค้อน กระดาษ กรรไกรเกิดอย่างน้อย 1 ครั้งคือ

$$ \sum_{i=1}^{n-1}\sum_{j=i+1}^{n-1} \frac{n!}{i! (j-i)! (n-j)!}$$

จำนวนการออกมือทั้งหมดที่เป็นไปไดคือ \(3^n\) เพราะฉะนั้น ความน่าจะเป็นที่ n คนเป่ายิงฉุบกันแล้วเสมอคือ

\begin{align}
P_n &amp;= \frac{1}{3^n} \sum_{i=1}^{n-1}\sum_{j=i+1}^{n-1} \frac{n!}{i! (j-i)! (n-j)!} + P(ออกเหมือนกันหมด) \\
&amp;= \frac{1}{3^n} \sum_{i=1}^{n-1}\sum_{j=i+1}^{n-1} \frac{n!}{i! (j-i)! (n-j)!} + \frac{1}{3^{n-1}} \\
&amp;= \frac{1}{3^n} \sum_{i=1}^{n-1}\sum_{j=i+1}^{n-1} \frac{n!}{(n-j)! j!}\frac{j!}{i! (j-i)! } + \frac{1}{3^{n-1}} \\
&amp;= \frac{1}{3^n} \sum_{i=1}^{n-1}\sum_{j=i+1}^{n-1} \binom{n}{j} \binom{j}{i} + \frac{1}{3^{n-1}} \\
&amp;= \frac{1}{3^n} \sum_{i=1}^{n-1} \left[ \sum_{j=i}^{n} \binom{n}{j} \binom{j}{i} - \binom{n}{i}\binom{i}{i} - \binom{n}{n}\binom{n}{i} \right] +\frac{1}{3^{n-1}} \\
\end{align}

ใช้สูตรจาก<a href="http://en.wikipedia.org/wiki/Binomial_coefficient#Identities_with_combinatorial_proofs">หน้าวิกิเรื่อง Binomial coefficient </a>ที่เขียนว่า Identities with combinatorial proofs เพื่อแทนพจน์แรก สมการด้านบนจึงได้ว่า

\begin{align}
P_n &amp;= \frac{1}{3^n} \sum_{i=1}^{n-1} \left[ 2^{n-i}\binom{n}{i} - 2\binom{n}{i}\right] +\frac{1}{3^{n-1}} \\
&amp;= \left(\frac{2}{3} \right)^n \sum_{i=1}^{n-1} \binom{n}{i} \frac{1}{2^i} - \frac{2}{3^n}(2^n-2) + \frac{1}{3^{n-1}} \\
&amp;= \left(\frac{2}{3} \right)^n \left[ \sum_{i=0}^n \binom{n}{i} \left(\frac{1}{2}\right)^i - \binom{n}{0} - \binom{n}{n}\left(\frac{1}{2}\right)^n \right] - \frac{2}{3^n}(2^n-2) + \frac{1}{3^{n-1}} \\
\end{align}

ใช้สูตรจาก<a href="http://en.wikipedia.org/wiki/Binomial_coefficient#Generalization_and_connection_to_the_binomial_series">หน้าเดิม</a>ที่เขียนว่า Generalization and connection to binomial series เพื่อแทนที่พจน์แรกในวงเล็บจะได้

\begin{align}
P_n &amp;= \left(\frac{2}{3} \right)^n \left[\left(1+\frac{1}{2} \right)^n -1 - \frac{1}{2^n}\right] - \frac{2}{3^n}(2^n-2) + \frac{1}{3^{n-1}} \\
&amp;= 1 - \frac{2^n-2}{3^{n-1}}
\end{align}

ซึ่งค่อนข้างชัดเจนว่า \(\lim_{n \rightarrow \infty} P_n = 1\)　สูตรที่ได้มานี้ตรงกับที่ให้ไว้ใน<a href="http://ja.wikipedia.org/wiki/%E3%81%98%E3%82%83%E3%82%93%E3%81%91%E3%82%93#.E3.81.82.E3.81.84.E3.81.93.E3.81.A8.E3.81.AA.E3.82.8B.E7.A2.BA.E7.8E.87">หน้าวิกิภาษาญี่ปุ่นเรื่องเป่ายิงฉุบ </a>
<h2>เขียน code เพื่อนับการออกมือทั้งหมด</h2>
เพื่อความแน่ใจเลยลองเขียน code Python เพื่อนับจำนวนการออกมือที่มีค้อน กระดาษ กรรไกร อย่างน้อย 1 ครั้งด้วย

[code lang="python"]

def atleast_once_each(c):
  return len(set(x for x in c)) == 3

def sub_gen_draw(n, cand=['']):
  if n &lt; 1: return ()
  if n ==1: return (str(x) for x in xrange(3) )
  else:
    return ( str(i)+c for i in range(3) for c in sub_gen_draw(n-1, cand) )

def gen_atleast1(n):
  if n &lt;= 2: return ()
  return (c for c in sub_gen_draw(n) if atleast_once_each(c))

if __name__ == '__main__':
  for n in xrange(4, 6):
    count = sum(1 for x in gen_atleast1(n) )
    print 'n = %d, #hands = %d' % (n, count)
    for (c,i) in zip(gen_atleast1(n), xrange(1, 3**n+1)):
      print c,
      if i % 10 == 0:
        print
    print

[/code]

กำหนด n แล้วcode นี้จะแสดงการออกมือทั้งหมด เป็น 0, 1, 2 (ค้อน กระดาษ กรรไกร) เหมือนเลขฐาน 3 ถ้าลองนำจำนวนนับที่ได้จาก code มาหารด้วย \(3^n\) แล้วบวกกับความน่าจะเป็นที่ออกเหมือนกันหมดคือ \(\frac{1}{3^{n-1}}\) จะได้ตรงกับสมการข้างบน จึงมั่นใจว่าถูกต้อง
