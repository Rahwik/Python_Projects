import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Plotting the bar chart
plt.bar(languages, popularity, color='skyblue')

# Customize the plot
plt.xlabel('Programming Language')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')
plt.ylim(0, 25)  # Adjust the y-axis limits if needed

# Show the plot
plt.show()
