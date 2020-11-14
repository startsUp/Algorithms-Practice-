int minChange(int n, vector<vector> productRatings, int ratingsThreshold) {
int changes = 0;

float numerator = 0;
float threshold = n * ratingsThreshold / 100.0;

auto comp = [] (vector<int>& ratings1, vector<int>& ratings2) {
        if(ratings1[0] == ratings1[1]) return true;
        if(ratings2[0] == ratings2[1]) return false;

        float change1 = ((float) ratings1[0] + 1)/(ratings1[1] + 1) - ((float) ratings1[0]/ratings1[1]);
        float change2 = ((float) ratings2[0] + 1)/(ratings2[1] + 1) - ((float) ratings2[0]/ratings2[1]);

        return change1 < change2;

};
priority_queue<vector<int>, vector<vector<int>>, decltype(comp)> pq(comp);

for(auto ratings : productRatings) {
    numerator += (float) ratings[0]/ratings[1];     
    pq.push(ratings);
}

while(numerator < threshold) {
    vector<int> toChange = pq.top();
    pq.pop();

    float change = (float) toChange[0]/toChange[1];
    toChange[0]++;
    toChange[1]++;
    change = (float) toChange[0]/toChange[1] - change;

    numerator += change;
    changes++;
    pq.push(toChange);
}

return changes;
}