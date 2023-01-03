int factorielle(int n) {
    return n < 2 ? 1 : n * factorielle(n - 1);
}
