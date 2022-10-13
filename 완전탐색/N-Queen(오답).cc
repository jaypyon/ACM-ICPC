#include<iostream>
#include<vector>
using namespace std;
int N;
vector<vector<int>> chess;
vector<vector<int>> status;
int totalCount = 0;
vector<vector<int>> dir = {
	{1,-1}, {1,0},{1,1},
	{0,-1},        {0,1},
	{-1,-1}, {-1,0},{-1,1},
};
void printStatus() {
	for (auto i : chess) {
		for (auto j : i) {
			cout << j << " ";
		}
		cout << endl;
	}
	cout << endl;
}
bool isInBox(int x, int y) {
	if (x >= 0 && x < N && y >= 0 && y < N) return true;
	return false;
}
void checkStatus(int x, int y) {
	for (int i = 0; i < 8; i++) {
		int localX = x;
		int localY = y;
		while (isInBox(localX, localY)) {
			status[localX][localY]++;
			localX += dir[i][0];
			localY += dir[i][1];
		}
	}
}
void uncheckStatus(int x, int y) {
	for (int i = 0; i < 8; i++) {
		int localX = x;
		int localY = y;
		while (isInBox(localX, localY)) {
			status[localX][localY]--;
			localX += dir[i][0];
			localY += dir[i][1];
		}
	}
}
void checkChess(int x, int y) {
	chess[x][y]++;
}
void uncheckChess(int x, int y) {
	chess[x][y]--;
}
void DFS(int depth) {
	if (depth == N) {
		//printStatus();
		totalCount++;
		return;
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (status[i][j] == 0) {
				checkChess(i, j);
				checkStatus(i, j);
				DFS(depth + 1);
				uncheckStatus(i, j);
				uncheckChess(i, j);
			}
		}
	}
}

int main() {
	iostream::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	chess.resize(N, vector<int>(N));
	status.resize(N, vector<int>(N));
	DFS(0);

	int fact = 1;
	for (int i = 1; i <= N; i++)fact *= i;
	cout << int(totalCount / fact) << endl;
}
