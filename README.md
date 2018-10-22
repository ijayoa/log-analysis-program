# Log Analysis Python Program

This a program written in python to carry out analysis on over 1 million log entries in a news site database. 
The program reports business critical information.

#### What to expect from the program: 
- Makes use of a postgresql database and queries.
- Outputs three critical reports in plain text.
- Executes complex reporting in a single database query.

# How to run this project

_You will need to run this program on a Linux machine. If you are on a different operating system, you can install a Linux-based virtual machine using [Virtual box](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/downloads.html)._ 

### Getting started

- Download a the news database here - [News Site DB](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Use [git](https://github.com/ijayoa/log-analysis-program) to clone this respository and save a local copy on your machine.

### Setting up the database

- Unzip the database file and navigate to the folder location in your terminal. 
- Run the following command to create the database and then connect to it.

```
$ psql -d news -f newsdata.sql
$ psql -d news

```
- Next you'll want to run this line of code to create a view within your news database.

```
CREATE VIEW log_report AS 
SELECT TO_CHAR(log.time:: DATE , 'Month dd,yyyy') AS day, 
COUNT(*) AS requests,
COUNT(*) FILTER (WHERE status != '200 OK') AS error 
FROM log 
GROUP BY day;
```
 - I recommend running some commands to verify everything's set up okay. 
 
 ```
 # list all the tables in the database : expect three: log, authors and articles
news=> \dt

# check view for records 
news=> select * from log_report limit 10;

```

### Running the Python Program

In your terminal navigate to your cloned version of this repo, you should see a file called `logdb.py`. 
That's the file you want to run. Type in the following: 

```
$ python logdb.py

```

# Got Any Errors?

- Ensure you are using Python 2 to run this.
- Did you create the log_report view? If you didn't you will get an error. Run the sql command above.
