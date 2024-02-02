# Official image of ROS humble version
FROM ros:humble-ros-base

# install colcon 
RUN apt update && apt install -y python3-colcon-common-extensions && apt install -y libssl-dev && apt install -y tree

# For tests
RUN apt install -y vim python3-pip
RUN pip install --upgrade pip && pip install pynguin

# create the /home/ros folder
RUN mkdir -p /home/ros/vehicle/src && mkdir /var/log/ros 
RUN chmod -R g+w /home/ros/vehicle/src && chmod -R g+w /var/log/ros 

# copy the "vehicle.py" python program from the repository to the "/home/ros" folder
ADD src /home/ros/vehicle/src

RUN echo cd /home/ros/vehicle/src > launch.sh && \
echo source /opt/ros/humble/setup.bash >> launch.sh && \
echo colcon build >> launch.sh && \
echo source install/local_setup.bash >> launch.sh && \
echo cd / >> launch.sh && \
# fix bug in ROS: https://github.com/ros2/rclpy/pull/1178
echo 'sed -i '\''243s/.*/        if hasattr(self, "_sigint_gc") and self._sigint_gc is not None:/'\'' /opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py' >> launch.sh &&  \
echo ros2 run vehicle_pkg vehicle --ros-args --enclave /mut4sec/vehicle >> launch.sh && \
chmod +x launch.sh

ENTRYPOINT ["/bin/bash", "/launch.sh"]
