class Solution {

    private HashMap<Integer, List<Node>> adjDict = new HashMap<>();
    private int minTime = -1;
    private HashMap<Integer, Integer> minTimeMap = new HashMap<>();

    static class Node {
        Integer id;
        Integer weight;
        Integer cost = -1;  // not set

        public Node(int id, int weight, int cost) {
            this.id = id;
            this.weight = weight;
            this.cost = cost;
        }

        void setWeight(int weight) {
            this.weight = weight;
        }

        public void updateCost(int cost) {
            if (this.cost == -1) {
                this.cost = cost;
            } else if (this.cost > cost) {
                this.cost = cost;
            }
        }

        public int getCost() {
            return this.cost;
        }

        public int getWeight() {
            return this.weight;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d, %d)", id, weight, cost);
        }
    }

    /**
    private void bfs(int k) {
        // loop through adjacency dictionary and populate the nodes using bfs, starting at node k
        LinkedList<Node> queue = new LinkedList<>();
        queue.addLast(new Node(k, 0, 0)); // min cost of k is 0  

        HashSet<Integer> nodes = new HashSet<>();

        while (!queue.isEmpty()) {
            Node currNode = queue.poll();
            // System.out.println("Current node = " + currNode);
            nodes.add(currNode.id);

            int parentCost = currNode.getCost();

            if (adjDict.containsKey(currNode.id)) {
                // iterate through all neighbors
                for (Node neighbor: adjDict.get(currNode.id)) {
                    int neighborCost = parentCost + neighbor.getWeight(); 

                    // neighbor.cost is cost of going from currNode to neighbor
                    neighbor.updateCost(neighborCost);
                    if (this.minTime < neighborCost) {
                        this.minTime = neighborCost;
                    }
                    queue.addLast(neighbor);
                }
            } else {
                continue;
            }
            // System.out.println("Queue = " + queue);
        }
    }
    */

    void dfs(int currNodeId, int currWeight) { // currWeight = time it took to get to currNodeId from all predecessors in the call flow

        // System.out.println("Current node id = " + currNodeId);
        int currMinWeight = minTimeMap.getOrDefault(currNodeId, -1);
        if (currMinWeight != -1 && currMinWeight < currWeight) {
            return;
        }
        minTimeMap.put(currNodeId, currWeight);

        if (!adjDict.containsKey(currNodeId)) {
            // no further expansion possible; terminal node
            return;
        }

        List<Node> neighbors = adjDict.get(currNodeId);
        for (Node neighbor: neighbors) {
            dfs(neighbor.id, currWeight + neighbor.weight); // neighbor.weight is the time taken to go from currNode to neighbor
        }
    }

    void dijkstra(int k) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
        pq.offer(new Node(k, 0, -1));

        while (!pq.isEmpty()) {
            // System.out.println("pq = " + pq);
            Node node = pq.remove();
            int currMinWeight = minTimeMap.getOrDefault(node.id, -1);
            if (currMinWeight != -1 && currMinWeight < node.weight) {
                continue;
            }
            minTimeMap.put(node.id, node.weight);

            if (adjDict.containsKey(node.id)) {
                for (Node neighbor: adjDict.get(node.id)) {
                    int newWeight = node.weight + neighbor.weight;
                    int neighWeight = minTimeMap.getOrDefault(neighbor.id, -1);
                    if (neighWeight == -1 || neighWeight > newWeight) {
                        minTimeMap.put(neighbor.id, newWeight);
                        neighbor.setWeight(newWeight);
                        pq.add(neighbor);
                    }
                }
            }
        }
    }

    void buildGraph(int[][] times, int k, int n) {

        int size = times.length;
        for (int i = 0; i < size; i++) {
            int[] triple = times[i];
            int source = triple[0];
            int dest = triple[1];
            int weight = triple[2];

            // Not bidirectional
            if (!adjDict.containsKey(source)) {
                adjDict.put(source, new ArrayList<Node>());
            }
            adjDict.get(source).add(new Node(dest, weight, -1));
        }
        // System.out.println("Adj Dict = " + adjDict);
    }
    public int networkDelayTime(int[][] times, int n, int k) {
        buildGraph(times, n, k);
        // bfs(k);
        // return this.minTime;
        // dfs(k, 0);

        dijkstra(k);
        // System.out.println("minTimeMap = " + minTimeMap);
        if (minTimeMap.size() != n) {
            return -1;
        }
        return minTimeMap.values().stream().max(Integer::compare).get();
    }
}
