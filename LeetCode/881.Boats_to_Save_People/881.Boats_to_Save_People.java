class Solution {
    // two points
    // count : store num of boats
    // at most two people
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0, right = people.length - 1;
        int count = 0;

        while (left <= right) {
            if (people[left] + people[right] > limit) {
                right -= 1;
            } else {
                left += 1;
                right -= 1;
            }
            count += 1;
        }

        return count;
    }
}