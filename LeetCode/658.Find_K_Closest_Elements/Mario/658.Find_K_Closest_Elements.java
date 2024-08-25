class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        // find the num bigger than or equal x, but most close to x
        int index = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= x) {
                index = i;
                break;
            }
        }

        List<Integer> result = new ArrayList<>();

        // not find close num
        if (index == -1) {
            for (int i = arr.length - 1; i >= arr.length - k; i--) {
                result.add(arr[i]);
            }
        } else {
            int count = 0;
            int left = index - 1, right = index;
            while (count < k) {
                if (left >= 0 && right < arr.length) {
                    if (x - arr[left] <= arr[right] - x) {
                        result.add(arr[left]);
                        left -= 1;
                    } else {
                        result.add(arr[right]);
                        right += 1;
                    }
                } else if (left >= 0) {
                    result.add(arr[left]);
                    left -= 1;
                } else if (right < arr.length) {
                    result.add(arr[right]);
                    right += 1;
                }
                count += 1;
            }
        }
        Collections.sort(result);
        return result;
    }
}

// Binary Search
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        // Initialize binary search bounds
        int left = 0;
        int right = arr.length - k;

        // Binary search against the criteria described
        while (left < right) {
            int mid = (left + right) / 2;
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // Create output in correct format
        List<Integer> result = new ArrayList<Integer>();
        for (int i = left; i < left + k; i++) {
            result.add(arr[i]);
        }

        return result;
    }
}