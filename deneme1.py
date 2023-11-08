import matplotlib.pyplot as plt
import numpy as np

# Verilerinizin örnek hali (örnek veri, gerçek verilerinizi kullanmalısınız)
data = [(100, [10, 12, 11]), (200, [22, 21, 25]), (300, [35, 31, 32])]

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

# Daha fazla nokta eklemek için interpolasyon kullanın
displacements_interp = np.linspace(min(displacements), max(displacements), 100)
average_speeds_interp = np.interp(displacements_interp, displacements, average_speeds)

plt.plot(displacements_interp, average_speeds_interp, marker='o', color='orange')
plt.xlabel('Yer Değiştirme (m)')
plt.ylabel('Ortalama Hız (m/s)')
plt.title('Yer Değiştirme ve Ortalama Hız Grafiği (Detaylı)')
plt.grid(True)

plt.tight_layout()
plt.show()
