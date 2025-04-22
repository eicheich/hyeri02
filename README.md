# Lee Hyeri Fan Website

A Django-based fan website dedicated to Lee Hyeri.

## Features

- Photo gallery
- Biography information
- Responsive design

## Deployment Instructions

### GitHub Setup
1. Initialize a Git repository:
   ```
   git init
   ```
2. Add all files to the repository:
   ```
   git add .
   ```
3. Commit the files:
   ```
   git commit -m "Initial commit"
   ```
4. Create a new repository on GitHub
5. Add the remote and push:
   ```
   git remote add origin https://github.com/yourusername/hyeri-fan-website.git
   git branch -M main
   git push -u origin main
   ```

### cPanel Deployment
1. Log in to your cPanel account
2. Navigate to "Git™ Version Control"
3. Click "Create" to set up a new Git repository
4. Fill in the required details:
   - Clone URL: Your GitHub repository URL
   - Repository path: The directory where you want to clone the repo (e.g., `public_html/hyeri`)
5. Click "Create" to clone the repository

6. Set up a Python application:
   - In cPanel, find "Setup Python App"
   - Choose Python version (3.8+ recommended)
   - Set application root to your cloned repository
   - Set application URL
   - In the application startup file, enter: passenger_wsgi.py

7. Install dependencies:
   - SSH into your server
   - Navigate to your repository directory
   - Run: `pip install -r requirements.txt`

8. Configure the database in settings.py with your cPanel database credentials

9. Collect static files:
   ```
   python manage.py collectstatic
   ```

10. Apply migrations:
   ```
   python manage.py migrate
   ```

11. Restart the Python application from cPanel

## Requirements
See requirements.txt file for package dependencies
