class Solution {
  public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }

        vector<int> freq1(26, 0);
        vector<int> freq2(26, 0);

        for (int i = 0; i < s1.size(); i++) {
            freq1[s1[i] - 'a']++;
            freq2[s2[i] - 'a']++;
        }

        int L = 0;

        if (freq1 == freq2) {
            return true;
        }

        for (int R = s1.size(); R < s2.size(); R++) {
            if (freq2[s2[L] - 'a'] == 1) {
                freq2[s2[L] - 'a'] = 0;
            } else {
                freq2[s2[L] - 'a']--;
            }

            freq2[s2[R] - 'a']++;
            L++;

            if (freq1 == freq2) {
                return true;
            }
        }

        return false;
    }
};