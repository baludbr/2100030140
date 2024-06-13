# Average Calculator Microservice

## Overview

The Average Calculator Microservice calculates the average of a sliding window of numbers fetched from a test server based on specific criteria. It exposes a REST API endpoint to fetch and manage numbers dynamically.

### Features

- Fetch numbers based on criteria ('p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random) from a test server.
- Manage a sliding window of fetched numbers with a configurable size (e.g., 10).
- Calculate and return the average of the current window of numbers.
- Ensure uniqueness of numbers within the window and handle edge cases like duplicates.
- Respond within 500 milliseconds for each request.

---

# Product Service API

## Overview

The Product Service API provides functionalities to retrieve and manage product information from various e-commerce companies through a unified interface. It exposes REST API endpoints to fetch product data, apply filters, sorting, and pagination.

### Features

- Retrieve products by category and company.
- Filter products based on criteria such as price range, ratings, and availability.
- Sort products by price, ratings, company, or discount.
- Paginate results for efficient data retrieval.
- Standardize product data format across different e-commerce platforms.

## Installation and Setup

### Requirements

- Python 3.x
- Django (Python web framework)
- requests (HTTP library for Python)
