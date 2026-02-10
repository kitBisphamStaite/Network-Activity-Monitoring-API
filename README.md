# Network Activity Monitoring API

## Overview

The Network Activity Monitoring API is a Python-based RESTful service designed to simulate the collection, analysis, and detection of anomalous network activity. The project demonstrates core backend engineering concepts, including API design, data validation, networking fundamentals, and behavioural analysis.

The application models network-connected devices generating traffic events and provides analytical endpoints to surface statistics and suspicious behaviour. This project was developed as a technical preparation exercise aligned with real-world cybersecurity use cases.

---

## Key Features

### Device Management

- Register new devices with hostname and IP address  
- Retrieve all registered devices  
- Retrieve individual device details by ID  

Each device includes:

- Unique identifier  
- Hostname  
- IP address  
- Creation timestamp  

---

### Network Event Collection

- Ingest network traffic events associated with devices  
- Filter events by device  
- Validate destination IP addresses and ports  
- Automatically determine whether destination IPs are private or public  

Each event records:

- Event ID  
- Device ID  
- Destination IP  
- Destination port  
- Bytes sent  
- Timestamp  

---

### Analytics & Statistics

The API provides aggregated insights including:

- Total connections  
- Total bytes transferred  
- Average bytes per event  
- Most frequently used destination ports  
- Per-device statistics  

---

### Anomaly Detection

The system identifies potentially suspicious behaviour using rule-based heuristics:

- High-volume transfers (greater than 1MB)  
- Connections to uncommon ports (outside 80, 443, and 22)  
- Burst activity (more than 10 events from a single device within 60 seconds)  

Detected anomalies are exposed via a dedicated endpoint.

---

### Networking Capabilities

- IP address validation using Python’s `ipaddress` module  
- Public vs private IP classification  
- CIDR subnet matching  
- Burst detection using sliding time windows  

---

## Technology Stack

- Python 3.10+  
- FastAPI  
- Pydantic  
- Requests  
- Pytest (optional)  
- Docker (optional)  

---

## Project Structure

app/   
├── main.py # Application entry point  
├── models.py # Pydantic models  
├── routes.py # API endpoints  
├── analytics.py # Statistical and anomaly logic  
└── utils.py # IP validation and helpers  

tests/ # Unit tests  
Dockerfile  
requirements.txt  
README.md  


---

## API Endpoints

### Devices
POST /devices  
GET /devices  
GET /devices/{device_id}  

---

### Network Events

POST /events  
GET /events  
GET /events?device_id={id} 


---

### Statistics

GET /stats  
GET /stats/{device_id}  

---

### Anomalies

GET /anomalies  

---

## Example Analytical Functions

The project includes standalone analytical utilities:

- Identify the top data-consuming device  
- Calculate most common destination ports  
- Detect traffic bursts  
- Filter events by CIDR subnet  

These functions demonstrate data aggregation, grouping, and time-series reasoning.

---

## Optional Enhancements

- Dockerised deployment  
- External GeoIP lookups  
- Unit test coverage  
- Persistent storage  
- Authentication and rate limiting  

---

## Future Improvements

- Replace in-memory storage with PostgreSQL  
- Introduce async background processing  
- Implement authentication (JWT)  
- Add metrics via Prometheus  
- Integrate ML-based anomaly detection  
- Improve scalability with message queues  

---

## Learning Objectives

This project demonstrates:

- REST API design principles  
- Production-style Python structure  
- Data validation and error handling  
- Networking fundamentals  
- Behavioural anomaly detection  
- Analytical problem-solving  
- Dockerisation  
- Test-driven development  

---

## Author

Kit Bispham

