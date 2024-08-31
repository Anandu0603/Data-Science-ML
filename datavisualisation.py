import matplotlib.pyplot as plt
import numpy as np


months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


affordable_sales = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650])
luxury_sales = np.array([80, 130, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630])
super_luxury_sales = np.array([60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610])


plt.scatter(months, affordable_sales, color='green', label='Affordable Segment')
plt.scatter(months, luxury_sales, color='yellow', label='Luxury Segment')
plt.scatter(months, super_luxury_sales, color='blue', label='Super Luxury Segment')


plt.title('Sales of Cars by Segment')
plt.xlabel('Months of the Year')
plt.ylabel('Sales of Segment')


-
plt.show()
