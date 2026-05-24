# Real-Time News Sentiment Analysis Pipeline on AWS

## Project Overview

This project is a cloud-based real-time news sentiment analysis pipeline built using AWS services, PostgreSQL, Docker, and Streamlit.

The system fetches live news articles from the News API, performs sentiment analysis on the articles, stores the processed data in an Aurora PostgreSQL database, and visualizes the results through a Streamlit dashboard deployed on AWS ECS Fargate.

---

# Features

- Real-time news data ingestion
- Sentiment analysis using VADER
- Automated AWS Lambda pipeline
- Event-driven scheduling with EventBridge
- Aurora PostgreSQL database integration
- Interactive Streamlit dashboard
- Dockerized application
- Cloud deployment using Amazon ECS Fargate
- Fully scalable cloud architecture

---

# Architecture

```text
News API
   ↓
AWS Lambda
   ↓
Aurora PostgreSQL
   ↓
Streamlit Dashboard
   ↓
Docker Container
   ↓
Amazon ECR
   ↓
Amazon ECS Fargate.


# Tech Stack

## Programming Languages
Python
SQL

## AWS Services
AWS Lambda
Amazon EventBridge
Amazon ECS Fargate
Amazon ECR
Amazon RDS / Aurora PostgreSQL

## Libraries & Frameworks
Streamlit
SQLAlchemy
Requests
Pandas
VADER Sentiment Analyzer
DevOps Tools
Docker
GitHub

# Folder Structure

project-root/
│
├── app/
│   └── news_pipeline.py
│
├── dashboard/
│   └── app.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

# Workflow

News articles are fetched from News API.
AWS Lambda processes incoming news data.
Sentiment analysis is performed using VADER.
Processed records are stored in Aurora PostgreSQL.
Streamlit dashboard reads data from the database.
Docker container packages the application.
Amazon ECS Fargate hosts the dashboard publicly.

#Database Schema

CREATE TABLE news_sentiment (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    sentiment_score FLOAT,
    source TEXT
);

# Setup Instructions

Clone Repository
git clone <repository-url>
cd <project-folder>

# Install Dependencies

pip install -r requirements.txt

#Run Streamlit Locally

streamlit run dashboard/app.py

#Docker Setup

## Build Docker Image
docker build -t news-dashboard .

##Run Docker Container
docker run -p 8501:8501 news-dashboard

#AWS Deployment

## Services Used
Amazon ECR for container registry
Amazon ECS Fargate for deployment
AWS Lambda for serverless processing
EventBridge for scheduling
Aurora PostgreSQL for storage

## ECS Deployment
Application deployed using AWS ECS Fargate.

## Amazon ECR
Docker image stored in Amazon ECR repository.

## Deployment Status
Application successfully deployed on AWS cloud.


#Future Improvements

Advanced NLP models using Transformers
Real-time streaming with Kafka
User authentication
Live dashboard refresh
CI/CD pipeline with GitHub Actions
Custom analytics visualizations
Project Outcome

# This project demonstrates:

Cloud-native application deployment
Real-time ETL pipeline development
Serverless architecture implementation
Data engineering workflows
Dashboard visualization
Containerized application deployment


Author: Athul T P

License
This project is developed for educational and portfolio purposes.