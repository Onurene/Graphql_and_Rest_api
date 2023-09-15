# Graphql_and_Rest_api

Pre requisites:
1. Setup the sample database 

https://www.sqlitetutorial.net/sqlite-sample-database/
wget https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip
unzip chinook.zip
sudo apt install --yes sqlite3
sqlite3 chinook.db .dump

2. Start the Graphql API server 
tuql --db chinook.db --graphiql

3. Start the Rest API server 
soul --database chinook.db --studio 

4. Make API calls from Python to retrieve following information

1. Albums by the artist "Red Hot Chili Peppers"
2. Genres associated with the artist "U2"
3. Names of tracks on the playlist "Grunge" and their associated artists and albums.


