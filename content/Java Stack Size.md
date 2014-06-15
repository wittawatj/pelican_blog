Title: Java Stack Size 
Date: 2008-05-22 01:35:00
Tags:  
Slug: Java Stack Size 


เป็นที่รู้กันว่าโปรแกรม Java หรือโปรแกรมเขียนจากภาษาอื่นๆก็ด้วย เวลาเรียก subroutine (หรือ method)หนึ่งครั้ง stack frame จะถูกสร้างขึ้นมา คิดว่า Java คงไม่ทำพวก <a href="http://en.wikipedia.org/wiki/Tail_recursion">tail call transform</a> มั้ง<br /><br />ช่วงนีต้องใช้ Regular expression ใน Java บ่อย แถมใช้ expression ยาวๆยุ่งๆมากด้วย บางครั้งโปรแกรมรันอยู่ก็เกิด Stack over flow ขึ้น เข้าใจว่า regular expression ที่ใช้มันคงจะซับซ้อน (มั้ง)<br /><br />ตามปกติขนาดของ stack ที่ Java (Client VM) ให้มาก็ใช้พอตลอด ไม่รู้ว่าขนาดของ stack เป็นเท่าไหร่กันแน่ มีเว็บหนึ่งบอกว่า Java stack ตอนแรกจะให้ไว้ 128k (ไม่รู้หน่วยอะไร, วัดยังไงก็ไม่รู้) แต่ครั้งนี้จำเป็นต้องขยายขนาดของ Stack ซึ่งวิธีที่ใช้ก็คือ:<br /><br />java -oss2m -ss2m MyProgram<br /><br />เราเพิ่ม parameter ไปอีก 2 ตัวตอนรันโปรแกรม<br /><ul><li>-oss นี่คือการตั้งขนาดของ Java stack หรือ VM stack (ข้อมูลไม่แน่นอน)<br /></li><li>-ss คือ การตั้งขนาดของ native stack (ข้อมูลไม่แน่นอน)<br /></li></ul>แล้ว stack 2 อย่างนี้คืออะไร? ต่างกันอย่างไร? คนเขียนก็ไม่รู้ ฮ่า ฮ่า  ไว้รู้แล้วค่อยมาเขียนเพิ่ม แต่ที่รู้ตอนนี้คือตั้งเป็น 2m แล้ว regular expression ที่เขียนมันรันได้ก็แล้วกัน
