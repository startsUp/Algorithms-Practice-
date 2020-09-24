package amzn.maxUnits; // for VS code
import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    
    public long getMaxUnit(int num, ArrayList<Integer> boxes, int unitSize, ArrayList<Integer> unitsPerBox, long truckSize){
        Comparator<Integer[]> maxHeap = (Integer[] x, Integer[] y) -> y[1].compareTo(x[1]);
        PriorityQueue<Integer[]> pq = new PriorityQueue<>(maxHeap);

        for (int i = 0; i < unitSize; i++) {
            pq.add(new Integer[]{boxes.get(i), unitsPerBox.get(i)});
        }

        long ans=0;
        long capacity = truckSize;
        //print values
        while (!pq.isEmpty() || capacity != 0) {
            Integer[] next = pq.poll();
            System.out.println("Putting "+next[1]+" of #:"+Math.min(next[0],capacity));
            ans += next[1]*Math.min(next[0],capacity);
            capacity -= Math.min(next[0], capacity);
        }
        return ans;
    }
    public static void main(String[] args) {
       Solution s = new Solution(); 
       long ans = s.getMaxUnit(3, new ArrayList<Integer>(Arrays.asList(1,2,3)), 3, new ArrayList<Integer>(Arrays.asList(3,2,1)), 3);
       System.out.println("Answer => "+ans);
    }
}