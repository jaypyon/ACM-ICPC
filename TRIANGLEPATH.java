import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;
public class Main {
	
	int th;
	int[][] triangle;
	int [][] dp;
	
	Main(int th,Scanner sc){
		this.triangle = new int[101][101];
		this.dp = new int[101][101];
		this.th = th;
		for(int[] arr : this.triangle)
			Arrays.fill(arr,-1);// -1 접근불가영역
		for(int[] arr : this.dp)
			Arrays.fill(arr,-1);// -1 접근불가영역
			
		for(int i = 0; i<this.th;i++) {
			for(int j =0; j<=i;j++) {
				this.triangle[i][j] = sc.nextInt();
			}
		}
	}
	public void printing() {
		for(int i = 0; i<this.th;i++) {
			System.out.println();
			for(int j =0; j<=i;j++) {
				System.out.print(this.dp[i][j]);System.out.print(' ');
			}
		}
	}
	public int solve(int pi, int pj) {

		//
		if(triangle[pi][pj]==-1)return 0;
		if(this.dp[pi][pj]!=-1)return this.dp[pi][pj];
		if(pi<this.th&&pj<this.th) {
			int temp = solve(pi+1,pj+1)>=solve(pi+1,pj)?
					triangle[pi][pj]+solve(pi+1,pj+1):triangle[pi][pj]+solve(pi+1,pj);
			//System.out.println(temp);
			return this.dp[pi][pj]=temp;
		}

		
		return this.dp[pi][pj];
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		for(int i=0; i<total; i++) {
			Main main = new Main(sc.nextInt(),sc);
			System.out.print(main.solve(0,0));
			System.out.println();
			//main.printing();
			
		}
		
		
	}

}
