from connection import cursor

cursor.execute("select slot_no from block where block_no is not null " \
    "order by block_no desc limit 1 ;")

print(cursor.fetchone())