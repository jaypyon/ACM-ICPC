#include<iostream>
#include<vector>
using namespace std;
int N,M;
vector<bool> isInNow;
vector<int> nmArr = { 0 };
void getNM(int depth, vector<bool> status, vector<int> now) {
	if (depth >= M) { for (auto i : now) { if (i == 0) continue; cout << i << " "; }cout << "\n";return; }
	for (int i = now.back(); i < N; i++) {
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

/*
- N과 M (1)과 다른 점
	1. 결과 출력을 위한 임시 벡터 nmArr에 원소가 없는 경우(최초 기동시 원소 없음)를 방지하기 위해 0을 가진 벡터로 초기화하였고, 출력부분(종료조건)에서는 continue 작성
	2. getNM 내부의 i값이 가장 마지막에 있는 원소(vector back 함수 사용)로 초기화 됨.
*/
