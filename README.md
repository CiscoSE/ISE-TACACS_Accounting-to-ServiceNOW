# ISE/TACACS Accounting to ServiceNOW Change

## Motivation
The motivation for this code is to solve a need for organizations who would like to automatically create a change management ticket into ServiceNOW whenever a network administrator works on their company devices. There are a couple of ways to solve this but I decided to use Logstash, which allows for flexibilities from transforms during the Logstash process.

## Prerequisites
1. ISE 2.4 (2.2 and 2.3 should work but wasn't tested during the build)
2. Workload capable of running Logstash. (Tested on EC2 in AWS)
3. ServiceNOW account with an account capable of creating Change Management tickets

### Step 1 - Install logstash
```
The first step to installing Logstash from YUM is to retrieve Elastic’s public key.
[user]$ rpm –import https://artifacts.elastic.co/GPG-KEY-elasticsearch

Next, create a logstash.repo file in /etc/yum.repos.d/ with the following contents:
[logstash-6.x]
name=Elastic repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md

Now your repository is ready for use. So install Logstash with this command line:
[user]$ sudo yum install logstash

Before you start, you need to make two changes to the current user’s environment. First, you need to add your current user to the logstash group so it can write to the application’s directories for caching messages. The usermod command will do this for you.
[user]$ sudo usermod -a -G logstash ec2-user

Next, if you’re running this tutorial on a micro instance, you may have memory problems. Modify your .bashrc and add this line:
[user]$ export LS_JAVA_OPTS=“-Xms500m -Xmx500m -XX:ParallelGCThreads=1”

```
### Step 2 - Copy the logstash.conf to /etc/logstash/conf.d/
This conf file creates a daily log in /var/log/logstash/tacacs-{YYYY-MM-dd}. This is important because the script attaches this file into the ServiceNOW change.

### Step 3 - Configure ISE to send TACACS commands to the logstash remote target
![alt text](https://github.com/CiscoSE/ISE-TACACS_Accounting-to-ServiceNOW/blob/master/images/remote%20target-fixed.png)
![alt text](https://github.com/CiscoSE/ISE-TACACS_Accounting-to-ServiceNOW/blob/master/images/Logging%20Category.png)

### Step 4 - Setup a cronjob to run the script
Note that logstash creates a new log name for each day, so running this script on a daily basis would be advisable. You can modify the code to aggregate the logs for the last 7 days would be good too. I may end up doing that if there is an ask.
```
$ python3 ISE-TACACS-ServiceNOW-Changes.py
```
![alt text](https://github.com/CiscoSE/ISE-TACACS_Accounting-to-ServiceNOW/blob/master/images/SNOW-Change.png)

## Credits
AWS Document around logstash that I took directly and placed above https://aws.amazon.com/elasticsearch-service/resources/articles/logstash-tutorial/ . Various references from ServiceNOW.

## License
This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
