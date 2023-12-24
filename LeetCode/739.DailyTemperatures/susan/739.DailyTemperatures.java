class Solution {
    public int[] dailyTemperatures(int[] temperatures) {

        int n = temperatures.length;
        int[] res = new int[n];
        Stack<Integer> num = new Stack<>();
        Stack<Integer> items = new Stack<>();

        for(int i = n-1; i>=0; i--){
            while(!num.isEmpty()&& num.peek()<= temperatures[i]){
                num.pop();
                items.pop();
            }
            res[i] = num.isEmpty()? 0: (items.peek()-i);
            
            num.push(temperatures[i]);
            items.push(i);
        }

        return res;
        
    }
}