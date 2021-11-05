# This project containins code for building Data Warehouse using AWS + Snowflake technologies

___

#Basically it is somethinh like ETL tool to build data warehouse
###This project was created to build Data Warehouse using cloud infrastructure(AWS + Snowflake)
###Main idea is to take free <a href="https://knoema.com/atlas/topics/Agriculture">KNOEMA</a> agriculture data atlas(2 million rows), ingest this atlas to AWS S3 storage. Then perform some transformations to make data atlas  be more normalized and compress data using Athena data manipulation engine.
### Finally load data to Snowflake to be able to query it fast and integrate it with PowerBI tool
<!-- GETTING STARTED -->
## Getting Started



This code is taking care of s3 and snowflake pipelines.
Using this repo you can generate infrastructure on S3 and Snowflake easily and without extra effort


### Prerequisites

1. _First of all make sure that you have AWS Account available_

2. _Then register to Snowflake and make setup there_

3. _Export AWS and Snowflake credentials in the following way:_

  ```sh
  export SNOWFLAKE_USER=YourSnowUser
  export SNOWFLAKE_PASSWORD=YourSnowUserPassword
  export AWS_ACCESS_KEY_ID=AWS_ID_PROVIDED_AFTER_REGISTRATION
  export AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCES_KEY_AFTER_REGSTRATION
  
  ```

### Installation

_Execute this script on your env to install necessary dependencies_

1. Clone the repo
   ```sh
   git clone git@github.com:Dudar99/agriculture_insight.git
   ```
2. Execute script to install dependencies
   ```sh
   sh setuplocal.sh
   ```

<!-- USAGE EXAMPLES -->
## Usage

Here is example how to manipulate with infra using scheduler.py script

__To generate everything from scratch use this command:__

   ```sh
   python scheduler.py --generate
   ```
__To delete tables  use this command:__

   ```sh
   python scheduler.py --delete
   ```
__This command need to be automated using some CRON job etc. It is main entry point to refresh our Data Warehouse:__

   ```sh
   python scheduler.py --refresh
   ```
<p align="right">(<a href="#top">back to top</a>)</p>
