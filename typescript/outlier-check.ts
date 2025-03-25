interface OutlierFields {
  history?: OutlierCheckResult[]
  currentSummary?: OutlierCheckResult
}

type UserId = string

export type OutlierCheckResult =
  | { tag: "auto flagged"; date: Date; _flaggedReasons?: string[] }
  | { tag: "unflagged"; date?: Date | null }
  | { tag: "manually flagged"; flaggedBy: UserId; date: Date }
  | { tag: "outlier acknowledged"; user: UserId; date: Date }
  | { tag: "approved"; user: UserId; date: Date }
  | { tag: "cannot check"; date: Date }
