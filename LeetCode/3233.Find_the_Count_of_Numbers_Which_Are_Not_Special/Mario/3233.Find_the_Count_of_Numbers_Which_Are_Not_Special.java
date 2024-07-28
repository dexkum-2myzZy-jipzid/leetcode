class Solution {
    public int nonSpecialCount(int l, int r) {
        // how many prime^2 in [l, r]
        int sqrtL = (int) Math.ceil(Math.sqrt(l));

        int count = 0;
        for (int i = sqrtL; i * i <= r; i++) {
            if (isPrime(i)) {
                count += 1;
            }
        }

        return r - l + 1 - count;
    }

    private boolean isPrime(int a) {
        if (a < 2)
            return false;
        for (int i = 2; i * i <= a; i++) {
            if (a % i == 0)
                return false;
        }
        return true;
    }
}