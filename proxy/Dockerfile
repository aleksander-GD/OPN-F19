FROM nginx

# Remove default conf
RUN rm /etc/nginx/conf.d/*

# Copy html and conf file
#COPY nginx.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/
COPY ssl/ /etc/ssl/
COPY html /usr/share/nginx/html