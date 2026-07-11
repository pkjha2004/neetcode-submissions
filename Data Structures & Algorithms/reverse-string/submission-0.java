class Solution {
    public void reverseString(char[] s) {
        int r = 0; int l  = s.length - 1;
        int mid = (l + r) / 2;
        while (r <= mid ){
            char temp = s[r];
            s[r] = s[l];
            s[l] = temp;
            r++;
            l--;
        }
        
    }
}