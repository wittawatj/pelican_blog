Title: Connect to MySQL from Java 
Date: 2008-07-11 16:13:00
Tags:  
Slug: Connect to MySQL from Java 


ขั้นตอนการ connect ไป MySQL database จาก Java มีดังนี<br /><ol><li>download MySQL connector จาก <a href="http://dev.mysql.com/downloads/connector/j/">http://dev.mysql.com/downloads/connector/j/</a><br /></li><li>แตก zip ออกมาแล้วเพิ่ม jar ไฟล์ที่อยู่ข้างใน (e.g. mysql-connector-java-5.1.6-bin.jar) ไปที่ classpath</li><li>เริ่มเขียน code ได้เลย</li></ol><span style="font-weight: bold;">ตัวอย่าง<span style="font-weight: bold;"><br /></span></span><br /><pre>Class.forName("com.mysql.jdbc.Driver").newInstance();<br />String url ="jdbc:mysql://localhost:3306/databaseName";<br />Connection con = DriverManager.getConnection(url , "dbuser","dbpassword");<br />Statement stmt = con.createStatement();<br />String q = "select * from test ;";<br />ResultSet rs = stmt.executeQuery(q);<br />while(rs.next()){<br />String col1Value = rs.getString("col1");<br />String col2Value = rs.getString("col2");<br /><br />// Do something with the values....<br /><br />}<br />rs.close();<br />con.close();<br /></pre><br /><span style="font-weight: bold;"><span style="font-weight: bold;"></span></span>
