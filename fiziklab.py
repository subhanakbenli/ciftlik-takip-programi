import numpy as np
import matplotlib.pyplot as plt
# Verilerinizin örnek hali (örnek veri, gerçek verilerinizi kullanmalısınız)
data = [
(80, [1.855, 1.860, 1.852]), 
(70, [1.544, 1.559, 1.552]), 
(60, [1.313, 1.308, 1.302]),
(50, [1.095, 1.097, 1.094]),
(40, [0.877, 0.874, 0.874]),
(30, [0.662, 0.660, 0.658]),
(20, [0.432, 0.434, 0.433]),
(10, [0.211, 0.210, 0.204])]

# Ortalama zamanları ve yer değiştirme için boş listeler
average_times = []
displacements = []

# Ortalama zamanları ve yer değiştirme hesaplamak için işlevler
def calculate_average_time(times):
    return sum(times) / len(times)

# Verileri işleyin ve ortalamaları hesaplayın
for distance, times in data:
    average_time = calculate_average_time(times)
    average_times.append(average_time)
    displacements.append(distance)

# Yer değiştirme ve zaman grafiği
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(displacements, average_times, marker='o')
plt.xlabel('Yer Değiştirme (m)')
plt.ylabel('Ortalama Zaman (saniye)')
plt.title('Yer Değiştirme ve Ortalama Zaman Grafiği')
plt.grid(True)

# Yer değiştirme ve hız grafiği
plt.subplot(1, 2, 2)
average_speeds = [distance / time for distance, time in zip(displacements, average_times)]
plt.plot(displacements, average_speeds, marker='o', color='red')
plt.xlabel('Displacement (cm)')
plt.ylabel('Average Velocity (cm/s)')
plt.title('Displacement and Average Velocity Graph')
plt.grid(True)

plt.tight_layout()
plt.show()
