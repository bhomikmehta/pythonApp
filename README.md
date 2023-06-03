## pythonApp
This is a dummy app built with Docker compose, Python, Flask, MySQL, Telegraf and InfluxDB for learning

The given Docker Compose file sets up a containerized environment for running a MySQL database, a Python web application, and an InfluxDB storage for metrics. Here's a summary of the configuration:

Services: The Docker Compose file defines three services: db, web, and influxdb.

# MySQL Service (db):
NOTE - This image takes some time to be available fully. 
Image: MySQL Debian version.
Build: The MySQL service is built using a custom Dockerfile located at ./mysql/dockerfile.mysql.
Container Name: mysql.
Restart Policy: The container always restarts if it stops.
Environment Variables: The MySQL service is configured with environment variables specifying the database name, user credentials, and root password.
Ports: The MySQL service is accessible on host ports 3306 and 8125.
Networks: The service is connected to a network named app_network.
Web Service (web):

# Image: Python 3.9.
Build: The web service is built using a custom Dockerfile located at ./app/dockerfile.app.
Container Name: web.
Restart Policy: The container always restarts if it stops.
Ports: The web service is accessible on host ports 5000 and 443.
Environment Variables: The web service is configured with environment variables specifying the Flask application, environment, and MySQL connection details.
Depends On: The web service depends on the db service to be running.
Networks: The service is connected to the app_network.
InfluxDB Service (influxdb):

# Image: InfluxDB version 1.8.
Container Name: storage.
Restart Policy: The container always restarts if it stops.
Ports: The InfluxDB service is accessible on host port 8086.
Environment Variables: The InfluxDB service is configured with environment variables specifying the database name, admin user credentials, regular user credentials, and their passwords.
Networks: The service is connected to the app_network.
Depends On: The InfluxDB service depends on the web service to be running.
Networks: The Docker Compose file defines a network named app_network with the bridge driver.
