# AI-Powered Fraud Detection System

This project is an AI-powered fraud detection system that uses machine learning to identify and prevent fraudulent transactions. The system is built with Django and uses a variety of machine learning models to analyze transaction data and identify suspicious activity. The system also includes a web-based interface for managing fraud cases and a REST API for integrating with other applications.

## Key Features

*   Real-time fraud detection
*   Machine learning-based fraud scoring
*   Web-based interface for managing fraud cases
*   REST API for integrating with other applications
*   Support for multiple machine learning models (XGBoost, LightGBM, CatBoost)
*   Scalable and extensible architecture

## Technologies Used

*   **Backend:** Django, Django REST Framework, Celery, Redis
*   **Frontend:** Streamlit
*   **Database:** PostgreSQL
*   **Machine Learning:** Pandas, NumPy, Scikit-learn, XGBoost, LightGBM, CatBoost
*   **Containerization:** Docker

## Getting Started

To get the project up and running on your local machine, you will need to have Docker and Docker Compose installed. Once you have installed Docker and Docker Compose, you can follow these steps:

1.  Clone the repository:
    ```
    git clone https://github.com/your-username/ai-powered-fraud-detection.git
    ```
2.  Create a `.env` file in the root of the project and add the following environment variables:
    ```
    DATABASE_NAME=fraud_detection
    DATABASE_USER=fraud_detection
    DATABASE_PASSWORD=fraud_detection
    ```
3.  Build and run the Docker containers:
    ```
    docker-compose up -d
    ```
4.  The application will be available at `http://localhost:8000`.

## Usage

Once the application is running, you can access the web interface at `http://localhost:8000`. The web interface allows you to view and manage fraud cases. You can also use the REST API to integrate the fraud detection system with other applications. The API documentation is available at `http://localhost:8000/api/docs/`.

## Contributing

Contributions to the project are welcome. To contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your changes and commit them to your branch.
4.  Push your changes to your forked repository.
5.  Create a pull request to the main repository.
