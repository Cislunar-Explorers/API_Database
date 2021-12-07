# About
This repository contains the API step of the data pipeline (view Data Pipeline Overview diagram below). The API receives requests from the UDP Client and Grafana and interfaces with the PostgreSQL database to store and retrieve data.

The API follows the Django REST framework format. Both the database and API are currently deployed on Heroku. The deployment process for Heroku is connected directly to this repository; any changes to the master branch will trigger redeployment.

## Data Pipeline Overview
<p align="center">
  <img src="/media/frame.png" width="750" title="hover text" alt="data pipeline schematic here">
</p>

Information on other steps can be found below: 
- <a href = "https://github.com/Cislunar-Explorers/FlightSoftware/tree/master/udp_client"> UDP Client </a>
- <a href = "https://github.com/Cislunar-Explorers/GroundSoftware/tree/main/UDP_groundstation"> UDP Server </a>
- <a href = "https://www.google.com/search?q=grafana"> Grafana (doc coming soon) </a>

# Additional documentation for current repository
- <a href = "">Set up and run locally</a>
- <a href = "">API endpoints</a>
- <a href = "">Process for adding to the data pipeline</a>
- <a href = "">Testing<a/>

# Other helpful resources: official documentation
- <a href= "https://www.django-rest-framework.org/"> Django REST framework </a>
- <a href="https://devcenter.heroku.com/categories/working-with-django"> Working with Django on heroku </a>

# Contact
- <a href = "kn294@cornell.edu"> Ka-Hyun Nam </a>


