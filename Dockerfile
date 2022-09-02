FROM python:3.10-alpine

EXPOSE 5000

WORKDIR /app
ENV db_connection="sqlite:///data.db"

# install pip updates
RUN python -m pip install --upgrade pip
COPY requirements.txt .
# install requirementsg
RUN pip install -r requirements.txt
COPY . .
