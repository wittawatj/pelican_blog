Title: ใช้ xmonad กับ Ubuntu 10.10  
Date: 2011-02-27 04:31:17
Tags: twm, ubuntu, window, xmonad 
Slug: ใช้ xmonad กับ Ubuntu 10.10  


ใครที่ใช้จอที่ใหญ่มากๆจะเจอปัญหาเรื่องการใช้เนื้อที่จออย่างมีประสิทธิภาพ ถ้าใช้แบบทั่วๆไปจะใช้เนื้อที่จอไม่คุ้ม เช่นมีจอ 24 นิ้วแต่เอามาเปิด web browser ขยายเต็มหน้าจอ วิธีที่ดีกว่าคือควรแบ่งเป็น 2-3 ส่วนแล้ววางโปรแกรมลงแต่ละช่องแล้วดูพร้อมๆกัน เช่น web browser + editor เขียนโปรแกรม

<a href="http://askubuntu.com/questions/1844/is-there-a-keyboard-centric-desktop-wm-available">ที่นี่</a> มีรายการของ <a href="http://en.wikipedia.org/wiki/Tiling_window_manager">Tiling Window Manager</a> ที่น่าลองอยู่หลายตัวเหมือนกัน ตัวแรกที่ลองคือ Bluetile ตัวนี้ใช้ง่าย เข้ากับ Gnome ทันที จะมีแถบเมนูขึ้นมาทางซ้าย สามารถกดได้วางจะให้จัดหน้าต่างโปรแกรมแบบไหน ค่อนข้างโอเค แต่ไม่ชอบตรงที่มันมีเมนูขึ้นมาและมันแทนที่ title bar ของโปรแกรมต่างๆด้วย title bar สีฟ้าของมันเอง

xmonad เป็นอีกตัวที่ลองแล้วถูกใจ ไอเดียคือเหมือนโปรแกรม screen น่ะ หน้าจอจะถูกแบ่งอัตโนมัติเมื่อมีโปรแกรมเปิดใหม่ สามารถกำหนดได้ว่าจะแบ่งแบบไหน (ซ้าย-ขวา, บน-ล่าง) จุดที่ชอบคือ ทุกอย่างคุมได้ด้วยคีย์บอร์ด ไม่ต้องแตะ mouse เลย แต่อาจไม่เหมาะกับผู้ใช้ใหม่นะ คนที่ชอบ vi น่าจะชอบตัวนี้

ปัญหาของ xmonad คือ ถ้าใช้ xmonad โดดๆ มันจะไม่มี gnome-panel (แถบที่แสดงเมนู, นาฬิกา) อีกทั้ง resolution ของหน้าจอก็จะต่ำมาก เหมือนทำขึ้นมาใช้สำหรับโปรแกรม command line  อย่างเดียวเลย และตั้งจอแนวตั้งไม่ได้ด้วย (คงได้แต่ไม่รู้ไปแก้ที่ไหน น่าจะเรื่องยาว) วิธีหนึ่งคือ ใช้ gnome เหมือนเดิมแต่เปลี่ยน metacity ให้เป็น xmonad ด้วยคำสั่งนี้

[bash]gconftool -t string -s /desktop/gnome/session/required_components/windowmanager xmonad[/bash]

แล้วต่อด้วยการสร้าง config file ที่ ~/.xmonad/xmonad.hs แล้วใส่ code (code ภาษา Haskel) นี้ลงไป

[code]import XMonad
import XMonad.Config.Gnome

main = xmonad gnomeConfig

[/code]

แค่นี้ก็จะใช้แบบผสมได้คือ มี gnome-panel เหมือนเดิม แต่หน้าต่างจะถูกจัดให้เองตามแบบของ xmonad (ลากย้ายไม่ได้)

อีกประเด็นที่ต้องพูดถึงคือ xmonad ใช้ Alt เป็นคีย์หลักในการคุมหน้าต่าง เช่น Alt+j เพื่อไปหน้าต่างถัดไป การใช้ Alt อาจทำให้ shortcut ไปชนกับ shortcut อื่นๆ ไม่สะดวก วิธีแก้คือใช้ Win แทน (หรือปุ่ม command บน Apple keyboard) โดยการใช้ code นี้แทน code ข้างบน

[code]

import XMonad
import XMonad.Config.Gnome

main = xmonad gnomeConfig
 { modMask = mod4Mask -- Use Win instead of Alt

 }

[/code]

ที่มา:
<ul>
	<li><a href="http://haskell.org/haskellwiki/Xmonad/Using_xmonad_in_Gnome">http://haskell.org/haskellwiki/Xmonad/Using_xmonad_in_Gnome</a></li>
	<li><a href="http://ubuntuforums.org/showthread.php?t=975329">http://ubuntuforums.org/showthread.php?t=975329</a></li>
	<li><a href="http://www.huntlycameron.co.uk/wordpress/2010/11/16/how-to-set-up-xmonad-xmobar-ubuntu/">http://www.huntlycameron.co.uk/wordpress/2010/11/16/how-to-set-up-xmonad-xmobar-ubuntu/</a></li>
</ul>
