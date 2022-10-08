#include<iostream>
#include<vector>

using namespace std;
int n,limit;

vector<int> w = {};
vector<int> p = {};
vector<vector<int>> DP;
int search(int index, int nowW) {
	if (nowW > limit) return -p[index-1];
	if (index >= n) return 0;
	if (DP[index][nowW]>0) return DP[index][nowW];
	return DP[index][nowW] = max(search(index + 1, nowW), search(index + 1, nowW + w[index]) + p[index]);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> limit;
	for (int i = 0;i < n;i++) {
		int f, s;
		cin >> f >> s;
		w.push_back(f);
		p.push_back(s);
	}
	
	DP.resize(101, vector<int>(100001));
	
	
	int result = search(0, 0);
	
	cout << result << endl;
}
