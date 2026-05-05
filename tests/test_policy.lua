package.path = "src/?.lua;" .. package.path
local policy = require("policy")

local signal_case_1 = { demand = 65, capacity = 81, latency = 19, risk = 11, weight = 11 }
assert(policy.score(signal_case_1) == 113)
assert(policy.classify(signal_case_1) == "review")
local signal_case_2 = { demand = 71, capacity = 101, latency = 12, risk = 10, weight = 6 }
assert(policy.score(signal_case_2) == 163)
assert(policy.classify(signal_case_2) == "accept")
local signal_case_3 = { demand = 96, capacity = 98, latency = 9, risk = 13, weight = 11 }
assert(policy.score(signal_case_3) == 222)
assert(policy.classify(signal_case_3) == "accept")
