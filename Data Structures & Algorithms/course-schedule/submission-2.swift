class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var graph = Array(repeating: [Int](), count: numCourses)
        for p in prerequisites {
            let course = p[0]
            let prereq = p[1]

            graph[prereq].append(course)
        }

        var state = Array(repeating: 0, count: numCourses)

        /*
            0 = unvisited
            1 = currently exploring
            2 = completed (memoizes the result)
        */

        func dfs(_ cur: Int) -> Bool {
            if state[cur] == 2 {
                return true
            }

            if state[cur] == 1 {
                return false // loop found
            }

            // unvisited:
            state[cur] = 1
            for next in graph[cur] {
                if (dfs(next)) {
                    // state[cur] = 2
                } else {
                    return false
                }
            }

            state[cur] = 2
            return true
        }

        for startCourse in 0..<numCourses {
            if !dfs(startCourse) { return false }
        }

        return true
    }
}
