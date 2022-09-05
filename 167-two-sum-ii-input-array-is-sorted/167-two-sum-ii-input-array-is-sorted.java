class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer > hash = new HashMap<>();
        for (int i = 0; i < numbers.length; i++){
            int compliment = target - numbers[i];
            if (hash.containsKey(numbers[i])) return new int[] {hash.get(numbers[i])+1, i+1};
            hash.put(compliment, i);
        }
        return new int[] {0, 0};
    }
}