import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;

public class GroupoAnagrams{

    public List<List<String>> groupAnagrams(String[] words){
        if(words == null || words.length == 0) return Collection.emptyList();

        Map<String, List<String>> anagramMap = new buildAnagramMap(words);
        return new ArrayList<>(anagramMap.values());
    }

    private Map<String, List<String>> buildAnagramMap(String[] words) {
        Map<String, List<String>> map = new HashMap<>();
        for ( String word : words ) {
            String hash = getAnagramHash(word);
            if(!map.containsKey(hash)) {
                map.put(hash, new ArrayList<>());
            }
            map.get(hash).add(word);
        }
        return map;
    }

    private String getAnagramHash(String s) {
        int[] letterCount = new int[26];
        for( int c : s.toCharArray()) {
            letterCount [c-'a']++;
        }
        return Arrays.toString(letterCount);
    }
}