public class Solution extends Relation {
    public int findCelebrity(int n) {

        if(n == 1){
            return 0;
        }

        LinkedList<Integer> q = new LinkedList<>();

        for(int i = 0; i< n; i++){
            q.addLast(i);
        }

        while(q.size()>1){
            int can = q.removeFirst();
            int other = q.removeFirst();

            if( knows(can,other) || !knows(other,can)){
                q.addLast(other);
            }else{
                q.addLast(can);
            }
        }

        int can = q.removeLast();

        for(int i = 0; i< n; i++){
            if(can == i){
                continue;
            }
            if(!knows(i,can) || knows(can, i)){
                return -1;
            }
        }

        return can;
        
    }
}