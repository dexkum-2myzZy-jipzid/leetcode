class TimeMap {

    // key -> [value, timestamp]
    private Map<String, ArrayList<Pair<Integer, String>>> map;

    public TimeMap() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        ArrayList<Pair<Integer, String>> array = map.getOrDefault(key, new ArrayList<Pair<Integer, String>>());
        array.add(new Pair(timestamp, value));
        map.put(key, array);
    }

    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }

        // first element in array is bigger than timestamp
        if (timestamp < map.get(key).get(0).getKey()) {
            return "";
        }

        ArrayList<Pair<Integer, String>> array = map.get(key);
        int left = 0, right = array.size();

        while (left < right) {
            int mid = (left + right) >> 1;
            if (array.get(mid).getKey() <= timestamp) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        if (right == 0) {
            return "";
        }

        return map.get(key).get(right - 1).getValue();
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */