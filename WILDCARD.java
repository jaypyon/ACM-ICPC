import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;
public class Main {

	char[] w;
	char[] s;
	ArrayList<String> fileNames;
	int [][] dp;// 1일치 0불일치 -1정의되지않음
	
	Main(String wild, ArrayList<String> fileNames){
		this.w = wild.toCharArray();
		this.fileNames = fileNames;
		this.dp = new int[101][101];
	}
	public void printing() {
		
	}
	public int match(int wi, int si) {
		if(dp[wi][si]!=-1) {
			return dp[wi][si];
		}
		if(wi<w.length&&si<s.length)
			if(w[wi]=='?'||w[wi]==s[si]) {
				return dp[wi][si] = match(wi+1,si+1);
			}
		if(wi == w.length) {
			return dp[wi][si]=(si==s.length)?1:0;
		}
		if(w[wi]=='*') {
			if(match(wi+1,si)==1||(si<s.length&&match(wi,si+1)==1))return dp[wi][si] =1;
		}
		return dp[wi][si] = 0;
	}
	public void solve() {
		ArrayList<String>resFileName = new ArrayList<String>();
		for(int i=0; i<fileNames.size();i++) {
			for(int[] arr: this.dp) {
				Arrays.fill(arr, -1);//memset
			}
			String fileName = fileNames.get(i);
			s = fileName.toCharArray();
			if(match(0,0)==1) {
				resFileName.add(fileName);
			}
		}
		Collections.sort(resFileName);
		for(int i=0; i<resFileName.size();i++) {

			System.out.println(resFileName.get(i));
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int numTextCase = sc.nextInt();
		
		for(int i=0; i<numTextCase;i++) {
			String wild = sc.next();
			int numFileNames = sc.nextInt();
			
			ArrayList<String> fileNames = new ArrayList<String>();
			for(int j=0; j<numFileNames; j++) {
				fileNames.add(sc.next());
			}
			Main algo = new Main(wild,fileNames);
			algo.solve();
			
		}
	}

}
