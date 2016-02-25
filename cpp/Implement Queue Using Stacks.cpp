#include<cstdio>
#include<stack>
using namespace std;

class Queue {
    stack<int> input, output;
public:

    void push(int x) {
        input.push(x); 
    }

    void pop(void) {
        peek();
        output.pop();
    }

    int peek(void) {
        if (output.empty()) // only when output is empty
            while (input.size())
                output.push(input.top()), input.pop();
        return output.top();
    }

    bool empty(void) {
        return input.empty() && output.empty();
    }
};
/*
class Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
        while(!pop_stack.empty()){
			int i = pop_stack.top();
			pop_stack.pop();
			push_stack.push(i);
		}
		push_stack.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        while(!push_stack.empty()){
			int i = push_stack.top();
			push_stack.pop();
			pop_stack.push(i);
		}
		pop_stack.pop();
    }

    // Get the front element.
    int peek(void) {
        while(!push_stack.empty()){
			int i = push_stack.top();
			push_stack.pop();
			pop_stack.push(i);
		}
		return pop_stack.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        return push_stack.empty() && pop_stack.empty();
    }
private:
	stack<int> push_stack;
	stack<int> pop_stack;
};*/

int main(){
	Queue q;
	printf("%d ", q.empty());
	q.push(1);
	printf("%d ", q.empty());
	q.push(2);
	printf("%d ", q.peek());
	q.pop();
	printf("%d ", q.peek());
	return 0;
}