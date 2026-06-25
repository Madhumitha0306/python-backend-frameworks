# TASK 1 - REQUEST RESPONSE CYCLE

# Browser
#    ↓
# URL Router
#    ↓
# View
#    ↓
# Model (Database)
#    ↓
# Response
#    ↓
# Browser


# MIDDLEWARE

# Middleware is a layer between the request and response.

# Request
#    ↓
# Middleware
#    ↓
# View
#    ↓
# Middleware
#    ↓
# Response

# Example 1:
# SecurityMiddleware
# Adds security protections to the application.

# Example 2:
# SessionMiddleware
# Manages user session data such as login information.


# WSGI vs ASGI

# WSGI (Web Server Gateway Interface)
# Handles synchronous requests.
# Django uses WSGI by default.

# ASGI (Asynchronous Server Gateway Interface)
# Handles asynchronous requests.
# Supports WebSockets and real-time applications.

# When to use WSGI?
# - Normal websites
# - Blogs
# - College portals
# - E-commerce sites

# When to use ASGI?
# - Chat applications
# - Live notifications
# - Real-time dashboards
# - Video conferencing apps

# MVC vs MVT

# MVC Architecture

# Model      -> Data and Database
# View       -> User Interface (UI)
# Controller -> Business Logic

# Django uses MVT Architecture

# Model    -> Data and Database
# View     -> Business Logic
# Template -> User Interface (UI)

# Mapping MVC to MVT

# MVC Model      = Django Model
# MVC View       = Django Template
# MVC Controller = Django View