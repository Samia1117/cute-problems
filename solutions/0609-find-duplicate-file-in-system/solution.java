class Solution {

    private List<List<String>> formatMap(HashMap<String, List<String>> map) {

        // Set<String> dups = map.entrySet().stream()
        //     .filter(entry -> entry.getValue().size() > 1)
        //     .map(entry -> entry.getKey()).collect(Collectors.toSet());

        List<Map.Entry<String, List<String>>> dups = map.entrySet().stream()
            .filter(entry -> entry.getValue().size() > 1)
            .collect(Collectors.toList());

            // .map(entry -> entry.getKey()).collect(Collectors.toSet());
        
        if (dups.size() == 0) {
            return new ArrayList<>();
        }

        // List<List<String>> result = withDuplicates.stream().
        // map(entry -> entry.getValue().stream().collect(Collectors.toList()) ).collect(Collector.toList());
        
        List<List<String>> result =  
        dups.stream().map(entry -> entry.getValue().stream().collect(Collectors.toList())).collect(Collectors.toList());
        /**
        map.entrySet().stream().filter(entry -> dups.contains(entry.getKey()))
            .map(entry -> entry.getValue().stream()
                .collect(Collectors.toList()))
            .collect(Collectors.toList());
         */
        return result;
    }
    public List<List<String>> findDuplicate(String[] paths) {
        /**
        ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

        -> [["root/a/1.txt", "root/c/3.txt"],
            ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]]
         */

         // 1. Create a hashmap<String, String> (content, path)
         // 2. Perform some string manipulation to format answer according to desired output. Output = format(map.values());

        HashMap<String, List<String>> map = new HashMap<>();

        for (String path: paths) {
            String[] parts = path.split(" ");
            String directory = parts[0];
            // System.out.println("directory = " + directory);

            for (int i = 1; i < parts.length; i++) {
                String part = parts[i];
                // System.out.println("Part = " + part);
                int contentLeftIdx = part.indexOf('(');
                int contentRightIdx = part.lastIndexOf(')');
                
                String content = part.substring(contentLeftIdx, contentRightIdx + 1);

                if (!map.containsKey(content)) {
                    map.put(content, new ArrayList<>());
                }
                // Add new filepath for this content
                String filepath = part.substring(0, contentLeftIdx);
                // System.out.println("Filepath before removing numeric = " + filepath);
                // Strip the "1./2./etc."
                filepath = directory + "/" + filepath.substring(0, filepath.length());
                // System.out.println("Filepath after removing numeric and prepending directory = " + filepath);

                map.get(content).add(filepath);

                // System.out.println("Map = " + map);
                
            }
        }

        return formatMap(map);
    }
}
