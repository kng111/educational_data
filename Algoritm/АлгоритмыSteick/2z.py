def tree_height_bottom_up(parents):
    depth = [-1] * len(parents) + [0]

    def count_depth(i):
        if depth[i] == -1:
            depth[i] = count_depth(parents[i]) + 1
        return depth[i]

    return max(count_depth(i) for i in range(len(parents)))


def main():
    n_ = input()
    parents = [int(i) for i in input().split()]

    print(tree_height_bottom_up(parents))


if __name__ == "__main__":
    main()