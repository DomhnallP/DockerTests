# Docker Tast Queue Cluster Project

This is a simple task queue cluster that runs in docker. this is a quickstart guide, feel free to clone or fork this repo and mess around with it

## Table of Contents

- [Installation](#installation)
- [Usage](#running)
- [Support](#support)
- [Contributing](#future)

## Installation

### Clone the git repo
git clone https://github.com/DomhnallP/DockerTests.git

###Set Up A Redis Server
 -  Make sure you update the value REDIS_HOST in tasks.py to represent the new IP address

###Installing the task runner on your server nodes:
For Each Node: 
 -  Make sure you have docker installed
 -  run the command: docker pull domhnallp/redisworker:latest
 -  Run: docker start domhnallp/redisworker
 -  your node should now be ready to take requests!

####Notes: 
 -  If you are using aws ec2 instances (like I did for testing), you must use sudo to run your docker commands.  

## Running the tasks
 -  Run the python file redisConnect.py to test the cluster.
 -  if you check the console of each node, you should see outputs from the tasks being processed.

## Support

Please [open an issue](https://github.com/DomhnallP/DockerTests/issues/new) for support.

## Future Work

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).