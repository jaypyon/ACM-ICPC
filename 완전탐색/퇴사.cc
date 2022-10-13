#include<iostream>

using namespace std;

int P[16] = { 0 };
int T[16] = { 0 };
int N; 
int maxCost = 0;
void DFS(int day, int cost) {

	// day가 N이상일 때, maxCost 갱신하고 종료한다. 
	if (day >= N) {
		maxCost = max(maxCost,cost);
		return;
	}
	// day는 0~N이상까지 보내지고, N이상으로 보내졌을때는 1번의 종료조건을 탄다.
	if (day + 1 <= N)DFS(day + 1, cost);
	if (day + T[day] <= N)DFS(day + T[day], cost + P[day]);
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> T[i] >> P[i];
	}
	DFS(0, 0);
	cout << maxCost;
}
