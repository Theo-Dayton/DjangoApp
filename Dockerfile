# Use a base image with Python (choose the appropriate version for your app)
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory inside the container
WORKDIR /

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's source code
COPY . .

# Expose the port your Django app is listening on (default is 8000)
EXPOSE 8000

# Collect static files (if using Django's static files)
RUN python manage.py collectstatic --noinput

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]