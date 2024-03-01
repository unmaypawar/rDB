# Documentation

**File Structure**

- databases
    - imdb
        - overall_schema.pickle
        - titles.csv
        - name.csv
        - crew.csv
        - rating.csv
    - sample_database_1
    - sample_database_2
- helper
    - make.py
    - shift.py
    - put.py
    - put.py
    - remove.py
    - modify.py
    - group.py
    - join.py
    - list.py
    - filter.py
    - query.py
- documentation
    - documentation.md
    - project_report.pdf
    - architecture.jpg
- main.py
- README.md
- Documentation.md

**Commands**

- make database *database_name.*
    - make database imdb.

- shift *database_name*.
    - shift imdb.

- make table *table_name ( schema )*.
    - make table rating (id*pk, rating, votes).

- list databases.

- list tables.

- put in *table_name (values according to schema)*.
    - put in rating (id= 1, rating= 8.0, votes= 1000).

- modify in *table_name (updated values according to schema)*.
    - modify in rating (id= 1, rating= 9.0, votes= 2000).

- remove in *table_name (key-value pair)*.
    - remove in rating (id= 1).

- print in *table_name (attributes you want to print)*.
    - print in rating (id, rating).

- import *file_name*.
    - import cmd.txt.
    
- query *(attributes you want to print), (conditions {optional}), (operations {optional}).*
    - query (name), (birthyear= 1974, profession= producer).
    - query (type, count.titles), (order= -1, first= 5), (group= type).
    - query (type, sum.votes), (order= 1, first= 10), (join= id.titles=id.rating, group= type).
    - query (type, avg.rating), (order= -1, skip= 2, first= 5), (join= id.titles=id.rating, group= type).
    - query (type, count.votes), (year= 2014, order= -1, first= 5), (join= id.titles=id.rating, group= type).