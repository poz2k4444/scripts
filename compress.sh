#!/bin/bash

#Let me eaxplain a little what we have
#First of all we check for the processors in the box

CORES=$(grep -c '^processor' /proc/cpuinfo)


#As we are copying files from root we need to be superuser
if [[ "$(whoami)" == 'root' ]]
   then
   echo "you have $CORES cores, we'll use all of them, just don't panic please"
   echo "Gziping files..."
   #As you said, we need to let the server attend petitions, so we let the nice value high in order to use all the processors power when it's not been used for other instance, we check por all the files matching and gzip them with the maximum compression possible, the xargs allow us to use multi cores with the -P argument, and the -n allows us decide how many jobs per process will be done.
   nice -19 find /var/log/apache2/ -iname "apache*.log" -print0 | xargs -0 -n 1 -P $CORES gzip -9
   echo "All files gziped... Let's send this..."
   #Again we let the process be nice with the other ones and send all files, using all the cores, to the destination folder 
   nice -19 find /var/log/apache2/ -iname "*.gz" -print0 | xargs -0 -n 1 -P $CORES -I {} scp {} user@xxx.xxx.xxx.xxx:/path/to/folder
   echo "All files copied babe!... have a nice day!!"
   else
   echo "You are not running this as sudo!  D= "
   exit
fi
exit

