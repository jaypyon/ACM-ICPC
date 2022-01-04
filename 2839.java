import java.util.*;
public class Main {

	int bag;
	int []dp;
	Main(int bag){
		this.bag = bag;
		this.dp = new int [5001];
		Arrays.fill(this.dp,-1);
	}
	public int solve() {
		this.dp[3]=1;
		this.dp[5]=1;
		
		for(int i=6;i<=this.bag;i++) {
			if(this.dp[i-3]!=-1||this.dp[i-5]!=-1) {
				if(this.dp[i-3]!=-1&&this.dp[i-5]!=-1) {
					this.dp[i] = this.dp[i-3]>this.dp[i-5]? this.dp[i-5]+1:this.dp[i-3]+1;
				}
				else if(this.dp[i-3]!=-1&&this.dp[i-5]==-1) {
					this.dp[i] = this.dp[i-3]+1;
				}
				else if(this.dp[i-3]==-1&&this.dp[i-5]!=-1) {
					this.dp[i] =this.dp[i-5]+1;
				}
			}
			else this.dp[i] = -1;
		}
		return this.dp[this.bag];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int numOfBag = sc.nextInt();
		Main main = new Main(numOfBag);
		System.out.println(main.solve());
	}

}
