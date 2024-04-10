public class Solution extends Relation {
    public int findCelebrity(int n) {
        int celebrity = 0;
        for (int i = 1; i < n; i++) {
            // i don't know celebrity, so celebrity is not a real celebrity
            // celebrity knows i, so celebrity is not a real celebrity
            //
            if (!knows(i, celebrity) || knows(celebrity, i)) {
                celebrity = i;
            } else {
                // i know celebrity and celebrity don't know i
                // so perhaps celebrity is real.
                // but i definitely not a celebrity
            }
        }

        // check celebrity is real
        for (int i = 0; i < n; i++) {
            if (i == celebrity)
                continue;
            if (!knows(i, celebrity) || knows(celebrity, i)) {
                return -1;
            }
        }
        return celebrity;
    }
}