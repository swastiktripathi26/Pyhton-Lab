time = float(input("Input time in seconds: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("Time in Hours:", hour,"Time in Minutes:", minutes, "Time in Seconds:", seconds, sep='\n')
