# Video Translation Client Library

## Overview
This library allows you to check the status of video translations using the Heygen video translation server.

## Enhancements

The server simulates the status of video translation jobs using a weighted random choice. The current implementation uses the following weights:

```python
status = random.choice(['pending', 'completed', 'error'])
```
To Reduce the Error rate, we can use the following weights (This statement will be available as a comment in the server.py File):

```python
status = random.choices(['pending', 'completed', 'error'], weights=[80, 15, 5], k=1)[0]
```

## Installation
Make sure to install the required packages:

```bash
pip install Flask requests
```