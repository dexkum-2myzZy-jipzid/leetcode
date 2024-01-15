class Solution {
    public int myAtoi(String s) {
        if(s.trim().isEmpty()) return 0;

        int i = 0;
        while( s.charAt(i) == ' '){
              i++;
        }

        int sign = 1;

        if(s.charAt(i) == '-' || s.charAt(i) == '+'){
             sign = s.charAt(i++) == '-'? -1:1;
        }
        
        int base = 0;
        while(i< s.length() && s.charAt(i) >= '0'&& s.charAt(i) <= '9'){
            if(checkIntegerOverFlow(base,s.charAt(i)-'0')){
                return sign == 1? Integer.MAX_VALUE:Integer.MIN_VALUE;
            }
            base = base*10 + (s.charAt(i++) - '0');
        }

        return base*sign;
    }

    public boolean checkIntegerOverFlow(int base, int current){
        return base > Integer.MAX_VALUE/10 || (base== Integer.MAX_VALUE/10 && current > Integer.MAX_VALUE%10);
    }
}