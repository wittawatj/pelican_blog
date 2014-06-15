Title: ผลรวมของตัวแปรสุ่มแบบ exponential  
Date: 2013-04-18 14:24:58
Tags: probability, statistics 
Slug: ผลรวมของตัวแปรสุ่มแบบ exponential  


โจทย์:

$$X_1, \ldots, X_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\beta) $$

$$Z= \sum_{i=1}^n X_i $$

พิสูจน์ว่า \(Z \sim \text{Gamma}(n, \beta) \) หรือพูดสั้นๆว่าจงพิสูจน์ว่าผลรวมของตัวแปรสุ่มแบบ exponential จะมีการกระจายตัวแบบ Gamma distribution

นิยามของ PDF ของ Gamma และ Exp คือ

$$
\begin{align*}
\text{Gamma}(\alpha, \beta): f(x) &amp;= \frac{1}{\beta^\alpha \Gamma(\alpha)} x^{\alpha-1} e^{-x/\beta} \\
\text{Exp}(\beta): f(x) &amp;= \frac{1}{\beta} \exp(-x/\beta)
\end{align*}
$$

เมื่อ

$$\Gamma(\alpha) = \int_0^\infty t^{\alpha-1} \exp(-t) \, dt$$

คือ <a href="http://en.wikipedia.org/wiki/Gamma_function">Gamma function</a> (generalization ของ factorial) ถ้าอยากลองคิดก็หยุดอ่านตรงนี้
<h2>Proof</h2>
จริงๆแล้ว \(\text{Exp}(\beta) = \text{Gamma}(1, \beta) \) ฉะนั้นมันมีเค้าอยู่ว่า Exp เกี่ยวกับ Gamma แนวคิดในการพิสูจน์คือจะใช้คุณสมบัติของ <a href="http://en.wikipedia.org/wiki/Moment-generating_function">moment-generating function</a> (MGF) ซึ่งกล่าวไว้ว่าถ้า MGF ของ Y มีค่าเท่ากับ MGF ของ Z

$$\psi_Y(t) = \psi_Z(t) $$

Y จะมีการกระจายตัวเหมือน Z สิ่งที่จะทำคือ หา MGF ของ \(Z=\sum_{i=1}^n X_i \) และหา MGF ของ \( Y \sim \text{Gamma}(n, \beta) \) ถ้า MGF 2 อันนี้เหมือนกันก็สรุปว่า \(Z \sim \text{Gamma}(n, \beta) \)
<h3>MGF ของ \(Z = \sum_{i=1}^n X_i \)</h3>
คุณสมบัติอีกหนึ่งอย่างของ MGF คือถ้า \(X_1, \ldots, X_n\) independent กันแล้ว จะได้

$$ \psi_Z(t) = \Pi_{i=1}^n \psi_{X_i}(t) $$

เนื่องจาก \(X_1, \ldots, X_n\) เป็น i.i.d กัน ทั้งหมดจะมี MGF เหมือนกันซึ่งก็คือ

$$ \psi_X(t)  = \mathbb{E}[ \exp(tX) ] = \frac{1}{1-\beta t} $$

เราจึงได้

$$ \psi_Z(t) = \frac{1}{ (1-\beta t)^n } $$
<h3>MGF ของ \(Y \sim \text{Gamma}(n, \beta) \)</h3>
$$
\begin{align*}
\psi_Y(t) &amp;= \mathbb{E}[\exp(tY)] \\
&amp;= \frac{1}{\beta^n \Gamma(n)}  \int_0^\infty \exp(ty) y^{n-1} \exp(-y/\beta) \, dy \\
&amp;= \frac{1}{\beta^n \Gamma(n)}  \int_0^\infty  y^{n-1} e^{y (t - 1/\beta)} \, dy
\end{align*}
$$

ตรงนี้จะเห็นว่าใน integral หน้าตาคล้ายกับ Gamma function น่าจะทำให้เป็น Gamma function แล้วตัดกับส่วนที่อยู่ด้านล่างได้ กำหนดให้

$$
\begin{align*}
u &amp;:= -y(t - 1/\beta ) \\
y &amp;= -\frac{u}{t-1/\beta} \\
dy &amp;= -\frac{1}{t-1/\beta} \, du
\end{align*}
$$

แทนเข้าไปข้างบนจะได้

$$
\begin{align*}
\mathbb{E}[\exp(tY)] &amp;= \frac{1}{\beta^n \Gamma(n)}  \int_0^\infty  (-1)^{n-1} \left(\frac{u}{t-\beta}\right)^{n-1} e^{-u}  \frac{(-1)}{t-1/\beta} \, du \\
&amp;= \frac{1}{\beta^n \Gamma(n)} \frac{ (-1)^n }{ (t-1/\beta)^n} \overbrace{\int_0^\infty  u^{n-1} e^{-u}  }^{\Gamma(n)} \, du \\
&amp;= \frac{1}{ (1-\beta t)^n }
\end{align*}
$$

แปลว่า \(\psi_Y(t) = \psi_Z(t) \) จึงสรุปว่า \(Z \sim \text{Gamma}(n, \beta) \)
