
import matplotlib.pyplot as plt
import csv

def read_csv(file):
    first =[]
    second = []
    with open(file) as csvf:
        data_csv = csv.reader(csvf)
        for row in data_csv:
            first.append(int(row[0])*0.000001)
            second.append(int(row[1])*0.000001)

    return first,second



if __name__ == "__main__":
    jitter_not_filtered, jitter_filtered = read_csv("jitter_last.csv")
    assert(len(jitter_filtered) == len(jitter_not_filtered))
    fig, (ax1, ax2) = plt.subplots(2,1)

    ax1.set_title("Jitter filtered")
    ax1.hist(x=jitter_filtered, bins=30, range=(-.5,.5))
    ax1.grid(True)
    ax1.set_xlabel("jitter ms") 
    ax1.set_xlim(-.5,.5) 
    ax1.set_ylabel("No. samples")

    ax2.set_title("Jitter not filtered")
    ax2.hist(x=jitter_not_filtered, bins=30, range=(-.5,.5))
    ax2.grid(True)
    ax2.set_xlabel("jitter ms")
    ax2.set_xlim(-.5,.5) 
    ax2.set_ylabel("No. samples")
    
    plt.show()