# API endpoints for UDP 

<u> "POST" request to https://cislunar-data.herokuapp.com/addData</u> 
- Required request data: json dictionary of all database fields and corresponding Float convertible values.
- Returns: json dictionary of the newly stored data

<u> "GET" request to https://cislunar-data.herokuapp.com/getData</u> 
- Required request data: none
- Returns: json dictionary of all stored data

<u> "DELETE" request to https://cislunar-data.herokuapp.com/deleteALLData</u> 
- Required request data: none
- Returns: json string message describing completed action


# API endpoints for Grafana
The behavior of the following datapoints were implemented to follow the behavior as specified by the <a href = "https://grafana.com/grafana/plugins/grafana-simple-json-datasource/">Grafana SimpleJson plugin</a>.

<u> "GET" request to https://cislunar-data.herokuapp.com/</u> 
<u> "POST" request to https://cislunar-data.herokuapp.com/search</u> 
<u> "POST" request to https://cislunar-data.herokuapp.com/query</u> 
