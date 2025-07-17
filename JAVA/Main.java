

public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6};

        // Use nums.length, not NumericShaper.length, and no colon after for(...)
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }
    }
}
