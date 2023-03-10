# python3

def parallel_processing(n, m, data):
    output = []
    starts = [0] * n
    threads = []
    for i in range(n):
        # 0 ir thread sākuma laiks, un i ir tā indekss
        thread = (0, i)
        threads.append(thread)


    for i in range(m):
        time = data[i]
        start, thread = min(threads)
        output.append((thread, start))

        starts[thread] += time
        threads[thread] = (starts[thread], thread)
        
        
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # n - thread count 
    # m - job count

    result = parallel_processing(n,m,data)
    
    for thread, start in result:
        print(thread, start)



if __name__ == "__main__":
    main()
