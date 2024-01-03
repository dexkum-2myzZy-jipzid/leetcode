class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        UF uf = new UF(n);
        Map<Integer,Integer> map = new HashMap<>();

        for(int i= 0; i< n; i++){
            if(map.containsKey(nums[i])){
                continue;
            }
            map.put(nums[i],i);
            if(map.containsKey(nums[i]-1)){
                uf.union(i,map.get(nums[i]-1));
            }
            if(map.containsKey(nums[i]+1)){
                uf.union(i,map.get(nums[i]+1));
            }
        }

        return uf.findMax();
    }
}
class UF{
    int[] parent;
    int[] size;
    public UF(int n ){
        parent = new int[n];
        size = new int[n];

        for(int i = 0; i < n; i++){
            parent[i] = i;
        }

        Arrays.fill(size,1);
    }

    public int find(int x){
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x , int y){
        int rootX = find(x);
        int rootY = find(y);
        if( rootX == rootY) return;
        if(size[rootX] > size[rootY]){
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
        }else{
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        }
    }

    public int findMax(){
        int max = 0;
        for(int s : size){
            max = Math.max(s,max);
        }

        return max;
    }
}