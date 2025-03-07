import { db } from "./db"
import { ClosedTrade } from "./types/ClosedTrade"
import { Order } from "./types/Order"

// The following code is run when new orders and trades are placed in the system
// We wants to add 'Outlier Detection' to orders & trades that enriches the data point with an 'outlier check result'
// Outlier checks should look at an order's price and volume to determine if it is an outlier

const onOrderPlaced = (order: Order) => {
  //TODO: Implement outlier check

  db.save(order)
}

const onTradePlaced = (trade: ClosedTrade) => {
  //TODO: Implement outlier check

  db.save(trade)
}
