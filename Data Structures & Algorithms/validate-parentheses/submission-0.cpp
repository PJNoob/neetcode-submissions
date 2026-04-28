class Solution {
  public:
    bool isValid(string s) {
        stack<char> bracketStack;

        for (char ch : s) {
            if (ch == ')' || ch == '}' || ch == ']') {
                if (bracketStack.empty() || !isMatchingPair(bracketStack.top(), ch)) {
                    return false;
                }

                bracketStack.pop();
            } else {
                bracketStack.push(ch);
            }
        }

        return bracketStack.empty();
    }

  private:
    bool isMatchingPair(char opening, char closing) {
        return (opening == '(' && closing == ')') ||
               (opening == '{' && closing == '}') ||
               (opening == '[' && closing == ']');
    }
};