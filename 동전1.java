import java.util.*;
public class Main {

	int nc;
	int total;
	int[] coins;
	int[] dp;
	Main(){
		Scanner sc = new Scanner(System.in);
		nc = sc.nextInt();
		total = sc.nextInt();
		coins = new int[101];Arrays.fill(coins, 0);
		dp = new int[10001];
		Arrays.fill(dp, 0);
		
		int rc = 0;
		for(int i=0;i<nc;i++) {
			int temp = sc.nextInt();
			if(temp<10000) {
				coins[rc]=temp;
				++rc;
			}
		}
		nc = rc;
		
		
	}
	public int solve() {
		 
		dp[0] = 1; 
		for (int i = 0; i < nc; i++) { 
			for (int j = coins[i]; j <= total; j++) { 
				dp[j] = dp[j] + dp[j - coins[i]]; 
			} 
		}
		return dp[total];

	}

	
	public static void main(String[] args) {
		
		Main main = new Main();
		System.out.print(main.solve());
	}

}
