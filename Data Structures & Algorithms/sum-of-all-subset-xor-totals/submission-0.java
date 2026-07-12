class Solution {
    public int subsetXORSum(int[] nums) {
        return backtrack(nums,  0 , 0);
    }
        private int backtrack(int[] nums, int i, int curr_xor){
            if(i == nums.length){
                return curr_xor;}
            
            int include = backtrack(nums, i+1, curr_xor ^ nums[i]);
            int exclude = backtrack(nums, i+1, curr_xor);

            return include + exclude;

            }   
    }
