import java.util.*;

class Solution {
    /**
     * @param nums1
     * @param m
     * @param nums2
     * @param n
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if ( n <= 0 ) {
            return;
        }
		int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while( j >= 0 ) {
            if( i >= 0 && nums1[i] > nums2[j] ) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
    }

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] s1_nums1 = {1,2,3,0,0,0,0};
		int s1_m = 3;
		int[] s1_nums2 = {2,5,6,7};
		int s1_n = 4;
		sol.merge( s1_nums1, s1_m, s1_nums2, s1_n );
		System.out.println( "out: " + Arrays.toString( s1_nums1 ) );

		int[] s2_nums1 = {1,2,3,0, 0};
		int s2_m = 3;
		int[] s2_nums2 = {2,5,6};
		int s2_n = 2;
		sol.merge( s2_nums1, s2_m, s2_nums2, s2_n );
		System.out.println( "out: " + Arrays.toString( s2_nums1 ) );

		int[] s3_nums1 = {1};
		int s3_m = 1;
		int[] s3_nums2 = {};
		int s3_n = 0;
		sol.merge( s3_nums1, s3_m, s3_nums2, s3_n );
		System.out.println( "out: " + Arrays.toString( s3_nums1 ) );

		int[] s4_nums1 = {0};
		int s4_m = 0;
		int[] s4_nums2 = {1};
		int s4_n = 1;
		sol.merge( s4_nums1, s4_m, s4_nums2, s4_n );
		System.out.println( "out: "+Arrays.toString( s4_nums1 ) );
	}
}

