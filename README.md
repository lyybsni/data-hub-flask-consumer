### Data Hub Flask Visualization Service
This project aims to aid in visualization in `applicant` domain for `data-hub-demo` project.

#### Project Structure
```text
Flask Framework - for web service core
Spark - for datasource processing
MongoDB Connector - for datasource linking
```

##### Configuration
For the current trail, the compromised version of low version PySpark has been installed.

| ITEM                  | VERSION             |
|-----------------------|---------------------|
| Python                | 3.12                |
| PySpark               | 3.1.1               |
| Mongo Spark Connector | 2.4.0               | 
| Scala                 | 2.1.2               |
| Mongo Driver          | 3.8.1               |
| Mongo Driver Core     | 3.8.1               |
| BSON                  | 3.8.1               | 
| Java                  | 11 (Zulu Community) |

#### Functionality
- [x] Update Based on Polling
- [ ] Update Based on Streaming (Will be put in experimental branch)
- [ ] Update Based on Messaging