FROM python:3.12.3
WORKDIR /app
COPY . /app
RUN pip install pandas
ENTRYPOINT [ "python", "docker_test_calc.py" ]