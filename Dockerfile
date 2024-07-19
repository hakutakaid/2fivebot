FROM python:3.10.14

# Update apt-get and install necessary packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends git\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy application files to /app directory
COPY . /app/
WORKDIR /app/

# Upgrade pip and install Python dependencies in a virtual environment
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m venv venv \
    && . venv/bin/activate \
    && pip install --no-cache-dir -U -r requirements.txt

# Ensure the virtual environment is activated when the container runs
ENV PATH="/app/venv/bin:$PATH"

# Set the command to start the application
CMD ["bash", "start"]