#include<iostream>
#include<vector>
using namespace std;
int N;
vector<int> chess;
int totalCount = 0;

bool checkChess(int depth) {
	for (int i = 0; i < depth; i++) {
		if (chess[i] == chess[depth] || abs(chess[i] - chess[depth]) == abs(i - depth)) return false;
	}
	return true;
}

void DFS(int depth) {
	if (depth == N) {
		totalCount++;
		return;
	}
	for (int i = 0; i < N; i++) {
		chess[depth] = i;
		if (checkChess(depth)) {
			DFS(depth + 1);
		}
	}
}

int main() {
	iostream::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	chess.resize(N, -1);
	DFS(0);
	cout << totalCount << "\n";
}
