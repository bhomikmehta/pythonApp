FROM python:3.9

WORKDIR /app

COPY ./app/requirements.txt .
COPY ./app/app.py .
RUN pip install -r requirements.txt

# Download Telegraf package
RUN wget https://dl.influxdata.com/telegraf/releases/telegraf_1.20.2-1_amd64.deb

# Install Telegraf using dpkg
RUN dpkg -i telegraf_1.20.2-1_amd64.deb

# Clean up downloaded package
RUN rm telegraf_1.20.2-1_amd64.deb

# Copy Telegraf configuration file
COPY ./app/telegraf.conf /etc/telegraf/telegraf.conf

CMD telegraf --config /etc/telegraf/telegraf.conf & python app.py