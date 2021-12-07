# API endpoints for UDP 

<i> "POST" request to https://cislunar-data.herokuapp.com/addData</i> 
- Required request data: json dictionary of all database fields and corresponding Float convertible values.
- Returns: json dictionary of the newly stored data

<i> "GET" request to https://cislunar-data.herokuapp.com/getData</i> 
- Required request data: none
- Returns: json dictionary of all stored data

<i> "DELETE" request to https://cislunar-data.herokuapp.com/deleteALLData</i> 
- Required request data: none
- Returns: json string message describing completed action


# API endpoints for Grafana
The behavior of the following datapoints (required/returns) were implemented to follow the behavior as specified by the <a href = "https://grafana.com/grafana/plugins/grafana-simple-json-datasource/">Grafana SimpleJson plugin</a>.

<i> "GET" request to https://cislunar-data.herokuapp.com/</i> 
- for testing connection
<i> "POST" request to https://cislunar-data.herokuapp.com/search</i>
- returns names of the data fields available to be queried/displayed 
<i> "POST" request to https://cislunar-data.herokuapp.com/query</i> 
- returns data, format depends on grafana's request data
