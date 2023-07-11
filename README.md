## _dbt-snowflake-airdlow-demo_

[![N|able](https://user-images.githubusercontent.com/76805373/152945012-5d715499-4498-4d8b-85c7-b5b8a6b82da9.png)](https://www.n-able.biz/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

## Introduction

This project demonstrates the use of dbt (data build tool) with Snowflake, a cloud-based data warehouse. dbt is a popular open-source tool that enables data transformation and modeling in a version-controlled and collaborative manner. This README provides a step-by-step guide to set up and use dbt with Snowflake.

## Getting Started

To get started with this project, follow the steps below:

## Prerequisites

- dbt (data build tool) installed on your local machine. You can install dbt by following the instructions at [dbt Installation Guide](https://docs.getdbt.com/dbt-cli/installation)

- Snowflake account (including credentials)
### Steps to Create a Snowflake Account

1. Go to the Snowflake website: https://www.snowflake.com/.

2. Click "Get Started" or "Try For Free."

3. Fill out the required information, including email and password.

4. Choose your preferred cloud platform (AWS, Azure, GCP).

5. Provide additional details like your name and company.

6. Accept the terms of service and privacy policy.

7. Complete any verification steps.

8. Activate your account by clicking the link in the email you receive.

9. Set up your first Snowflake instance by selecting region, organization name, and account identifier.

10. Access the Snowflake web interface to start using the platform.

Optionally, configure your account by adding users, roles, databases, and tables.

Refer to [Snowflake documentation ](https://docs.snowflake.com/user-guide/admin-trial-account) for further guidance.

## **steps**:

#### Intall Docker ####

##### 1. Download and install Docker by following the official instructions for your operating system. #####

##### 2. Once the installation is complete, verify that Docker is running by opening a terminal (or command prompt) and running the following command: #####

```sh
docker --version
```
You should see the Docker version information printed in the terminal.

### Install the project dependencies:

```sh
pip install -r requirements.txt
```
### Running the container

1. start required docker services with docker-compose-initiate database

    ```sh

     cd dockerairflow

     docker compose up airflow-init

    ```

2. check all docker application services up and running

    Running Airflow:

    ```sh

    docker compose up

    ```

3. Start the Airflow scheduler and web server:

    ```sh

    airflow scheduler

    airflow webserver -p 8080

    ```

### Configuration

1. Open the dbt_project.yml file and update the necessary configurations, such as **target database**, **credentials**, and other project-specific settings.

2. Configure your database connection by creating a **profiles.yml** file in the ~/.dbt directory. Refer to the [dbt Profiles Documentation](https://docs.getdbt.com/reference/warehouse-profiles) for more details.

## Running the project

Please make sure to have yt.csv file available in your project seed file before running the dbt commands.

#### Building Data Models ####

**To build the data models and transform your data, follow these steps:**

##### 1. Test the database connection and show information for debugging purposes ####

```sh

cd dbt_project

dbt debug

```

##### 2. Downloads dependencies for a project

```sh

dbt deps

```

##### 3. Loads CSV files into the database #####

```sh

dbt seed

```
This command will load csv files located in the seed-paths directory of your dbt project into your data warehouse.

##### 4. To execute the compiled SQL transformations and materialize the models, use the following command: #####

```sh

dbt run

```
Running this command will create or update the tables/views defined in your project. It applies the transformations defined in the models and loads the data into the target database.

##### If you want to perform a full refresh of the data models, including dropping and recreating the tables/views, use the following command: #####

```sh

dbt run --full-refresh
```
This command ensures that the data models reflect the latest state of the source data.

#### Testing ####

**To test the project models and ensure the accuracy of the transformations, follow these step:**

##### To execute the tests defined in your project, use the following command: #####

```sh

dbt test

```

This command runs the tests specified in this project, checking if the expected results match the actual data.

#### Documentation ####

**To generate and view the documentation for this dbt project, follow these steps:**

##### 1. Generate the documentation by running the following command: #####

```sh

dbt docs generate

```
This command generates HTML pages documenting the models, tests, and macros in your project.

#####  2. Serve the documentation locally by running the following command: #####

```sh
dbt docs serve

```
This command starts a local web server to host the documentation. You can access it by opening your browser and visiting the provided URL.

**Note**: Remember to generate the documentation before serving it.

###### Generated lineage graph

![Lineage graph](Graph-1.png)

 Refer the [dbt commands](https://docs.getdbt.com/reference/dbt-commands) for more details.

#### Airflow Web UI

The Airflow Web UI provides a graphical interface for managing and monitoring workflows. Through the UI, you can:

- View and manage DAGs, including enabling/disabling DAGs and individual tasks.

- Trigger manual executions of tasks or entire DAGs.

- Monitor task status, logs, and execution history.

- Configure connections to external systems and variables for use within your DAGs.

- Define schedules and set up task dependencies.

- The Airflow Web UI offers a user-friendly way to interact with Airflow and gain insights into your workflows.

To access the Airflow Web UI, you need to follow these steps:

1. Install and Configure Airflow: Ensure that you have installed and configured Airflow on your machine or server. Refer to the official [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) for detailed instructions on installation and configuration.

2. Start the Airflow Web Server: Open a terminal or command prompt and navigate to the Airflow installation directory. Use the following command to start the Airflow web server:

    ```sh
    airflow webserver
    ```
- By default, the web server will listen on port 8080. If you want to use a different port, you can specify it using the -p or --port option followed by the desired port number.

3. Access the Airflow Web UI: Open a web browser and enter the following URL:

    ```sh

    http://localhost:8080

    ```
- If you started the web server on a different port, replace 8080 with the corresponding port number.


4. Login to the Airflow Web UI: You will be directed to the Airflow login page. Enter your username and password to log in. The default username and password are typically set to admin. Make sure to change the default credentials for security reasons.

5. Explore the Airflow Web UI: Once logged in, you will be presented with the Airflow Web UI. Here, you can perform various actions such as:

    - View and manage DAGs: The UI provides an overview of all your DAGs, their status, and configuration details. You can enable or disable DAGs, trigger manual runs, and view the DAG structure.

    - Monitor task execution: Check the status of individual tasks, view task logs, and track the execution history. You can identify successful runs, failed runs, and ongoing runs.

    - Configure connections and variables: Airflow allows you to define connections to external systems (e.g., databases, APIs) and variables (e.g., reusable configuration values). You can manage these configurations through the web UI.

    - Access additional features: The Airflow Web UI offers other functionalities, such as browsing logs, configuring access controls, and managing plugins. Explore the UI to leverage these features.

    Remember to secure access to the Airflow Web UI by configuring authentication and authorization mechanisms according to your requirements.

    By following these steps, you should be able to access and utilize the Airflow Web UI for managing and monitoring your workflows