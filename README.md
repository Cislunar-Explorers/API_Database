# About
This repository contains the API step of the data pipeline (view Data Pipeline Overview diagram below). This is an API for a SQL database. The API follows the Django REST framework format. Both the database and API are currently deployed on Heroku. The deployment process for Heroku is connected directly to this repository; any changes to the master branch will trigger redeployment. 

## Data Pipeline Overview
<p align="center">
  <img src="/media/frame.png" width="750" title="hover text" alt="data pipeline schematic here">
</p>

Information on other steps can be found below: 
- <a href = "https://github.com/Cislunar-Explorers/FlightSoftware/tree/master/udp_client"> UDP Client </a>
- <a href = "https://github.com/Cislunar-Explorers/GroundSoftware/tree/main/UDP_groundstation"> UDP Server </a>
- <a href = "https://www.google.com/search?q=grafana"> Grafana (doc coming soon) </a>

# Additional Documentation for current repository/API:
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
