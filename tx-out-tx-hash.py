from connection import cursor

# Transaction outputs for specified transaction hash:
cursor.execute("select tx_out.* from tx_out inner join tx on tx_out.tx_id = tx.id " \
    r"where tx.hash = '\xb44bfcebd25b68d82ac6aedf2d5d72390cb191a1359120fa9383a4e15d3e68f7' ;")

print(cursor.fetchall())