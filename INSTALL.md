# Improve Food Installation Guide

## Requirements

- Python 3.x
- MongoDB Atlas account (or local MongoDB instance)
- pip

## Install Dependencies

```bash
python3 -m pip install flask pymongo python-dotenv certifi
```

## Environment Variables

Create a `.env` file containing:

```
MONGO_URI=<your MongoDB connection string>
SECRET_KEY=<your Flask secret key>
```

## Run the Application

```bash
python3 app.py
```

The application will start on port 5000.

## Notes

This project was developed in the course Jupyter environment. Some routing behavior may differ when running behind the Jupyter proxy. When run in a standard local Flask environment, navigation behaves normally.