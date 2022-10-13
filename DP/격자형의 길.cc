#include<iostream>
#include<vector>

using namespace std;
int H, W;
vector<vector<int>> DP;
vector<vector<bool>> isVisitable;
int search(int x, int y) {
	if (x >= H || y >= W || !(isVisitable[x][y]))return 0;
	if (x == H - 1 && y == W - 1)return 1;
	if (DP[x][y])return DP[x][y];
	return DP[x][y] = search(x + 1, y) + search(x, y + 1);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> H >> W;
	++H;++W;
	DP.resize(H, vector<int>(W));
	isVisitable.resize(H, vector<bool>(W));
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			int visit;
			cin >> visit;
			isVisitable[i][j] = !bool(visit);
		}
	}
	int result = search(0, 0);
	cout << result << endl;
}
