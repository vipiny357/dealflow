#!/bin/bash

# Configure Nginx to proxy requests to Uvicorn
cat > /etc/nginx/sites-available/fastapi_nginx <<EOL
server {
    listen 80;
    server_name 18.222.217.21;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
EOL

# Create a symbolic link to enable the Nginx configuration
ln -s /etc/nginx/sites-available/fastapi_nginx /etc/nginx/sites-enabled/

# Restart Nginx
systemctl restart nginx
