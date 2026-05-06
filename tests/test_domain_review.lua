package.path = "src/?.lua;" .. package.path
local review = require("domain_review")

local item = { signal = 78, slack = 38, drag = 19, confidence = 59 }
assert(review.score(item) == 196)
assert(review.lane(item) == "ship")
