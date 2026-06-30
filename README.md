# Automated Broadway Data Pipeline with Airflow and Snowflake

This project implements an automated data engineering pipeline for Broadway show datasets using **Apache Airflow** and **Snowflake**. The pipeline processes raw CSV files, detects upstream data availability, loads historical data into Snowflake, validates data quality, refreshes views, and generates dimensional tables for downstream analysis.

## Project Overview

The goal of this project is to build a reliable and maintainable ETL workflow for Broadway performance and ticketing data. The pipeline supports automated ingestion of raw data, historical table updates, signal table tracking, and data validation through custom Airflow components.

The project focuses on three major tasks:

- Loading raw Broadway CSV datasets into Snowflake
- Building historical and dimensional tables for analysis
- Validating upstream partitions, null values, and percentage-based metrics

## Tech Stack

- **Apache Airflow**: Workflow orchestration and DAG scheduling
- **Snowflake**: Cloud data warehouse for data storage and transformation
- **Python**: Custom operators, sensors, and validation logic
- **SQL**: Data modeling and table/view generation
- **CSV**: Raw input data source

## Repository Structure

```text
.
├── dags/
│   ├── data/
│   │   ├── cpi.csv
│   │   ├── grosses.csv
│   │   ├── pre_1985_starts.csv
│   │   └── synopses.csv
│   ├── utils/
│   │   └── constants.py
│   └── ...
├── plugins/
│   ├── operators/
│   │   ├── snowflake_historical_operator.py
│   │   ├── snowflake_percentage_check_operator.py
│   │   └── snowflake_signal_sensor.py
│   └── utils/
│       └── constants.py
├── Data Pipelines.pdf
├── HW_3b.pdf
└── README.md
