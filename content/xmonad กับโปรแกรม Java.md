Title: xmonad กับโปรแกรม Java 
Date: 2011-03-01 04:42:44
Tags: java, xmonad 
Slug: xmonad กับโปรแกรม Java 


ต่อจาก post แล้วเรื่อง xmonad เจอปัญหาตรงที่โดยปกติจะไม่สามารถเปิด GUI ที่เขียนโดย Java ได้ พอรันโปรแกรม Java แล้วจะเห็นแต่หน้าต่างโล่งๆไม่มีอะไร วิธีแก้มีเขียนไว้ในเว็บอ้างอิงด้านล่างแล้ว เพิ่มเติมสำหรับคนที่จะใช้ Win คีย์แทน Alt แล้วก็อยากแก้เรื่อง Java ด้วย ให้ใช้ code ต่อไปนี้ใน xmonad.hs

[code]

import XMonad
import XMonad.Config.Gnome
import XMonad.Hooks.SetWMName

main = xmonad gnomeConfig
 { modMask = mod4Mask -- Use Win instead of Alt
 , startupHook = setWMName &quot;LG3D&quot;
 }

[/code]

ที่มา
<ul>
	<li><a href="http://haskell.org/haskellwiki/Xmonad/Frequently_asked_questions#Problems_with_Java_applications.2C_Applet_java_console">http://haskell.org/haskellwiki/Xmonad/Frequently_asked_questions#Problems_with_Java_applications.2C_Applet_java_console</a></li>
</ul>
