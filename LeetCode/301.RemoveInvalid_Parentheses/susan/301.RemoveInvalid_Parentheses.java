class Solution {
   
    List<String> res = new LinkedList<>();
  StringBuilder track = new StringBuilder();

  public List<String> removeInvalidParentheses(String s) {
      backtrack(s, 0);
     
      int maxLen = 0;
      for (String str : res) {
          maxLen = Math.max(maxLen, str.length());
      }
      HashSet<String> set = new HashSet<>();
      for (String str : res) {
          if (str.length() == maxLen) {
              set.add(str);
          }
      }
      return new LinkedList<>(set);
  }


  void backtrack(String s, int i) {
      if (i == s.length()) {
          if (isValid(track.toString())) {
              res.add(track.toString());
          }
          return;
      }
      char c = s.charAt(i);
      if (c != '(' && c != ')') {
         
          track.append(c);
          backtrack(s, i + 1);
          track.deleteCharAt(track.length() - 1);
      } else {
          
          track.append(c);
          backtrack(s, i + 1);
          
          track.deleteCharAt(track.length() - 1);

       
          backtrack(s, i + 1);
      }
  }

  boolean isValid(String s) {
      int left = 0;
      for (char c : s.toCharArray()) {
          if (c == '(') {
              left++;
          } else if (c == ')') {
              left--;
              if (left < 0) {
                
                  return false;
              }
          }
      }
     
      return left == 0;
  }  
}