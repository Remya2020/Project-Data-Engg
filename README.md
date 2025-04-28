Stock Analysis and Visualization with OpenSearch

Project Overview

This project performs real-time stock analysis by fetching stock market data using Python and Yahoo Finance.
The program analyzes selected stocks, determines their trend (bullish or bearish), and stores the results in an OpenSearch dashboard.
Both the analysis application and OpenSearch are containerized using Docker for easy deployment.

Technologies Used
•	Python
•	yFinance (Yahoo Finance API)
•	OpenSearch (for data storage and visualization)
•	Docker (for containerization)
•	OpenSearch Dashboards

How to Run the Project
1.	Clone the repository:
2.	git clone <your-repository-url>
3.	cd <your-project-folder>
4.	Set up OpenSearch and OpenSearch Dashboard:

o	Use Docker Compose or separate Docker containers.

o	Default credentials used:
Username: admin
Password: admin
o	OpenSearch runs on port 9200.

5.	Set up Python environment:
o	Install required libraries:
o	pip install yfinance opensearch-py
o	Run the Python script:
o	python stock_analysis.py

6.	View Results:
o	Open OpenSearch Dashboard in your browser.
o	Connect to your OpenSearch instance.
o	Visualize the "us_stock" index data for stock trends.
Screenshots
![image](https://github.com/user-attachments/assets/3b236aff-3d66-4c00-bc32-73c81a7da93a)
Features
•	Fetches weekly historical stock data.
•	Analyzes stock trends (bullish or bearish).
•	Sends real-time data to OpenSearch index.
•	100% Dockerized: Easy to deploy and scale.

License
This project is licensed under the MIT License. Feel free to use and modify it!



