from connection import cursor

# In general the database is operated on in an append only manner. 
# Pool certificates can be updated so that later certificates override earlier ones. In addition pools can retire. 
# Therefore to get the latest pool registration for every pool that is still valid:
cursor.execute("select * from pool_update " \
    "where registered_tx_id in (select max(registered_tx_id) from pool_update group by hash_id) " \
    "and not exists " \
      "( select * from pool_retire where pool_retire.hash_id = pool_update.hash_id " \
          "and pool_retire.retiring_epoch <= (select max (epoch_no) from block) " \
      ") ;")

print(cursor.fetchall())

# To include the pool hash in the query output
cursor.execute("select * from pool_update inner join pool_hash on pool_update.hash_id = pool_hash.id " \
    "where registered_tx_id in (select max(registered_tx_id) from pool_update group by hash_id) " \
    "and not exists " \
      "( select * from pool_retire where pool_retire.hash_id = pool_update.hash_id " \
          "and pool_retire.retiring_epoch <= (select max (epoch_no) from block) " \
          ") ;")

print(cursor.fetchall())