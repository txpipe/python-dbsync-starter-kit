from connection import cursor

# Transaction fee for specified transaction hash in the preview network
cursor.execute("select tx.id, tx.fee from tx where " \
 r"tx.hash = '\xb44bfcebd25b68d82ac6aedf2d5d72390cb191a1359120fa9383a4e15d3e68f7';")

print(cursor.fetchone())