Title: งงกับ closure ของ Python 
Date: 2012-06-02 08:26:48
Tags: python 
Slug: งงกับ closure ของ Python 


วันนี้นั่งหา bug มานาน สุดท้ายก็เจอ แต่ไม่ใช่ bug แต่เป็นความเข้าใจผิดนิดหน่อย ต่อไปนี้เป็น code Python ที่เขียนขึ้นมาทดสอบไอเดีย

[python]

def funcList():
    lists = []
    for x in ['1','2']:
        for y in ['a', 'b']:
            f = lambda: x+y
            lists += [f]
    return lists

if __name__ == '__main__':
    for f in funcList():
        print f()
[/python]

code นี้จะ print ออกมา 4 บรรทัด ถ้าคิดว่าได้แบบนี้
<pre>1a
1b
2a
2b</pre>
ยินดีด้วย คุณเข้าใจผิดเหมือนผม คงเป็นเพราะ background จากภาษาอื่นทำให้คิดแบบนั้น จริงๆมันได้
<pre>2b
2b
2b
2b</pre>
ทำไม? เพราะ lambda ถูกนิยามใน environment ของ funcList และ x, y ใน lambda จะ bind กับ ตัวแปร x,y ไม่ใช่ bind กับค่าใน x, y ณ ตอนที่ lambda ถูกนิยาม ตอนรันจึงได้ x, y เป็นค่าสุดท้ายหลังจาก for loop รันเสร็จ ซึ่งก็คือ 2, b

ถ้าอยากให้ x, y bind กับค่าของ x, y ณ ตอนนั้น ก็ต้องสร้าง environment ใหม่ที่ x, y ไม่เปลี่ยนแปลง แล้วไป bind กับ x, y ใน environment ใหม่นั่น แบบนี้

[python]
def funcList2():
    def ffPlus(x,y):
        return lambda: x+y
    lists = []
    for x in ['1','2']:
        for y in ['a', 'b']:
            f = ffPlus(x,y)
            lists += [f]
    return lists
[/python]

ตัวอย่างที่ 2 นี้ ตรง

[python]lambda: x+y[/python]

อยู่ใน environment ของ ffPlus ซึ่งไม่มีการเปลี่ยนค่าของ x, y เลย ถ้าใช้ funcList2 ใน main อันเดิมจะได้
<pre>1a
1b
2a
2b</pre>
ข้อมูล
<ul>
	<li><a href="http://stackoverflow.com/questions/233673/lexical-closures-in-python">http://stackoverflow.com/questions/233673/lexical-closures-in-python</a></li>
	<li><a href="http://en.wikipedia.org/wiki/Closure_%28computer_science%29">http://en.wikipedia.org/wiki/Closure_%28computer_science%29</a></li>
</ul>
