# ISE TACACS Accounting to ServiceNOW

## Prerequisites
1. ISE 2.4 (2.2 and 2.3 should work but wasn't tested during the build)
2. Workload capable of running Logstash
3. ServiceNOW account with a service account capable of creating Change Management tickets


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
```
