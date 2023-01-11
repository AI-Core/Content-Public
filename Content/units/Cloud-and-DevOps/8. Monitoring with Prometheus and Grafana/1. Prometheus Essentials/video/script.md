<!-- INTRO -->

- so let's get started monitoring our application using prometheus

<!-- RUN PROMETHEUS IN DOCKER -->

- these days almost all applications are containerised so it makes sense to run prometheus inside a docker container
- you can run the official image on its own
- and you can find it at prom/prometheus

_Enter `docker run prom/prometheus`_

- but before I run that I need to expose port 9090, that prometheus runs on, outside my container

_add -p `9090:9090` flag_

- and I also need to specify the config file

_make new prometheus.yaml file_

copy in default example from prometheus documentation https://prometheus.io/docs/prometheus/latest/getting_started/

- I'll copy in the default template
<!-- - which simply does X -->

- and then bind mount it's location to the container, so the container can access the config file which is on the host machine

_add `-v config/prometheus.yml:/etc/prometheus/prometheus.yml`_

_run the command_

<!-- OPEN PROMETHEUS UI -->

- now that it's running, you can access the prometheus UI at the root

<!-- SHOW PROMETHEUS LOGGING FORMAT -->

- you can see the metrics being logged by prometheus, and the format which it stores them, at `/metrics`

- back to the UI at the root, we can see the targets which these come from
- by default, prometheus is just monitoring itself

_browse the targets_

<!-- BROWSE METRICS AND OTHER THINGS LIKE THE TARGETS -->

- here you can make queries in prometheus' query language, promQL

_Query cpu_

- we call this the "metric name"

_Highlight metric name_

- And you can find all of these and their definitions in the prometheus docs

_Screen capture some of those in the docs_

- when I run this, it shows me what data was pulled in at each timestamp in a table
- then I can hit the graph tab to show this over time

- and we can also specify key value pair filters which we call "labels" within braces after the metric names
- and can apply multiple labels at once by separating them with commas

_Add labels_

- you can also specify a timeframe using square brackets
- you can only see table data when you do this

- if you enter an invalid metric then it will tell you this

- if your synttax is wron, you'll get atn error

<!-- USE PYTHON TO CREATE CUSTOM METRICS -->

- by default, prometheus logs a bunch of hardware metrics
- but often, you want to be able to log custom metrics
- for example, you might want to know how many times some python code encounters an error

_Install python client_

- `pip install prometheus_client`\_

_Import python client_

_`from prometheus_client import Counter`_

- the prometheus client allows you to define a metric like this counter

- and then start a web server like this which exposes a HTTP endpoint at /metrics

- just like any other exporter needs to

- im gonna use docker compose to spin up one container running this python code on port 9100 and another running prometheus

- but first, I need to update the prometheus YAML to specify my python target

_show other prometheus.yml with python target_

# Did to here

_docker compose up_

- and now prometheus should be scraping that metric

- so we can find it in the UI

- and those are the very essentials of prometheus
