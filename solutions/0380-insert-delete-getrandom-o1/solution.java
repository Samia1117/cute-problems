import java.util.Random;

class RandomizedSet {

    // private final LinkedHashSet<Integer> linkedHashSet;      // <Number, NumberIdx>
    private final HashMap<Integer, Integer> linkedHashSet;      // <Number, NumberIdx>
    // private final LinkedList<Integer> ll = new LinkedList<>();
    private ArrayList<Integer> alist = new ArrayList<>();
    private int length = 0;   
    private final Random random = new Random();

    public RandomizedSet() {
        // this.linkedHashSet = new LinkedHashSet<>();
        this.linkedHashSet = new HashMap<>();

    }
    
    public boolean insert(int val) {
        if (this.linkedHashSet.containsKey(val)) {
            return false;
        } else {
            // this.linkedHashSet.add(val);
            this.linkedHashSet.put(val, this.length);
            this.alist.add(val);

            this.length++;
            return true;
        }
    }
    
    public boolean remove(int val) {
        if (!this.linkedHashSet.containsKey(val)) {
            return false;
        } else {
            // this.linkedHashSet.remove(val);
            int reqIndex = linkedHashSet.get(val);
            int lastVal = alist.get(this.length-1);

            alist.set(reqIndex, lastVal);
            linkedHashSet.put(lastVal, reqIndex);

            alist.remove(this.length-1);
            linkedHashSet.remove(val);

            length--;

            return true;
        }
    }
    
    public int getRandom() {
        
        int randomIdx = this.random.nextInt(this.length);
        // System.out.println("Linked list = " + ll);
        return alist.get(randomIdx);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
