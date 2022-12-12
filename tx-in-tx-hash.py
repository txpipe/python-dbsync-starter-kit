from connection import cursor

# Transaction inputs for specified transaction hash:
cursor.execute("select tx_out.* from tx_out " \
    "inner join tx_in on tx_out.tx_id = tx_in.tx_out_id " \
    "inner join tx on tx.id = tx_in.tx_in_id and tx_in.tx_out_index = tx_out.index " \
    r"where tx.hash = '\xb44bfcebd25b68d82ac6aedf2d5d72390cb191a1359120fa9383a4e15d3e68f7' ;")

print(cursor.fetchall())