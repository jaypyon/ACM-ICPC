#include<iostream>
#include<vector>
using namespace std;
int N,M,B;
vector<vector<int>> ground;
int getResult(int h, vector<vector<int>> g) {
	int result = 0 ; //Time, Height
	int blk = B;
	for (auto i : ground) {
		for (auto j : i) {
			if (h >= j) {
				blk -= (h - j);
				result += 1 * (h - j);
			}
			else {
				blk += (j-h);
				result += 2 * (j-h);
			}
		}
	}
	//cout << result<<" "<< h << "\n";
	if (blk >= 0)return result;
	else return INT32_MAX;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M >> B;
	ground.resize(N, vector<int>(M));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> ground[i][j];
		}
	}
	vector<int> locMin = { INT32_MAX,0 };
	for (int i = 0; i < 257; i++) {
		int localResult = getResult(i, ground);
		if (localResult <= locMin[0]) {
			locMin[0] = localResult;
			locMin[1] = i;
		}
	}
	cout << locMin[0] << " " << locMin[1] << "\n";
}
