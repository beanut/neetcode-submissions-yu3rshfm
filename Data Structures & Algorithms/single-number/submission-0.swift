class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var count: [Int : Int] = [:]

        for n in nums {
            count[n, default: 0] += 1
        }

        for (n, c) in count {
            if c == 1 {
                return n
            }
        }
        return -1
    }
}
