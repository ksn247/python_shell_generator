#!/bin/bash
remote_host=remote_node_name
source_file=/opt/test/file3.txt
dest_file=new_file3.txt

ndmcli -x <<-EOJ
submit maxdelay=unlimited
procname123
process
pacct="C:D test"
snode=$remote_host

step01
copy from (file = $source_file)
compress = extended
to (file = $dest_file
snode
disp = new)
pend;
EOJ