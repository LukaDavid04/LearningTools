class Solution {
    public static int romanToInt(String s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (String.valueOf(s.charAt(i)).equals("I")){
                if (i + 1 < s.length()) {
                    if (String.valueOf(s.charAt(i + 1)).equals("V")) {
                        sum += 4;
                        i++;
                    }
                    else if (String.valueOf(s.charAt(i + 1)).equals("X")) {
                        sum += 9;
                        i++;
                    }
                    else{
                        sum += 1;                    
                    }
                }
                else{
                        sum += 1;                    
                }
                
            }
            else if (String.valueOf(s.charAt(i)).equals("V")){
                sum += 5;                
            }
            else if (String.valueOf(s.charAt(i)).equals("X")){
                if (i + 1 < s.length()) {
                    if (String.valueOf(s.charAt(i + 1)).equals("L")) {
                        sum += 40;
                        i++;
                    }
                    else if (String.valueOf(s.charAt(i + 1)).equals("C")) {
                        sum += 90;
                        i++;
                    }
                    else{
                        sum += 10;                    
                    }
                }
                else{
                    sum += 10;                    
                }
            }
            else if (String.valueOf(s.charAt(i)).equals("L")){
                sum += 50;
            }
            else if (String.valueOf(s.charAt(i)).equals("C")){
                if (i + 1 < s.length()) {
                    if (String.valueOf(s.charAt(i + 1)).equals("D")) {
                        sum += 400;
                        i++;
                    }
                    else if (String.valueOf(s.charAt(i + 1)).equals("M")) {
                        sum += 900;
                        i++;
                    }
                    else{
                        sum += 100;                    
                    }
                }
                else{
                    sum += 100;                    
                }
            }
            else if (String.valueOf(s.charAt(i)).equals("D")){
                sum += 500;              
            }
            else if (String.valueOf(s.charAt(i)).equals("M")){
                sum += 1000;
                
            }
        }
        return sum;
    }
}