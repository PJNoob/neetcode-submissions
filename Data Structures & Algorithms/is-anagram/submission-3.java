class Solution {
    public boolean isAnagram(String s, String t) {

        // Checking the lenght of the string first before proceeding further
        if(s.length() != t.length())
            return false;

        HashMap<Character, Integer> c = new HashMap<>();

        // Storing frequency of the elements in the 1st String
        // 'toCharArray' is used to change String to charachter array
        // Use 'put' to enter elements in array
        for (char a : s.toCharArray()){
            c.put(a, c.getOrDefault(a,0) + 1);
        }

        // Deleting each value corresponding to the key in the HashMap
        for (char a : t.toCharArray()){
            c.put(a, c.getOrDefault(a,0) - 1);
        }
        
        // Chechking if all the values of each key is zero then it's a valid Anagram 
        // otherwise it's not a Valid Anagram, it could be more than 1 or in negative too
        for (char a : c.keySet()){
            if(c.get(a) != 0){
                return false;
            }
        }
        

        // Print keys and values
        for (char i : c.keySet()) {
        System.out.println("key: " + i + " value: " + c.get(i));
        }

        return true;
    }

    // public static void main(String[] args) {

    //     practice obj = new practice();

    //     // Example 1
    //     String s1 = "racecar";
    //     String t1 = "carrace";
    //     System.out.println();
    //     System.out.println(obj.isAnagram(s1, t1));  // true

    //     System.out.println();

    //     // Example 2
    //     String s2 = "jar";
    //     String t2 = "jam";
    //     System.out.println(obj.isAnagram(s2, t2));  // false

    //     // Example 3
    //     String s3 = "bbcc";
    //     String t3 = "ccbc";
    //     System.out.println(obj.isAnagram(s3, t3));  // false
    // }

}
