class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int i = 0, j = 0;
        for (String dir : commands) {
            if (dir.equals("UP")) {
                i -= 1;
            } else if (dir.equals("RIGHT")) {
                j += 1;
            } else if (dir.equals("DOWN")) {
                i += 1;
            } else if (dir.equals("LEFT")) {
                j -= 1;
            }
        }
        return (i * n) + j;
    }
}