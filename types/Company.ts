export interface Company {
  id: string
  name: string
  logoUrl: string
  hqCountry: string
  marketpricePPS?: number
  lastFundingRoundPPS?: number
  lastFundingRoundDate?: Date
}
