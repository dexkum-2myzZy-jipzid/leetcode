func reversePrefix(word string, ch byte) string {
	j := -1
	for i := range word {
		if word[i] == ch {
			j = i
			break
		}
	}

	if j == -1 {
		return word
	}

	result := make([]byte, 0, len(word))
	for i := j; i >= 0; i-- {
		result = append(result, word[i])
	}
	result = append(result, word[j+1:]...)

	return string(result)
}