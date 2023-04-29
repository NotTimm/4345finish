class exampleObj {
    public:
        int x, y;
        exampleObj clone() {
            exampleObj next;
            next.x = this->x;
            next.y = this->y;
            return next;
        }
};
int main() {
    exampleObj first;
    first.x = 1;
    first.y = 10;
    exampleObj second = first.clone();
}