int findMinimumOffloadTime(int n, vector b, vector t){
    # sort buildings ascending
    # sort offload times descending and calculate max time => building open + offload
sort(b.begin(), b.end());
sort(t.begin(), t.end(), greater());
int ans = INT_MIN;
for(int i=0;i<n;i++){
ans = max(ans, b[i]+t[i*4]);
}
return ans;
}