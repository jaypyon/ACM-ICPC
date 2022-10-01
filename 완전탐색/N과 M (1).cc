#include<iostream>
#include<vector>
using namespace std;
int N,M;
vector<bool> isInNow;
vector<int> nmArr;
void getNM(int depth, vector<bool> status, vector<int> now) {
	if (depth >= M) { for (auto i : now) { cout << i << " "; }cout << "\n";return; }
	for (int i = 0; i < N; i++) {
		if (status[i] == false) {
			//cout << i + 1 << " ";
			now.push_back(i + 1);
			status[i] = true;
			getNM(depth + 1, status, now);
			now.pop_back();
			status[i] = false;
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	
	isInNow.resize(N, false);
	getNM(0, isInNow, nmArr);
}
