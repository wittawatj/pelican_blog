Title: คำสั่ง add-apt-repository กับ Jaunty 
Date: 2010-10-02 05:24:31
Tags: ubuntu 
Slug: คำสั่ง add-apt-repository กับ Jaunty 


Ubuntu ตั้งแต่ Karmic Koala (9.10) มีคำสั่งเพิ่มมาอันหนึ่งคือ add-apt-repository สำหรับเพิ่ม repository ผ่าน command line ได้อย่างสะดวก ปัญหาคือคนใช้ Ubuntu รุ่นก่อน 9.10 จะไม่สามารถใช้ได้ อย่างเช่น ผมในขณะนี้ยังใช้ Jaunty Jackalope (9.04) อยู่

วิธีแก้คือให้โหลด package ชื่อ python-software-properties มาใช้ แต่อย่าโหลดจาก apt-get เพราะมันจะเป็นตัวที่ไม่มีคำสั่งนี้อยู่ดี ให้โหลดจาก <a href="http://ns2.canonical.com/karmic/all/python-software-properties/download">http://ns2.canonical.com/karmic/all/python-software-properties/download</a> แล้วลงซะ ก็จะใช้ add-apt-repository ได้
