class Solution {
    private List<String> res;

    public List<String> findStrobogrammatic(int n) {
        res = new ArrayList<>();

        if (n == 1) {
            return new ArrayList<>(List.of("0", "1", "8"));
        }

        char[] chs = { '0', '1', '6', '8', '9' };
        backtracking(chs, 0, n, new char[n]);
        return res;
    }

    private void backtracking(char[] chs, int index, int n, char[] arr) {
        if (index == n / 2) {
            generateString(index, n, arr);
            return;
        }

        for (int i = 0; i < chs.length; i++) {
            if (index == 0 && i == 0) {
                continue;
            }
            arr[index] = chs[i];
            backtracking(chs, index + 1, n, arr);
        }
    }

    private void generateString(int index, int n, char[] arr) {
        int dec = n % 2 == 0 ? 1 : 2;
        int start = n % 2 == 0 ? index : index + 1;
        for (int i = start; i < arr.length; i++) {
            if (arr[i - dec] == '6') {
                arr[i] = '9';
            } else if (arr[i - dec] == '9') {
                arr[i] = '6';
            } else {
                arr[i] = arr[i - dec];
            }
            dec += 2;
        }
        if (n % 2 == 0) {
            res.add(new String(arr));
        } else {
            for (char c : new char[] { '0', '1', '8' }) {
                arr[index] = c;
                res.add(new String(arr));
            }
        }

        return;
    }
}