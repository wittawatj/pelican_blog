Title: คุม servo motor 2 ตัวด้วย mouse ผ่าน Arduino และ Processing 
Date: 2012-10-09 15:48:33
Tags: Arduino, mouse, Processing, robot 
Slug: คุม servo motor 2 ตัวด้วย mouse ผ่าน Arduino และ Processing 


post นี้เป็นการจดบันทึกการคุม servo motor 2 ตัวด้วย mouse ผ่าน Arduino และ Processing แบบนี้

http://www.youtube.com/watch?v=U673Kx4i6rE

อันนี้เป็นโปรเจค Arduino อันแรกที่เคยทำเลย
<h3>อุปกรณ์ที่ต้องใช้</h3>
อุปกรณ์ที่สั่งจาก <a href="http://www.arduino.in.th">arduino.in.th</a>
<ul>
	<li>board Arduino (รุ่นไหนก็ได้ แต่ที่เห็นในวิดีโอคือ Arduino Uno R3)</li>
	<li>servo motor 2 ตัว ที่เห็นใช้ Futaba s3003</li>
	<li>สาย jump wire เอาไว้ต่อ servo กับ board (ใช้สายไฟธรรมดาเล็กๆปอกเองก็ได้)</li>
</ul>
จาก <a href="http://inex.co.th">inex.co.th</a>
<ul>
	<li>ฉากเหล็กเพื่อยึด servo ติดกัน และยึดติดกับฐาน</li>
	<li>ตัวต่อพลาสติก และฐานพลาสติก</li>
	<li>น็อตขนาด 3mm ยาวเท่าไหร่ก็ได้ พร้อมน็อตตัวเมีย ใช้กับฉากเหล็กและแผ่นพลาสติก</li>
</ul>
พวกตัวต่อพลาสติกไม่มีก็ได้ หาอะไรยึดให้แน่นได้ก็พอ ที่เห็นในวิดีโอมี <a href="http://www.dfrobot.com/index.php?route=product/product&amp;product_id=264">I/O Expansion Shield</a> ของ dfrobot ด้วย มีแล้วจะต่อ servo ง่าย แต่ไม่จำเป็น ต่อ servo ตรงๆเข้า Arduino ก็ได้
<h3>เขียนโปรแกรมคุม Arduino</h3>
Arduino เป็น board ที่คุมง่ายด้วยภาษาที่เรียกว่า "Arduino C" ซึ่งก็คือ C นี่แหละ ยังไม่รู้สึกถึงความต่าง ตัว board มี pin หลากหลายทั้ง analog และ digital การคุม servo motor ใช้ pin digital เบอร์ 2 ถึง 13 อันไหนก็ได้ การคุม servo ให้หมุนไปที่องศาไหนสามารถทำได้โดยการตั้ง pin ที่ต่อ servo เป็น HIGH ตั้งแต่ 600 microseconds (หมุนไปที่จุดสุดท้ายทวนเข็ม) ถึง 2400 microseconds (หมุนไปที่จุดสุดท้ายตามเข็ม) ส่งสัญญาณสั้นๆแบบนี้เรียกว่า pulse สรุปว่าความยาว pulse คุมองศาของ servo ปกติ servo motor จะหมุนได้ประมาณ 180 องศา servo motor มี 3 สาย สายดำต่อเข้า ground สายแดงต่อเข้า 5v สายขาวเอาไว้ต่อเข้า digital pin เพื่อควบคุม

ต่อไปนี้เป็น code Arduino  C เพื่อคุม servo 2 ตัวโดยสายขาวของทั้งสองต่อเข้ากับ pin 7 และ 8

[code language="C"]
#define LINESIZE 20

const int servoPin1     =  7; // the one below
const int servoPin2     =  8; // the one above
const int servoPins[2] = {servoPin1, servoPin2};

int screenW = 800;
int screenH = 600;

const int minPulse     =  600;  // minimum servo position
const int maxPulse     =  2400; // maximum servo position
int refreshTime  =  20;   // time (ms) between pulses (50Hz)

double xangle = 0.5;          // servo position (horizontal axis) (0 to 1)
double yangle = 0.5;          // servo posiiton (vertical axis) (0 to 1)

long lastPulses[2]   = {0,0};    // recorded time (ms) of the last pulse of 2 servos

int pulseWidth;

void setup() {
  pinMode(servoPin1, OUTPUT);  // Set servo pin as an output pin
  pinMode(servoPin2, OUTPUT);  // Set servo pin as an output pin

  Serial.begin(57600);
  Serial.flush();
  Serial.println(&quot;      Arduino Serial Servo Control from Processing&quot;);
  Serial.println();
}

void loop() {
  char* line=NULL;
  const int coarseness = 2;
  short move = 0;
  if( (line=readLine())!=NULL ){
    Serial.print(&quot;line: &quot;);
    Serial.println(line);

    // assume line is of the form &quot;x,y&quot;
    int x, y;
    sscanf(line, &quot;%d%d&quot;, &amp;x, &amp;y);
    if(x%coarseness==0 || y%coarseness==0){
      Serial.print(&quot;x: &quot;);
      Serial.print(x);
      Serial.println();
      Serial.print(&quot;y: &quot;);
      Serial.print(y);
      Serial.println();

      xangle = (double)x/screenW;
      yangle = (double)y/screenH;
      move=1;
    }else{
      move=0;
    }

    free(line);
  }

  if(move==1){
    preciseServos(xangle, yangle);
  }

}

char* readLine(){
  if(Serial.available()){
    char* line = (char*)malloc(sizeof(char)*LINESIZE);
    char ch = 0;
    int i= 0;
    delay(10);
    // assume one chunk ends with '\n'
    while(1){
      if( (ch=Serial.read())!='\n' ){
        if(ch!=-1){ //-1 means no input
          line[i++] = ch;
        }else{
          delay(5);
        }
      }else{
        line[i++]='&#92;&#48;';
        return line;  // assume we get &quot;x y&quot;
        // don't forget to free
      }
    }

  }
  return NULL;

}
// parameterize the angle of servo from 0 to 1.
void preciseServos(double xangle, double yangle){

  int pulsex = (int) ( (maxPulse - minPulse)*xangle + minPulse );
  int pulsey = (int) ( (maxPulse - minPulse)*yangle + minPulse );
  // error protection
  pulsex = constrain(pulsex, minPulse, maxPulse);
  pulsey = constrain(pulsey, minPulse, maxPulse);

  driveServo(0, pulsex);
  driveServo(1, pulsey);

}

void driveServo(int servoIndex, int pulseWidth){
  // pulse the servo every 20 ms (refreshTime) with current pulseWidth
  // this will hold the servo's position if unchanged, or move it if changed
  if (millis() - lastPulses[servoIndex] &gt;= refreshTime) {
    digitalWrite(servoPins[servoIndex], HIGH);   // start the pulse
    delayMicroseconds(pulseWidth);  // pulse width
    digitalWrite(servoPins[servoIndex], LOW);    // stop the pulse
    lastPulses[servoIndex] = millis();           // save the time of the last pulse
  }
}

[/code]

ใน Arduino C มี function เริ่มต้น 2 ตัวคือ setup() และ loop()
<ul>
	<li>setup() เอาไว้ตั้งค่าเริ่มต้นของโปรแกรม ปกติเอาไว้ตั้งว่า pin ไหนเป็น input, output</li>
	<li>loop() เป็น function หลักที่ Arduino จะเรียกซ้ำๆไปเรื่อยๆ เพื่อทำอะไรต่างๆ</li>
</ul>
จาก code ข้างบน ใน setup() เราตั้งให้ pin ที่คุม servo ทั้ง 2 เป็น OUTPUT จะได้ส่งสัญญาณไปคุมได้ ต่อมาตั้ง baud rate ของ Serial port ให้เป็น 57600 การตั้ง baud rate ตรงนี้ทำเพื่อให้ใช้กับ <a href="http://processing.org">Processing</a> ภายหลัง ปกติ Arduino มี Serial communication ในตัว เอาไว้ติดต่อกับ PC ผ่าน USB ได้ มี Serial.read(), Serial.write() เอาไว้รับ input และส่ง output ได้ การติดต่อจาก PC ก็แค่เปิด terminal (หรือกด Ctrl+Shift+M เพื่อเปิด serial monitor ของ Arduino IDE ก็ได้) ไปที่ device ของ Arduino แล้วสิ่งที่พิมพ์จะเข้าไปที่ Serial.read() เอง ในโปรเจคนี้เดี๋ยวเราจะเขียนโปรแกรมใน Processing ด้วยเพื่อให้ Processing ส่งพิกัด mouse แล้วให้ Arduino ทำ Serial.read() แล้วแปลงพิกัด mouse เป็น สัญญาณ pulse คุม servo อีกที

ที่ loop() เราอ่าน input เป็นบรรทัดไปเรื่อยๆ (เพราะเดี๋ยวเราจะทำให้ Processing ส่งพิกัด "x y" ทีละบรรทัด) ถ้าเจอบรรทัดก็ให้แกะพิกัดออกมาด้วย sscanf() แล้วแปลงพิกัดเป็นความยาว pulse พิกัด x แปลงเป็น pulse คุม servo ตัวที่ 1 พิกัด y แปลงเป็น pulse คุม servo ตัวที่ 2 ถ้าไม่มี input จาก Serial port ก็ไม่ต้องทำอะไร
<ul>
	<li>ตัวแปร coarseness เป็นตัวแปรกำหนดความหยาบของพิกัด คือที่ตั้งเป็น 2 แปลว่าจะหัน servo เมื่อ x หรือ y หาร 2 ลงตัวเท่านั้น ทำไปเพื่อไม่ให้ servo สั่นเกินไปเวลาเลื่อน mouse ถ้า coarseness เป็น 1 (คือเหมือนไม่มี coarseness นั่นแหละ) มันจะสั่นมากเวลาเลื่อน mouse แค่นิดเดียว</li>
	<li>preciseServo() เอาไว้คุม servo สองตัวด้วยค่า 0 ถึง 1 (เข้าใจง่ายดี)</li>
	<li>driveServo() เป็น function เอาไว้สั่งการ servo ด้วย pulse จริงๆ จะเห็นว่ามีการทำให้ pin เป็น HIGH ด้วย digitalWrite() แล้วทำ delayMicroseconds() เพื่อหยุดไว้แป็ปเดียว (ขึ้นอยู่กับความยาว pulse ที่อยากได้) แล้วค่อยทำให้ pin เป็น LOW</li>
</ul>
ด้วย code ที่มีอยู่นี้ หลังจาก upload แล้ว ให้ลองเปิด serial monitor ด้วย Ctrl+Shift+M ตั้งค่า baud rate ให้เป็น 57600 ด้วย แล้วลองพิมพ์ "100 100"  กด enter แล้ว servo 2 ตัวจะต้องหันทวนเข็มทั้งสองตัว
<h3>เขียนโปรแกรม Processing เพื่อส่งพิกัด mouse ไปให้ Arduino</h3>
Processing เป็นภาษาคล้ายๆ Java สำหรับเขียนโปรแกรม graphics แบบ interaction โดยเฉพาะ มี library หลากหลาย หนึ่งในนั้นมี library Serial เพื่อติดต่อกับอุปกรณ์ผ่าน serial port ได้ด้วย จริงๆแล้ว Processing มี library ชื่อ Firmata ด้วยเพื่อติดต่อกับ Arduino โดยเฉพาะ แต่ลงแล้วใช้งานไม่ได้ และไม่ค่อยเข้าใจด้วยว่าทำไปทำไม ตอนนี้ใช้แค่ Serial ก็เพียงพอแล้ว

ต่อไปนี้เป็น code Processing เพื่อส่งพิกัด mouse ไปที่ input Serial port ทุกครั้งที่ mouse เลื่อน

[code language="java"]
import processing.serial.*;
import cc.arduino.*;

Serial arduino;
int ledPin = 13;
int X=0,Y=0;

void setup(){

  println(Arduino.list());
  arduino = new Serial(this, Serial.list()[0], 57600);

  // graphics setup
  size(800, 600);

}

void draw()
{
//  if (mousePressed){
    if( !(X==mouseX &amp;&amp; Y==mouseY) ){
      X = mouseX;
      Y = mouseY;
      println(X+&quot; , &quot;+Y);
      arduino.write(X+&quot; &quot;+Y+&quot;\n&quot;);
      delay(10);
    }

//  }

}
[/code]

ใน Processing มี 2 function หลัก คล้ายๆ Arduino คือ setup() กับ draw() ทำงานเหมือนกับ setup() กับ loop() ของ Arduino เลย จาก code ที่ setup() เราสร้าง object  Serial ขึ้นมาโดยเลือก ตัวแรกจาก list และตั้ง baud rate ให้ถูกต้องเหมือนที่ตั้งใน Arduino คำสั่ง size(800,600) เอาไว้กำหนดขนาดหน้าต่าง 800,600 ค่านี้ตรงกับตัวแปร screenW, screenH ที่ตั้งไว้ใน Arduino

ที่ draw() เราก็แค่เช็คว่าถ้า X,Y มีการเปลี่ยนแปลง ให้ write() ไปที่ object Serial ที่เราสร้างขึ้น โดยเราเขียนให้เป็น format เดียวกับที่เราใช้ sscanf() ใน code ของ Arduino เพื่อให้มันคุยกันรู้เรื่อง

ถึงตอนนี้ถ้าลอง run Processing แล้วเลื่อน mouse พิกัดของ mouse ก็จะถูกส่งไปที่ Arduino และ servo ก็จะหมุนตาม mouse แบบในวิดีโอ
<p style="text-align: center;"><a href="http://wittawat.com/blog/?attachment_id=1166" rel="attachment wp-att-1166"><img class="aligncenter  wp-image-1166" title="Arduino + Processing to control 2 servos" src="http://wittawat.com/blog/wp-content/uploads/2012/10/arduino_servos-680x1024.jpg" alt="" width="354" height="533" /></a></p>
หมายเหตุ: พยายามเอา laser pointer มาติดที่แขนสีส้มด้วย เอาถ่านออกเพราะหนัก บัดกรีเชื่อมออกมาต่อถ่านข้างนอกได้แล้ว แต่ตอนยึดมันไม่แข็งแรง ยังไม่ได้ทำต่อ เลิกซะก่อน
