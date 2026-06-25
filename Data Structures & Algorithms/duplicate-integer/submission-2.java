class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashMap<Integer,Integer> counter = new HashMap<>();
        for(int num: nums){
            if(counter.containsKey(num)){
                int curr_count = counter.get(num);
                counter.put(num,curr_count+1);

        }
        else{
            
            counter.put(num,1);
        }

        for(int count: counter.values()){
            if(count > 1){
                return true;
            }
        }
                
    }
    return false;
}
}
