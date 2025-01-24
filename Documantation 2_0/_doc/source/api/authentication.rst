Authentication
=============

Overview
--------
Authentication in the RIS-Web Backend is handled through Django's built-in authentication system.

Authentication Methods
--------------------
1. Session Authentication
   - Used for admin interface
   - Cookie-based authentication
   - CSRF protection enabled

2. Development Settings
   - Debug mode authentication
   - Local development users

Security Configuration
--------------------
.. code-block:: python

   # Security settings in ris_prj/settings/base.py
   AUTHENTICATION_BACKENDS = [
       'django.contrib.auth.backends.ModelBackend',
   ]

   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
