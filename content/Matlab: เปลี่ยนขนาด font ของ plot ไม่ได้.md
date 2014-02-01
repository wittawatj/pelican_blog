Title: Matlab: เปลี่ยนขนาด font ของ plot ไม่ได้ 
Date: 2012-05-24 10:39:10
Tags: matlab, ubuntu 
Slug: Matlab: เปลี่ยนขนาด font ของ plot ไม่ได้ 


มีปัญหาไม่ทราบสาเหตุคือ เปลี่ยนขนาดของ font ตรง axis ของ plot ไม่ได้ รวมทั้งเปลี่ยน font ก็ไม่ได้ ไม่ได้ทั้งการใช้ GUI figure editor และการใช้ code อย่าง [matlab]set(gca, 'FontSize', 30)[/matlab]

หาแล้วได้ความว่าให้ลง package 2 อัน [bash] sudo apt-get install xfonts-100dpi xfonts-75dpi[/bash]

แล้ว logout แล้วเข้าใหม่

ที่มา
<ul>
	<li><a href="http://www.mathworks.nl/matlabcentral/newsreader/view_thread/301184">http://www.mathworks.nl/matlabcentral/newsreader/view_thread/301184</a></li>
</ul>
