# Data Pipeline Overview
<p align="center">
  <img src="/media/frame.png" width="750" title="hover text" alt="data pipeline schematic here">
</p>

This repository concerns the Django(server) step of the pipeline. The Django server provides an API over the embedded SQLite database. This handles all requests related to storing and retrieving data. This is an independent system (does not require any other steps in the data pipeline to be running concurrently).

For information on the UDP client step, view: https://github.com/Cislunar-Explorers/FlightSoftware/tree/master/udp_client

For information on the UDP server step, view: https://github.com/Cislunar-Explorers/GroundSoftware/tree/main/UDP_groundstation

For information on the Grafana step, view: (doc coming soon)

# Additional Documentation:
- <a href = "">API endpoints</a>
- <a href = "">Additions to the data pipeline<a/>

# Set Up Instructions
run the following in the base directory
```
sh setup.sh
```
if there are errors running the bash script, run each command in sh setup.sh manually 

# Run Instructions
run the following in the base directory
```
sh run.sh
```
if there are errors running the bash script, run each command in sh setup.sh manually 
