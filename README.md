# PoC Pynguin - ROS

This proof of concepts aims at generating tests using [Pynguin](https://github.com/se2p/pynguin) on a [ROS2](https://docs.ros.org/en/rolling/index.html) system.

## Usage

Install Docker: https://docs.docker.com/get-docker/

Grab this repository, then build and launch the sample listener/talker stack.  

```bash
git clone git@github.com:cetic/pynguin_ros_poc.git
docker-compose build
docker-compose up
```

This will launch a ROS node, here it is a simple robot that is listening to a topic for instructions.

In another shell session, enter the container, run the following commands to prepare the environment and run the test generation:

```bash
# connect to vehicle container
docker exec -it vehicle /bin/bash

# activate ROS
source /opt/ros/humble/setup.bash

# prepare Pynguin
export PYNGUIN_DANGER_AWARE=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1

# run Pynguin on the vehicle package, need to ctrl+c at the end to finish the generation.
pynguin   --project-path /home/ros/vehicle/src/vehicle_pkg/   --output-path ./pynguin-testgen --create-coverage-report True   --module-name vehicle -v
```
