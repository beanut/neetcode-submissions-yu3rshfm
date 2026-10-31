class Solution {
    func maxSlidingWindow(_ nums: [Int], _ k: Int) -> [Int] {
    var deque: [Int] = []   // stores indices
    var head = 0            // logical front pointer
    var result: [Int] = []

    for i in 0..<nums.count {
        // Remove indices outside the current window
        while head < deque.count && deque[head] <= i - k {
            head += 1
        }

        // Remove smaller values from the back
        while deque.count > head,
              nums[deque[deque.count - 1]] <= nums[i] {
            deque.removeLast()
        }

        deque.append(i)

        // Start recording once the first full window exists
        if i >= k - 1 {
            result.append(nums[deque[head]])
        }
    }

    return result
}
}
