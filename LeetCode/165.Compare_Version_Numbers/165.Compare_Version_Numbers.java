class Solution {
    // convert versions to split(".") 1.0.1 => String[1, 0 ,1]
    // string => int[]
    // two points, compare from 0 -> min(len(version1), len(version2));
    // result = 1 version1 > version2
    // result = -1 version1 < version2
    // result = 0, still continue compare left part, if left part is all 0, so,
    // equal, return 0
    // if not version which has left part > another version
    public int compareVersion(String version1, String version2) {
        String[] version1Strs = version1.split("\\.");
        String[] version2Strs = version2.split("\\.");

        int minLen = Math.min(version1Strs.length, version2Strs.length);
        for (int i = 0; i < minLen; i++) {
            String str1 = version1Strs[i];
            String str2 = version2Strs[i];

            int result = compareSegmentVersion(str1, str2);
            if (result != 0) {
                return result;
            }
        }

        // left part of version1 or version 2;
        int j = minLen;// index no need plus 1
        while (j < version1Strs.length) {
            String str1 = version1Strs[j];
            int str1Int = chars2Int(str1.toCharArray());
            if (str1Int > 0) {
                return 1;
            }
            j += 1;
        }

        while (j < version2Strs.length) {
            String str2 = version2Strs[j];
            int str2Int = chars2Int(str2.toCharArray());
            if (str2Int > 0) {
                return -1;
            }
            j += 1;
        }

        return 0;
    }

    private int compareSegmentVersion(String str1, String str2) {
        // convert str to char to int
        char[] chs1 = str1.toCharArray();
        char[] chs2 = str2.toCharArray();

        int str1Int = chars2Int(chs1);
        int str2Int = chars2Int(chs2);

        if (str1Int < str2Int) {
            return -1;
        } else if (str1Int > str2Int) {
            return 1;
        } else {
            return 0;
        }
    }

    // left -> right
    private int chars2Int(char[] chs) {
        int num = 0;
        // remove zeros
        int i = 0;
        while (i < chs.length && chs[i] == '0') {
            i += 1;
        }

        for (int j = i; j < chs.length; j++) {
            num += (num * 10 + chs[j] - '0');
        }

        return num;
    }
}