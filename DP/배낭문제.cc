//-----------------------------------------하향식-------------------------------------------------//
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

//-----------------------------------------상향식-------------------------------------------------//
	
#include<iostream>
#include<vector>

using namespace std;
int n,limit;

vector<int> w = {0};
vector<int> p = {0};
vector<vector<int>> DP;

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
	
	DP.resize(n+1,vector<int>(limit+1));
	
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= limit; j++) {
			if (w[i] <= j) {
				DP[i][j] = max(DP[i - 1][j], p[i] + DP[i - 1][j - w[i]]);
			}
			else {
				DP[i][j] = DP[i - 1][j];
			}
		}
	}
	cout << DP[n][limit] << endl;
}
