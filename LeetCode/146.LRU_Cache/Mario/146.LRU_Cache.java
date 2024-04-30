class LRUCache {

    private final int n; // capacity
    private final Map<Integer, Integer> map = new LinkedHashMap<>();

    public LRUCache(int capacity) {
        n = capacity;
    }

    public int get(int key) {
        // check key exist
        if (map.get(key) == null) {
            return -1;
        } else {
            // put key at the last of LinkedHashMap
            int val = map.get(key);
            map.remove(key);
            map.put(key, val);
            return val;
        }
    }

    public void put(int key, int value) {
        // check key exist
        if (map.get(key) != null) {
            map.remove(key);
            map.put(key, value);
        } else {
            // check if out of capacity
            if (map.size() == n) {
                // if full, evict the first element of LinkedHashMap
                int removedKey = map.keySet().iterator().next();
                map.remove(removedKey);
            }
            map.put(key, value);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */