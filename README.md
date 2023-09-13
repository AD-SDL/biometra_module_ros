# biometra_module

Github repository for ROS Packages related to the Biometra TRobot II

## biometra_client

A ROS2 wrapper that accepts service calls from the wei_client in order to call certain functions on the thermocycler

Start biometra node:

`ros2 launch biometra_client biometra_client.launch.py`

Accepted commands:
- `open_lid`
- `close_lid`
- `run_program`
- `get_status`

## Running
The following are step by step instructions for activating the biometra ROS2 node and running a protocol

- `ssh rpl@parker`
- navigate to `~/wei_ws`
- `ros2 launch biometra_client biometra_client.launch.py`
- wait to ensure biometra node is broadcasting "READY" state
- switch back to local computern (sched)
- navigate to `~/home/workspace/`
- `source /opt/ros/humble/setup.bash`
- `source ~/wei_ws/install/setup.bash`
- `./` + path to your wei client

## Troubleshooting

### biometra is saying the lid is open when it is not and vice versa
- power cycle the biometra

