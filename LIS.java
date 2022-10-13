import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;
public class Main {
	
	int[] list;
	int[] dp;
		
	Main(int size,Scanner sc){
		this.list = new int[size];
		this.dp = new int[size];
		for(int i=0; i<size; i++) {
			this.list[i] = sc.nextInt();
		}
		Arrays.fill(this.dp,-1);
		
	}
	public void printing() {
		
	}
	public int solve(int start) {
		if(this.dp[start]!=-1) {
			return this.dp[start];
		}
		
		this.dp[start] =1 ;
			for(int next = start+1; next<this.list.length; next++) {
				if(this.list[start]<this.list[next]) {
					this.dp[start] = this.dp[start]>solve(next)+1?this.dp[start]:solve(next)+1;
				}	
		}
		return this.dp[start];
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		for(int i=0; i<total; i++) {
			Main main = new Main(sc.nextInt(),sc);
			int maxRet = 0;
			for(int j=0; j<main.list.length;j++) {
				maxRet = maxRet>main.solve(j)?maxRet:main.solve(j);
			}
			System.out.println(maxRet);
		}
		
		
	}

}
