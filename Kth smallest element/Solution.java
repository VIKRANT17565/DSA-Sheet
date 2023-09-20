import java.util.*;

class Solution{
    public static int kthSmallest(int[] arr, int l, int r, int k) 
    { 
        //Your code here
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < arr.length; i++){
            pq.add(arr[i]);
        }
        // return pq.peek();
        for(int i = 0; i < k-1; i++){
            pq.poll();
        }
        
        return pq.peek();
    } 

    public static void main(String[] args){
        // TC 1
        int[] arr = {7, 10, 4, 3, 20, 15};
        int k = 3;
        System.out.println(kthSmallest(arr, 0, arr.length-1, k));

        // TC 2
        int[] arr2 = {7, 10, 4, 20, 15};
        int k2 = 4;
        System.out.println(kthSmallest(arr2, 0, arr2.length-1, k2));
        
    }
}
