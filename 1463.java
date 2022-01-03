import java.util.*;
public class Main {

	int[] dp;
	Main(int total){
		dp = new int[total+1];
		dp[1]=0;
		dp[2]=1;
		dp[3]=1;
	}
	public int solve() {
		for(int i=4; i<dp.length;i++) {
			dp[i] = dp[i-1]+1;
			if(i%2 ==0) {
				dp[i] = dp[i]<dp[i/2]+1?dp[i]:dp[i/2]+1;
			}
			if(i%3 ==0) {
				dp[i] = dp[i]<dp[i/3]+1?dp[i]:dp[i/3]+1;
			}
		}
		return dp[dp.length-1];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		if(total==1)System.out.print(0);
		else if(total==2)System.out.print(1);
		else if(total==3)System.out.print(1);
		else {
			Main main = new Main(total);
			System.out.print(main.solve());
			
		}
	}

}
