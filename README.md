# Run Python Script with MariaDB Connector
Uses a CentOS 7 base image to deploy a container with MariaDB Connector/Python installed. Immediately runs file `script.py` and exits on completion.

# Dependencies

* [Docker Engine](https://docs.docker.com/engine/install/)

# Install and Run
Download/clone/extract the code to a directory. Open a terminal and change into the directory the code is in. Then-

```
docker build -t python-script . ;
docker run python-script ;
```

# View Logs

```
docker logs python-script ;
```

# Included Code
A default `script.py` comes with this repository. Expect the following output when using it without any modifications-

```
Error connecting to MariaDB Platform: Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)
```

To test connectivity to your MariaDB server, edit `Dockerfile` and change `ENV` lines to the correct MariaDB user, password, IPv4 address or FQDN, and port for your remote MariaDB server. You can then rebuild this container and see if the output of the test script changes.

# Use Your Script
Move the existing `script.py` and then copy (or move) the Python script you want to run to `script.py`. Then rebuild the image and run as normal.

## Note on `ENV`
The included `script.py` is coded to pull data from `ENV`. This functionality is not inherent though. If you would like your Python script to support this, please review the source code of the included `script.py` and adapt it for your needs.

# Connecting to MariaDB
The container only provides connector infrastructure, it does not provide a running MariaDB server. Reference [Connector/Python documentation](https://mariadb.com/docs/appdev/connector-python/#opening-a-connection) to learn how to specify parameters to open a connection to a remote MariaDB server.
