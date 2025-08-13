public class MergeStrings {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int i = 0;
        while (i<word1.length() || i<word2.length()) {
            if (i<word1.length()){
                merged.append(word1.charAt(i));
            }
            if (i<word2.length()){
                merged.append(word2.charAt(i));
            }
            i++;
        }
        return merged.toString();
}
public static void main(String[] args) {
    MergeStrings m = new MergeStrings();
    String result = m.mergeAlternately("koira", "maukkakissa");
    System.out.println(result);
}
}
