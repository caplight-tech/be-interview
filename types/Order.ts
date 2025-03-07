import { UserId } from "./UserId"

export interface Order {
  id: string
  direction: "bid" | "offer"
  company: {
    name: string
    id: string
  }
  price: number
  targetSizeInMillions: number
  userId: UserId
  createdAt: Date
}
