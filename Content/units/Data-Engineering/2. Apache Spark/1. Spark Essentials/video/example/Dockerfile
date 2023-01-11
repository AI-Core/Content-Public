FROM openjdk:slim
COPY --from=python:3.6 / /
RUN pip install pyspark

CMD tail -f /dev/null