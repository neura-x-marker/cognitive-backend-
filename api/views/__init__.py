"""
Views package initialization.

Usage:
1. Create a new file for your views (e.g., `api/views/auth_views.py`).
2. Define your view classes or functions inside that file.
3. Import them here to make them available at the package level:
   `from .auth_views import LoginView, LogoutView`
"""

from .auth import register, login
