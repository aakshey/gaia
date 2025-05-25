# Gaia

This repository contains a simple Flask web application that accepts a user's
email address and sends them a message saying "Hi". The SMTP server
configuration is defined in `app.py`.

## Running the app

Install dependencies and run the server:

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000/` in your browser to submit an email address
using the provided form. Alternatively, you can send a POST request to
`http://localhost:5000/send` with JSON body containing the `email` field.

## Testing

Run unit tests with:

```bash
python -m unittest
```
