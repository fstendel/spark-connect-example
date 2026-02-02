This project starts a spark cluster setup consisting of:

* 1 Spark Master Node
* 1 Spark Worker Node
* 1 Spark Connect Node

using docker compose.

The compose file can be run using `docker compose up -d`.


UIs are exposed via the ports outlined in the docker-compose file. 
Currently, the setup doesn't have any proxy settings configured hence the links in those 
UIs won't work (as they use the internal container host names).

An example python script is provided alongside the compose-file. 
The script prints out a range of numbers and writes it to a folder within the spark cluster. 

If you want to see the files contents either login into one of the containers 
or mount the data-volume in the compose file to a folder on your local machine.

