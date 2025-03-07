import { UserId } from "./UserId"

export interface ClosedTrade {
  id: string
  company: {
    name: string
    id: string
  }
  price: number
  numShares: number
  userId: UserId
  transactionDate: Date
  createdAt: Date
}
