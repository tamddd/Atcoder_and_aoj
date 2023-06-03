#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n;cin>>n;
  vector<vector<int> > dp(n+1, vector<int>(10100));
  dp[0][0] = 1;
  vector<int>a;

  for (int i = 0;i < n; i++){
	  int nm;cin>>nm;
	  a.push_back(nm);
  }

  for (int i = 0; i < n; i++){
	for (int j = 0; j < 10100; j++){
	  if (dp[i][j]){
		dp[i+1][j] = 1;
		dp[i+1][j+a[i]] = 1;
	  }
	}
  }
  int ans = 0;
  for (int i = 0; i < 10100; i++){
	if (i%10!=0 && dp[n][i])
	  ans = max(ans, i);
  }
  cout << ans << endl;
}
