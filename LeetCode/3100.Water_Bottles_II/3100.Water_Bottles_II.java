class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int res = numBottles, emptyBottles = numBottles;
        int exchangeFullBottle = 0;
        while (emptyBottles - numExchange >= 0) {
            emptyBottles -= numExchange;
            numExchange += 1;
            emptyBottles += 1;
            exchangeFullBottle += 1;
        }

        return res + exchangeFullBottle;
    }
}