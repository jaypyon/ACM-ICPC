#include<iostream>
#include<string>
using namespace std;
int N;

int findSeries(int n) {
	int count = 0;
	int idx = 0;
	int targetNumber = 666;
	string stringifiedNumber;
	while (true) {
		stringifiedNumber = to_string(targetNumber);
		for (int j = 0; j < stringifiedNumber.length() - 2;j++) {
			if (stringifiedNumber[j] == '6' && stringifiedNumber[j + 1] == '6' && stringifiedNumber[j + 2] == '6') {
				++count;
				break;
			}
		}
		if (count == n) {
			return targetNumber;
		}
		++targetNumber;
	}
}
int main() {
	cin >> N;
	int result = findSeries(N);
	cout << result << "\n";
}


