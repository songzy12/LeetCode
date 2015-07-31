#include<queue>
#include<cstdio>
using namespace std;
class Stack {
public:
    // Push element x onto stack.
    void push(int x) {
        queue<int> *f, *e;
		f = q1.empty()?&q0:&q1;
		e = q1.empty()?&q1:&q0;
		e->push(x);
		while(!f->empty()){
			int i = f->front();
			f->pop();
			e->push(i);
		}
    }

    // Removes the element on top of the stack.
    void pop() {
		q0.empty()?q1.pop():q0.pop();
    }

    // Get the top element.
    int top() {
		return q0.empty()?q1.front():q0.front();
    }

    // Return whether the stack is empty.
    bool empty() {
        return q0.empty() && q1.empty();
    }
private:
	queue<int> q0;
	queue<int> q1;
};

int main(){
	Stack q;
	printf("%d ", q.empty());
	q.push(1);
	printf("%d ", q.empty());
	q.push(2);
	printf("%d ", q.top());
	q.pop();
	printf("%d ", q.top());
	return 0;
}