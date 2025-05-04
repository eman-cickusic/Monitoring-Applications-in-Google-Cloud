# Monitoring Applications in Google Cloud

This repository demonstrates how to deploy an application to Google Cloud and use Google Cloud tools to monitor it. The project implements a simple Python Flask application with Google Cloud Profiler integration and shows how to use Cloud Logging, Trace, Profiler, dashboards, uptime checks, and alerting policies.

## Overview

This project covers:
- Deploying a Python Flask application to App Engine
- Integrating Google Cloud Profiler
- Examining Cloud logs
- Using Cloud Trace for request tracking
- Creating monitoring dashboards
- Setting up uptime checks and alerts

## Video Demonstration

A video demonstration of this project is available at (https://www.youtube.com/watch?v=sX4DrgOAE34)


## Project Structure

```
.
├── README.md          # This file
├── main.py            # Python Flask application
├── requirements.txt   # Dependencies
├── app.yaml           # App Engine configuration
├── Dockerfile         # Docker configuration
└── screenshots/       # Screenshots of the monitoring setup (not available - replaced with video)
```

## Prerequisites

- Google Cloud account
- Google Cloud SDK (gcloud)
- Docker (for local testing)

## Setup and Deployment Steps

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/gcp-monitoring-app.git
cd gcp-monitoring-app
```

### 2. Enable the Profiler API

```bash
gcloud services enable cloudprofiler.googleapis.com
```

### 3. Local Testing

Build and run the Docker container:

```bash
docker build -t test-python .
docker run --rm -p 8080:8080 test-python
```

Access the application at http://localhost:8080

### 4. Deploy to App Engine

Create an App Engine application (one-time setup):

```bash
gcloud app create --region=REGION
```

Deploy the application:

```bash
gcloud app deploy --version=one --quiet
```

Access your deployed application at https://PROJECT_ID.appspot.com

## Monitoring the Application

### Cloud Logging

View logs by navigating to App Engine > Versions > Logs in the Google Cloud Console.

### Cloud Profiler

Access Profiler by searching for "Profiler" in the Google Cloud Console. It provides visualization of CPU usage by function.

### Cloud Trace

Access Trace Explorer by searching for "Trace Explorer" in the Google Cloud Console. It shows request history and latency.

### Generate Test Traffic

You can generate traffic to your application using Apache Bench:

```bash
sudo apt update
sudo apt install apache2-utils -y
ab -n 1000 -c 10 https://PROJECT_ID.appspot.com/
```

### Monitoring Dashboards

Access pre-built dashboards for App Engine and VM instances in the Monitoring section of the Google Cloud Console.

### Setting Up Uptime Checks and Alerts

1. Navigate to Monitoring > Uptime Checks
2. Create an uptime check for your App Engine URL
3. Configure alert policies to notify you when the application is unavailable
