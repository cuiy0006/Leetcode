class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        int minVal = x;
        if(v.size() > 0){
            minVal = min(minVal, v[v.size() - 1]);
        }
        v.push_back(x);
        v.push_back(minVal);
    }
    
    void pop() {
        v.pop_back();
        return v.pop_back();
    }
    
    int top() {
        return v[v.size() - 2];
    }
    
    int getMin() {
        return v[v.size() - 1];
    }
private:
    vector<int> v;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
