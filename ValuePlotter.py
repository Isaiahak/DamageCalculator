import matplotlib.pyplot as plt



def valuePlotter(map): 
    keys = list(map.keys())
    values = list(map.values())
    plt.scatter(keys, values)  
    plt.plot(keys, values, linestyle='-', marker='.', color='black')
    
    ###for key, value in map.items():
      ###  plt.annotate(f'{value}', (key, value), textcoords="offset points", xytext=(0, 5), ha='center') 
        
    plt.title("Dps over a BA")
    plt.xlabel("Time")
    plt.ylabel("Damage [Billions per second]")
    plt.legend() 
     
    plt.show()


def main():
    my_duct = {1:2, 2:4, 3:10}
    valuePlotter(my_duct)
    
if __name__ == "__main__":
    main()