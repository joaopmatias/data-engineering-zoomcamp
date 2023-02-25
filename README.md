## Week 2: Workflow Orchestration

> If you're looking for Airflow videos from the 2022 edition,
> check the [2022 cohort folder](../cohorts/2022/week_2_data_ingestion/).

Python code from videos is linked [below](#code-repository).

Also, if you find the commands too small to view in Kalise's videos, here's the [transcript with code for the second Prefect video](https://github.com/discdiver/prefect-zoomcamp/tree/main/flows/01_start) and the [fifth Prefect video](https://github.com/discdiver/prefect-zoomcamp/tree/main/flows/01_start).

### Data Lake (GCS)

* What is a Data Lake
* ELT vs. ETL
* Alternatives to components (S3/HDFS, Redshift, Snowflake etc.)
* [Video](https://www.youtube.com/watch?v=W3Zm6rjOq70&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
* [Slides](https://docs.google.com/presentation/d/1RkH-YhBz2apIjYZAxUz2Uks4Pt51-fVWVN9CcH9ckyY/edit?usp=sharing)


### 1. Introduction to Workflow orchestration

* What is orchestration?
* Workflow orchestrators vs. other types of orchestrators
* Core features of a workflow orchestration tool
* Different types of workflow orchestration tools that currently exist 

:movie_camera: [Video](https://www.youtube.com/watch?v=8oLs6pzHp68&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)


### 2. Introduction to Prefect concepts

* What is Prefect?
* Installing Prefect
* Prefect flow
* Creating an ETL
* Prefect task
* Blocks and collections
* Orion UI

:movie_camera: [Video](https://www.youtube.com/watch?v=cdtN6dhp708&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

### 3. ETL with GCP & Prefect

* Flow 1: Putting data to Google Cloud Storage 

:movie_camera: [Video](https://www.youtube.com/watch?v=W-rMz_2GwqQ&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)


### 4. From Google Cloud Storage to Big Query

* Flow 2: From GCS to BigQuery

:movie_camera: [Video](https://www.youtube.com/watch?v=Cx5jt-V5sgE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

### 5. Parametrizing Flow & Deployments 

* Parametrizing the script from your flow
* Parameter validation with Pydantic
* Creating a deployment locally
* Setting up Prefect Agent
* Running the flow
* Notifications

:movie_camera: [Video](https://www.youtube.com/watch?v=QrDxPjX10iw&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

### 6. Schedules & Docker Storage with Infrastructure

* Scheduling a deployment
* Flow code storage
* Running tasks in Docker

:movie_camera: [Video](https://www.youtube.com/watch?v=psNSzqTsi-s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

### 7. Prefect Cloud and Additional Resources 


* Using Prefect Cloud instead of local Prefect
* Workspaces
* Running flows on GCP

:movie_camera: [Video](https://www.youtube.com/watch?v=gGC23ZK7lr8&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

* [Prefect docs](https://docs.prefect.io/)
* [Pefect Discourse](https://discourse.prefect.io/)
* [Prefect Cloud](https://app.prefect.cloud/)
* [Prefect Slack](https://prefect-community.slack.com)

### Code repository

[Code from videos](https://github.com/discdiver/prefect-zoomcamp) (with a few minor enhancements)

### Homework 
Homework can be found [here](../cohorts/2023/week_2_workflow_orchestration/homework.md).

## Community notes

Did you take notes? You can share them here.

* [Blog by Marcos Torregrosa (Prefect)](https://www.n4gash.com/2023/data-engineering-zoomcamp-semana-2/)
* [Notes from Victor Padilha](https://github.com/padilha/de-zoomcamp/tree/master/week2)
* [Notes by Alain Boisvert](https://github.com/boisalai/de-zoomcamp-2023/blob/main/week2.md)
* [Notes by Candace Williams](https://github.com/teacherc/de_zoomcamp_candace2023/blob/main/week_2/week2_notes.md)
* [Notes from Xia He-Bleinagel](https://xiahe-bleinagel.com/2023/02/week-2-data-engineering-zoomcamp-notes-prefect/)
* [Notes from froukje](https://github.com/froukje/de-zoomcamp/blob/main/week_2_workflow_orchestration/notes/notes_week_02.md)
* [Notes from Balaji](https://github.com/Balajirvp/DE-Zoomcamp/blob/main/Week%202/Detailed%20Week%202%20Notes.ipynb)
* Add your notes here (above this line)


### 2022 notes 

* Batch processing
* What is Spark
* Spark Dataframes
* Spark SQL
* Internals: GroupBy and joins

[More details](week_5_batch_processing)

### [Week 6: Streaming](week_6_stream_processing)

* Introduction to Kafka
* Schemas (avro)
* Kafka Streams
* Kafka Connect and KSQL

[More details](week_6_stream_processing)


### [Week 7, 8 & 9: Project](week_7_project)

Putting everything we learned to practice

* Week 7 and 8: working on your project
* Week 9: reviewing your peers

[More details](week_7_project)


### Workshop: Maximizing Confidence in Your Data Model Changes with dbt and PipeRider


[More details](cohorts/2023/workshops/piperider.md)

## Overview

### Architecture diagram
<img src="images/architecture/arch_2.png"/>

### Technologies
* *Google Cloud Platform (GCP)*: Cloud-based auto-scaling platform by Google
  * *Google Cloud Storage (GCS)*: Data Lake
  * *BigQuery*: Data Warehouse
* *Terraform*: Infrastructure-as-Code (IaC)
* *Docker*: Containerization
* *SQL*: Data Analysis & Exploration
* *Prefect*: Workflow Orchestration
* *dbt*: Data Transformation
* *Spark*: Distributed Processing
* *Kafka*: Streaming


### Prerequisites

To get the most out of this course, you should feel comfortable with coding and command line
and know the basics of SQL. Prior experience with Python will be helpful, but you can pick
Python relatively fast if you have experience with other programming languages.

Prior experience with data engineering is not required.



## Instructors

- Ankush Khanna (https://linkedin.com/in/ankushkhanna2)
- Sejal Vaidya (https://linkedin.com/in/vaidyasejal)
- Victoria Perez Mola (https://www.linkedin.com/in/victoriaperezmola/)
- Kalise Richmond (https://www.linkedin.com/in/kaliserichmond/)
- Jeff Hale (https://www.linkedin.com/in/-jeffhale/)
- Alexey Grigorev (https://linkedin.com/in/agrigorev)

## Tools

For this course, you'll need to have the following software installed on your computer:

* Docker and Docker-Compose
* Python 3 (e.g. via [Anaconda](https://www.anaconda.com/products/individual))
* Google Cloud SDK
* Terraform

See [Week 1](week_1_basics_n_setup) for more details about installing these tools



## FAQ


* **Q**: I registered, but haven't received a confirmation email. Is it normal?
  **A**: Yes, it's normal. It's not automated. But you will receive an email eventually.
* **Q**: At what time of the day will it happen?
  **A**: Office hours will happen on Mondays at 17:00 CET. But everything will be recorded, so you can watch it whenever it's convenient for you.
* **Q**: Will there be a certificate?
  **A**: Yes, if you complete the project.
* **Q**: I'm 100% not sure I'll be able to attend. Can I still sign up?
  **A**: Yes, please do! You'll receive all the updates and then you can watch the course at your own pace.
* **Q**: Do you plan to run a ML engineering course as well?
**A**: Glad you asked. [We do](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) :)
* **Q**: I'm stuck! I've got a technical question!
  **A**: Ask on Slack! And check out the [student FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing); many common issues have been answered already. If your issue is solved, please add how you solved it to the document. Thanks!



## Supporters and partners

Thanks to the course sponsors for making it possible to create this course

<p align="center">
  <a href="https://www.prefect.io/">
    <img height="100" src="https://github.com/DataTalksClub/mlops-zoomcamp/raw/main/images/prefect.png">
  </a>
</p>

<p align="center">
  <a href="https://www.piperider.io/">
    <img height="130" src="images/piperider.png">
  </a>
</p>


Do you want to support our course and our community? Please reach out to [alexey@datatalks.club](alexey@datatalks.club)

* [Notes from Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/2_data_ingestion.md)
* [Notes from Aaron Wright](https://github.com/ABZ-Aaron/DataEngineerZoomCamp/blob/master/week_2_data_ingestion/README.md)
* [Notes from Abd](https://itnadigital.notion.site/Week-2-Data-Ingestion-ec2d0d36c0664bc4b8be6a554b2765fd)
* [Blog post by Isaac Kargar](https://kargarisaac.github.io/blog/data%20engineering/jupyter/2022/01/25/data-engineering-w2.html)
* [Blog, notes, walkthroughs by Sandy Behrens](https://learningdataengineering540969211.wordpress.com/2022/01/30/week-2-de-zoomcamp-2-3-2-ingesting-data-to-gcp-with-airflow/)
* [Notes from Vincenzo Galante](https://binchentso.notion.site/Data-Talks-Club-Data-Engineering-Zoomcamp-8699af8e7ff94ec49e6f9bdec8eb69fd)
* More on [Pandas vs SQL, Prefect capabilities, and testing your data](https://medium.com/@verazabeida/zoomcamp-2023-week-3-7f27bb8c483f), by Vera
