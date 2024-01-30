FROM postgres:latest

# Set environment variables for the PostgreSQL database
ENV POSTGRES_USER=franciscoavila
ENV POSTGRES_PASSWORD=password

# Expose port 5432 for PostgreSQL
EXPOSE 5432

# Enable SUPERUSER rights for the database
ENV POSTGRES_DB=container_todo_db
ENV POSTGRES_INITDB_ARGS="--encoding=UTF-8 --lc-collate=C --lc-ctype=C --data-checksums"

# Start the PostgreSQL server using the correct entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]

# Pass the command "postgres" as an argument to the entrypoint
CMD ["postgres"]