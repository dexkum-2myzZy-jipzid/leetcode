func addBinary(a string, b string) string {
    var builder strings.Builder
    i, j := len(a)-1, len(b)-1
    plus, sum := 0,0

    for i>= 0 || j >= 0{
        sum = plus

        if i >= 0 {
            sum += int(a[i] - '0')
            i -= 1
        }

        if j >= 0 {
            sum += int(b[j] - '0')
            j -= 1
        }

        if sum > 1 {
            plus = 1
        }else{
            plus = 0
        }

        builder.WriteString(fmt.Sprintf("%d", sum%2))
    }

    if plus > 0 {
        builder.WriteString(fmt.Sprintf("%d", plus))
    }

    return reverseString(builder.String())
}

func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}