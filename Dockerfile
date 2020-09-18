FROM centos:7
ENV container docker
ENV MARIADB_USER='connpy_test'
ENV MARIADB_PASS='passwd'
ENV MARIADB_HOST='localhost'
ENV MARIADB_PORT=3306
RUN curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash ;
RUN yum -y install gcc python3-devel ;
RUN yum -y install MariaDB-shared MariaDB-devel ;
RUN pip3 install mariadb ;
COPY script.py /root/script.py
CMD /usr/bin/python3 /root/script.py