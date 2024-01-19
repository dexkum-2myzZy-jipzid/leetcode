class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length; int n = nums2.length;
        int x = m + n;
        if(x % 2 == 1){
            return solve(nums1,nums2,x/2,0,m-1,0,n-1);
        }else{
            return (double)(solve(nums1,nums2,x/2,0,m-1,0,n-1) + solve(nums1,nums2, x/2-1,0,m-1,0,n-1))/2;
        }
    }

    public int solve(int[] A, int[] B, int k, int start1, int end1, int start2, int end2){
        if(start1 > end1){
            return B[k-start1];
        }
        if(start2 > end2){
            return A[k-start2];
        }

        int middle1 = (start1+end1)/2;
        int middle2 = (start2+end2)/2;
        int value1 = A[middle1];
        int value2 = B[middle2];

        if(middle1 + middle2 < k){
            if( value1 > value2){
                return solve(A,B,k,start1,end1,middle2+1,end2);
            }else{
                return solve(A,B,k,middle1+1,end1,start2,end2);
            }
        }else{
            if( value1> value2){
                return solve(A,B,k,start1,middle1 -1, start2, end2);
            }else{
                return solve(A,B,k,start1,end1,start2,middle2 -1);
            }
        }
    }
}