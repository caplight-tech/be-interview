import { ClosedTrade } from "./types/ClosedTrade"
import { Company } from "./types/Company"
import { Order } from "./types/Order"
import fs from "fs"

const save = (order: Order | ClosedTrade) => {
  //... save to database
  console.log("Saved")
}

const getOrders = (): Promise<Order[]> => {
  const orders = JSON.parse(
    fs.readFileSync("data/generated_orders.json", "utf8")
  )
  return Promise.resolve(orders)
}

const getTrades = (): Promise<ClosedTrade[]> => {
  const trades = JSON.parse(
    fs.readFileSync("data/generated_trades.json", "utf8")
  )
  return Promise.resolve(trades)
}

const getCompanies = (): Promise<Company[]> => {
  const companies: Company[] = JSON.parse(
    fs.readFileSync("data/generated_companies.json", "utf8")
  )
  return Promise.resolve(companies)
}

const getCompany = async (id: string): Promise<Company | undefined> => {
  const companies = await getCompanies()
  return Promise.resolve(
    companies.find((company: Company) => company.id === id)
  )
}

export const db = {
  getCompanies: getCompanies,
  getCompany: getCompany,
  getOrders: getOrders,
  getTrades: getTrades,
  save: save,
}
