# Takehome 2019 in OPN

**Submission date: 22nd of December.**

## Requirements
1. Proxy
- Proxy must communicate with the Actor over https, meaning nginx should terminate the TLS connection.
- Proxy must serve two html files which are provided in the GitHub repository:
    - insert.html
    - select.html 
Proxy must proxy POST /person/ and GET /persons/ to backend
2. Backend
- Backend must interact with database. How, is for you to decide and you can use whatever programming language to setup the web server, but we can only guarantee to be able to help with Python Flask servers.
- Backend should serve two API endpoints:
    - POST /person/
     - /person/ must take input from the insert.html form (See Figure 1)
    - GET /persons/
     - /persons/ must return the result from the database in JSON. (See Listing 1)
3. Database
- Database should be a mysql-container
- Database should have one table that contains three columns: An automatically incremented integer called 'PersonID' and two text fields called 'Firstname' and 'Lastname'.
4. Network
- The network between the containers must be split into two seperate networks, making it impossible for the proxy to interact directly with the database. This means that the proxy and the backend are the only containers on network1, and the backend and the database the only containers on network2
The complete introduction can be found at: https://docs.google.com/document/d/1MYMciztUZKMkXKEGh9hFGQUNrJFwxmSQOrz9tfpFqw0/

