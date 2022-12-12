# Python-dbsync Starter-kit

This Starter-Kit is composed of a set of python scripts that query the [DB-sync](https://docs.cardano.org/cardano-components/cardano-db-sync/about-db-sync) instance running on [Demeter.run](https://demeter.run) cluster to generate different data analysis outputs from the ledger history.

We have implemented as an example some of the queries available in [input-output-hk
/interesting-queries.md](https://github.com/input-output-hk/cardano-db-sync/blob/master/doc/interesting-queries.md). This kit should be easy to extend with additional functionality. 

## Dev Environment

For executing the scripts in this starter kit you'll need access to a running [DB-sync](https://docs.cardano.org/cardano-components/cardano-db-sync/about-db-sync) instance in sync with a Node running on the network of your preference.

In case you don't want to install the required components yourself, you can use [Demeter.run](https://demeter.run) platform to create a cloud environment with access to common Cardano infrastructure. The following command will open this repo in a private, web-based VSCode IDE with access to a running DB-Sync instance in the preview network.

[![Code in Cardano Workspace](https://demeter.run/code/badge.svg)](https://demeter.run/code?repository=https://github.com/txpipe/python-dbsync-starter-kit.git&template=python)


## Running the scripts

Each script executes a simple query to DB-Sync and outputs the result in the terminal. 
The database connection is established in the file `connection.py`. 

We are going to use a library called [psycopg2](https://pypi.org/project/psycopg2/) for interfacing with the postgres SQL instance of DB-Sync.

The first step would be to install the dependencies. For doing that open a new terminal in the Development workspace and execute the following command:

```bash
pip install psycopg2-binary
```

As you might have noticed, we installed the psycopg2-binary package, which is the binary version of Psycopg2. What this means is that this version of the library comes with its own version of C libraries, namely liboq and libssl. For Psycopg2 beginners and most users, this version is perfectly fine

Now we are going to use the DB-Sync feature of [Demeter.run](https://demeter.run) for establishing a connection.

All the required inputs for establishing a connection are environment values available in the Workspace. We take advantage of this in `connection.py` where we establish the database connection. 

```python
conn = psycopg2.connect(database="cardanodbsync",
                        host=os.environ['DBSYNC_POSTGRESQL_HOSTNAME'],
                        user=os.environ["DBSYNC_POSTGRESQL_USER"],
                        password=os.environ["DBSYNC_POSTGRESQL_PASSWORD"],
                        port=os.environ["DBSYNC_POSTGRESQL_PORT"])

```

For running a script you can run it from the terminal with the `python3` command:

```bash
python3 query-current-valid-pools.py
```

Feel free to navigate the DB-Sync schema inside of the [Demeter.run](https://demeter.run) features list for extending this kit functionality with additional queries.

<img src="/assets/db-sync-schema.png" alt="schema">
