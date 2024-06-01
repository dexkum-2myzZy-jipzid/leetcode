class Solution {
    public int reverse(int x) {
        // y store reverse x
        int y = 0;

        // using queue to store x digits
        Queue<Integer> queue = new LinkedList<>();
        while (x != 0) {
            int digit = x % 10;
            queue.offer(digit);
            x /= 10;
        }

        // remove leading zeros
        while (!queue.isEmpty() && queue.peek() == 0) {
            queue.poll();
        }

        // reverse
        int max = Integer.MAX_VALUE, min = Integer.MIN_VALUE;
        while (!queue.isEmpty()) {
            int digit = queue.poll();

            if (y > max / 10 || y == max / 10 && digit > 7) {
                return 0;
            }
            if (y < min / 10 || y == min / 10 && digit < -8) {
                return 0;
            }
            y = 10 * y + digit;
        }

        return y;
    }
}