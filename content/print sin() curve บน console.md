Title: print sin() curve บน console 
Date: 2011-12-16 06:30:55
Tags: challenge 
Slug: print sin() curve บน console 


เจอโจทย์ที่ไหนไม่รู้ลืมแล้ว ให้เขียนโปรแกรมให้ print กราฟ sin แนวตั้งแบบนี้
<pre>                              *
                                   *
                                       *
                                           *
                                              *
                                                *
                                                 *
                                                 *
                                                *
                                              *
                                           *
                                       *
                                   *
                              *
                         *
                   *
              *
          *
      *
   *
 *
*
*
 *
   *
      *
          *
              *
                   *
                        *</pre>
คำตอบแบบใช้ Python
[code lang="python"]
from math import *

lines = 30
width = 50
hpos = (int(width*(1+sin(i*2*pi/lines))/2.0) for i in xrange(1,lines+1))
for p in hpos:
	print(' '*p + '*')
[/code]

