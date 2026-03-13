class Solution {
    static char[] arr;
    static int top;
    
    public static void push(char x) {
        arr[top++] = x;
    }

    public static char pop() {
        return arr[--top];
    }

    public static boolean isEmpty() {
        return top == 0;
    }

    public static int peek() {
        return arr[top - 1];
    }

    public boolean isValid(String s) {
        arr = new char[s.length()];
        top = 0;
        for(char i : s.toCharArray()){
            if (i == '(' || i == '{' || i == '[') {
                push(i);
            }
            else {

                if (isEmpty()) return false;

                if (i == ')' && peek() == '(') {
                    pop();
                }
                else if (i == '}' && peek() == '{') {
                    pop();
                }
                else if (i == ']' && peek() == '[') {
                    pop();
                }
                else {
                    return false;
                }
            }
        }
        return isEmpty();
    }
}