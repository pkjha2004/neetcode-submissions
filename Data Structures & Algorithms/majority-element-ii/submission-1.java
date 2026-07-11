class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int k = nums.length/3;
        ArrayList<Integer> arr = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num : nums){
                map.put(num, map.getOrDefault(num,0) +1 );
            
        }
        for(Map.Entry<Integer, Integer> entry :map.entrySet()){
          
                if (entry.getValue() >  k){
                    arr.add(entry.getKey());
                }
            
        }
        return arr;
    }
}