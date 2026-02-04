This project starts a spark cluster setup consisting of:

* 1 Spark Master Node
* 1 Spark Worker Node
* 1 Spark Connect Node

using docker compose.

The compose file can be run using `docker compose up -d`.
If you want to run it with more than one worker node, you can alternatively use `docker compose up -d --scale spark-worker=4` to
run with up to 4 worker nodes.


UIs are exposed via the ports outlined in the docker-compose file. 
Currently, the setup doesn't have any proxy settings configured hence the links in those 
UIs won't work (as they use the internal container host names).

An example python script is provided alongside the compose-file. 
The script prints out a range of numbers and writes it to a folder within the spark cluster. 

If you want to see the files contents either login into one of the containers 
or mount the data-volume in the compose file to a folder on your local machine.

