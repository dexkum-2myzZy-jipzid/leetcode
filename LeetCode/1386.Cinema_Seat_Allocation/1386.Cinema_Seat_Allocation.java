class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        // only 3 case in every row, left, middle, right
        // map, key: row, value: set(2, 3, 8)
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int[] e : reservedSeats) {
            int row = e[0], seat = e[1];
            Set<Integer> seats = map.getOrDefault(row, new HashSet<>());
            seats.add(seat);
            map.put(row, seats);
        }

        // no reservedSeats have 2 cases
        int result = (n - map.size()) * 2;
        for (int row : map.keySet()) {
            Set<Integer> set = map.get(row);
            int count = 0;
            if (!set.contains(2) && !set.contains(3) && !set.contains(4) && !set.contains(5)) {
                count += 1;
            }
            if (!set.contains(6) && !set.contains(7) && !set.contains(8) && !set.contains(9)) {
                count += 1;
            }
            if (count == 0 && !set.contains(6) && !set.contains(7) && !set.contains(4) && !set.contains(5)) {
                count = 1;
            }
            result += count;
        }

        return result;
    }
}