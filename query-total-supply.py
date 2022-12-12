from connection import cursor

# This just queries the UTxO set for unspent transaction outputs. 
# It does not include staking rewards that have have not yet been withdrawn. 
# Before being withdrawn rewards exist in ledger state and not on-chain
cursor.execute("select sum (value) / 1000000 as current_supply from tx_out as tx_outer where " \
    "not exists " \
      "( select tx_out.id from tx_out inner join tx_in " \
          "on tx_out.tx_id = tx_in.tx_out_id and tx_out.index = tx_in.tx_out_index " \
          "where tx_outer.id = tx_out.id " \
      ") ;")

print(cursor.fetchone())