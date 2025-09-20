class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        // email -> index
        Map<String, Integer> map = new HashMap<>();
        UnionFind uf = new UnionFind(accounts.size());

        for (int i = 0; i < accounts.size(); i++) {
            List<String> nameAndEmail = accounts.get(i);
            for (int j = 1; j < nameAndEmail.size(); j++) {
                String email = nameAndEmail.get(j);
                if (map.get(email) == null) {
                    map.put(email, i);
                } else {
                    uf.unionBySize(i, map.get(email));
                }
            }
        }

        // store representative -> emails
        Map<Integer, List<String>> emailMap = new HashMap<>();
        for (String email : map.keySet()) {
            int index = map.get(email);
            int req = uf.find(index);

            if (!emailMap.containsKey(req)) {
                emailMap.put(req, new ArrayList<>());
            }

            emailMap.get(req).add(email);
        }

        // Sort emails and add name
        List<List<String>> res = new ArrayList<>();
        for (Integer i : emailMap.keySet()) {
            String name = accounts.get(i).get(0);
            List<String> emails = emailMap.get(i);
            emails.sort(null);
            emails.add(0, name);
            res.add(emails);
        }

        return res;
    }
}

class UnionFind {
    private int[] parent;
    private int[] size;

    public UnionFind(int size) {
        this.parent = new int[size];
        this.size = new int[size];

        for (int i = 0; i < size; i++) {
            this.parent[i] = i;
            this.size[i] = 1;
        }
    }

    public int find(int x) {
        if (parent[x] == x) {
            return x;
        }

        return find(parent[x]);
    }

    public void unionBySize(int a, int b) {
        int rootA = find(a), rootB = find(b);
        if (rootA != rootB) {
            if (size[rootA] < size[rootB]) {
                parent[rootA] = rootB;
                size[rootB] += size[rootA];
            } else {
                parent[rootB] = rootA;
                size[rootA] += size[rootB];
            }
        }
    }
}