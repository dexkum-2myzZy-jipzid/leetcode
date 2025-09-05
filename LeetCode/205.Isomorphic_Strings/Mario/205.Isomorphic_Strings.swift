class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        // edge case
        if s.count != t.count {
            return false
        }

        var sMapping: [Character: Character] = [:]
        var tMapping: [Character: Character] = [:]

        for (ss, tt) in zip(Array(s), Array(t)) {
            // check s -> t
            if let a = sMapping[ss], a != tt {
                return false
            }
            // check t -> s
            if let b = tMapping[tt], b != ss {
                return false
            }

            // build s->t && t -> s
            if sMapping[ss] == nil && tMapping[tt] == nil {
                sMapping[ss] = tt
                tMapping[tt] = ss
            }
        }

        return true
    }
}

class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        // edge case
        if s.count != t.count {
            return false
        }

        var mapST = Array(repeating: -1, count: 256)
        var mapTS = Array(repeating: -1, count: 256)

        for (ss, tt) in zip(s.utf8, t.utf8) {
            let si = Int(ss), ti = Int(tt)
            // build mapping
            if mapST[si] == -1 && mapTS[ti] == -1 {
                mapST[si] = ti
                mapTS[ti] = si
            } else if mapST[si] != ti || mapTS[ti] != si {
                return false
            }
        }

        return true
    }
}
