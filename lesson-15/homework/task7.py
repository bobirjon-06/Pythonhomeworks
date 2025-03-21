import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['r', 'g', 'b', 'y', 'orange']

plt.figure(figsize=(8, 5))
plt.bar(products, sales, color=colors)

plt.title("Sales Data")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
