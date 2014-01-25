#!/bin/bash


#IP=nukevps
IP=wittawat.com

#rsync  -e ssh -zavc --modify-window=2 --exclude=".svn" --exclude-from="/nfs/home1/wittawat/script/exclude_upresearchblog.txt" --delete --progress /nfs/home1/wittawat/SHARE/blog/hakyll_blog/_site/ nuke@${IP}:/home/nuke/public_html/

rsync  -e ssh -zav --modify-window=2 --exclude=".git"  --progress output/  nuke@${IP}:/home/nuke/public_html/


