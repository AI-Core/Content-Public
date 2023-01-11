<!-- MOTIVATION -->

- once you deploy something, that's not the end of the road
- you might need to know
- how many requests is it receiving
- how hot is the CPU getting
- how much memory is spare
- that means, you need to monitor it

- one of the most popular options is prometheus

_show website_

<!-- BIG -->

- open source project with a EXTREMELY large community
- 2nd project to join the cloud native computing foundation in 2016, after kubernetes

_scroll to bottom and show all companies using it_

**sarcastically**

- which you _might_ have heard of

 <!-- DATA RETRIEVAL -->

- prometheus monitors specific "targets", which are IP addresses

\_show diagram of retrieval highlighted)

- on each of those targets it pulls in "metrics"
- things like the memory usage, rate of requests, or anything else
- prometheus does that by making a get request to a /metrics endpoint on the target

_show diagram of prom pulling in metrics_

<!--  -->

- to serve metrics in the prometheus format from this endpoint is to run an exporter

- the node exporter is the most fundamental and is used for essential hardware metrics like temperature or CPU
- but there are many off the shelf exporters for common software components too which gather and serve you related metrics on the /metrics endpoint

_show list of public exporters_

- or you can implement custom exporters using a client library for example in python

_show import prometheus in python_

<!-- YAML FILE -->

- all of the targets can be configured in yaml

_show prometheus yaml file_

<!-- PULL NOT PUSH -->

- it's key to understand that prometheus pulls in data
- data isn't pushed to it
- if it was, then too many requests could overwhelm the monitoring service and turn it into a bottleneck
- instead prometheus _pulls_ in data when it needs to

- pulling data in also makes it easy to identify specifically which service is down and when
- because the requests to them fail

_show list of exporters_

- even when other components of the sytem do fail, prometheus is designed to stay up
- it's totally standalone
- and even includes it's own storage

<!-- METRIC TYPES -->

_show storage section_

- there are 3 key types of metrics

<!-- GAUGE -->

- which can go up and down arbitrarily
<!-- COUNTER -->
- which can only go up
<!-- HISTOGRAM -->
- for measuring how big or how long something was

<!-- STORED IN SPECIAL PROMETHEUS FORMAT WITH A TYPE AND HELP -->

- all of this is stored on disk in a special prometheus format
- which you can see at the /metrics endpoint

<!-- SERVING -->

- prometheus runs its own web server which actually shows all the metrics it's monitoring from its targets, and also it's own machine
- these can then be queried in the prometheus UI
- or pulled in by other visualisation tools like grafana

<!-- OTHER THINGS -->

<!-- - email alerting -->

<!-- OUTRO -->

- so if you only had 90 seconds to learn about prometheus, that's the essentials
