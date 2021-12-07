# API endpoints for UDP 

### "POST" request to https://cislunar-data.herokuapp.com/addData
- Required request data: json dictionary of all database fields and corresponding Float convertible values.
- Returns: json dictionary of the newly stored data

### "GET" request to https://cislunar-data.herokuapp.com/getData
- Required request data: none
- Returns: json dictionary of all stored data

### "DELETE" request to https://cislunar-data.herokuapp.com/deleteALLData
- Required request data: none
- Returns: json string message describing completed action


# API endpoints for Grafana
The behavior of the following datapoints were implemented to follow the behavior as specified by the <a href = "https://grafana.com/grafana/plugins/grafana-simple-json-datasource/">Grafana SimpleJson plugin</a>.

### "GET" request to https://cislunar-data.herokuapp.com/
### "POST" request to https://cislunar-data.herokuapp.com/search
### "POST" request to https://cislunar-data.herokuapp.com/query
