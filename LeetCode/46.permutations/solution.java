class Solution {
    public List<List<Integer>> permute(int[] nums) {
       List<List<Integer>> res = new ArrayList<>();
       List<Integer> track = new ArrayList<>();
       boolean[] used = new boolean[nums.length];
       Arrays.sort(nums);
       bfs(nums,used,track,res);
       return res;
    }

    public void bfs(int[] nums, boolean[] used, List<Integer> track, List<List<Integer>> res){
        if(track.size() == nums.length){
            res.add(new ArrayList<>(track));
            return;
        }

        for(int i = 0; i< nums.length; i++){
            if(used[i]){
                continue;
            }
            track.add(nums[i]);
            used[i] = true;
            bfs(nums,used,track,res);
            used[i] = false;
            track.remove(track.size()-1);
        }
    }
}