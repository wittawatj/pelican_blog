Title: ncftp: FTP Client with Recursive Transfers 
Date: 2010-06-05 08:06:20
Tags: ftp, ubuntu 
Slug: ncftp: FTP Client with Recursive Transfers 


[ad#afterpost]

I have searched for a FTP client with recursive transfers for a while. By recursive transfers, I mean transfering the whole directory at once. For many GUI clients, this feature is quite common. What I mean here is a FTP command-line client. FTP command-line clients rarely provide such feature. A good client I have come across which can do that is <strong>ncftp</strong> . If you use Ubuntu, you can get it by

[bash]sudo apt-get install ncftp[/bash]

You can start ncftp with

[bash]ncftp -u &lt;your_ftp_user&gt; -p &lt;your_ftp_password&gt; &lt;yourhostname.here.com&gt; [/bash]

After you are in the ncftp interface, normal FTP commands work here. To transfer the whole folder, use

[bash]mget -R folder_name [/bash]

If you need more information, issue the command

[bash]help[/bash]

to see all available commands.
