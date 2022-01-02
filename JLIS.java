import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;
public class Main {

	int[] listA;
	int[] listB;
	int[][] dp;
		
	Main(int sizeA,int sizeB,Scanner sc){
		this.listA = new int[sizeA];
		this.listB = new int[sizeB];
		this.dp = new int[sizeA+1][sizeB+1];
		for(int i=0; i<sizeA; i++) {
			this.listA[i] = sc.nextInt();
		}for(int i=0; i<sizeB; i++) {
			this.listB[i] = sc.nextInt();
		}
		for(int[] arr : this.dp) {
			Arrays.fill(arr,-1);
		}	
	}
	
	public int solve(int startA,int startB) {
		if(this.dp[startA+1][startB+1] !=-1)return this.dp[startA+1][startB+1] ;
		this.dp[startA+1][startB+1] = 0;
		
		int a = startA==-1?-2147483648:this.listA[startA];
		int b = startB==-1?-2147483648:this.listB[startB];
		int localMax = a>b?a:b;
		
		
		for(int nextB=startB+1;nextB<this.listB.length;nextB++) {
			if(localMax<this.listB[nextB])
			this.dp[startA+1][startB+1] = this.dp[startA+1][startB+1]>solve(startA,nextB)+1?this.dp[startA+1][startB+1]:solve(startA,nextB)+1;
		}
		for(int nextA=startA+1;nextA<this.listA.length;nextA++) {
			if(localMax<this.listA[nextA])
			this.dp[startA+1][startB+1] = this.dp[startA+1][startB+1]>solve(nextA,startB)+1?this.dp[startA+1][startB+1]:solve(nextA,startB)+1;
		}
		//System.out.println(this.dp[startA+1][startB+1]);
		return this.dp[startA+1][startB+1];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		for(int k=0; k<total; k++) {
			int first = sc.nextInt();
			int second = sc.nextInt();

			Main main = new Main(first,second,sc);
			
			int maxRet = 0;
			maxRet = maxRet>main.solve(-1,-1)?maxRet:main.solve(-1,-1);
			
			System.out.println(maxRet);
		}
		
		
	}

}
