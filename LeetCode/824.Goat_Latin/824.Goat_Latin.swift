class Solution {
    func toGoatLatin(_ sentence: String) -> String {
        // 1. begin with 'a', 'e', 'i', 'o', or 'u', append "ma"
        // 2. begin with consonant, remove first and append end, add "ma"
        // 3. add "a" to the end, based on its index, index is 1-based
        let vowel: Set<String> = Set(["a", "e", "i", "o", "u"])
        let words = sentence.split(separator: " ")

        var res: [String] = []
        var suffix = "a"
        for (i, w) in words.enumerated() {
            var seg = Array(w)
            let first = String(seg[0]).lowercased()
            if !vowel.contains(first) {
                let removed = seg.remove(at: 0)
                seg.append(removed)
            }

            res.append(String(seg) + "ma" + suffix)
            suffix += "a"
        }

        return res.joined(separator: " ")
    }
}
