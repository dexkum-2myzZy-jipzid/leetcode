class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        let sBytes = Array(s.utf8).sorted(), tBytes = Array(t.utf8).sorted()
        return sBytes == tBytes
    }
}
